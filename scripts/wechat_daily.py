"""Send a short WeChat notice linking to today's published Chinese briefing."""

import asyncio
import base64
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from cryptography.fernet import Fernet, InvalidToken

from src.models import WeChatConfig
from src.services.wechat import SESSION_FILE, WeChatNotifier
from src.storage.manager import StorageManager


def briefing_message(post: Path, repository: str) -> str:
    date = post.name.removesuffix("-summary-zh.md")
    body = post.read_text(encoding="utf-8")
    headlines = re.findall(r"^### \[(.+?)\]\(", body, re.MULTILINE)[:3]
    overview = re.search(r"^> (.+)$", body, re.MULTILINE)
    lines = [f"Horizon 中文日报 · {date}"]
    if overview:
        lines.append(overview[1])
    lines.extend(f"{n}. {title[:100]}" for n, title in enumerate(headlines, 1))
    lines.append(f"阅读全文：https://github.com/{repository}/blob/gh-pages/_posts/{post.name}")
    return "\n".join(lines)


def main() -> None:
    post = Path(sys.argv[1])
    message = briefing_message(post, os.environ["GITHUB_REPOSITORY"])
    seed = os.environ["HORIZON_WECHAT_SESSION"].encode()
    token = json.loads(seed)["bot_token"].encode()
    cipher = Fernet(base64.urlsafe_b64encode(hashlib.sha256(b"horizon-wechat-cache-v1:" + token).digest()))
    cache = Path(os.environ["RUNNER_TEMP"]) / "wechat-session.enc"
    state = seed
    if cache.exists():
        try:
            state = cipher.decrypt(cache.read_bytes())
        except InvalidToken:
            # A new QR login supplies a new token, invalidating the old cache.
            pass
    with TemporaryDirectory() as private_dir:
        path = Path(private_dir) / SESSION_FILE
        path.write_bytes(state)
        notifier = WeChatNotifier(WeChatConfig(enabled=True), StorageManager(private_dir))
        try:
            result = asyncio.run(notifier.send_text(message))
        finally:
            cache.write_bytes(cipher.encrypt(path.read_bytes()))
    if not result.sent:
        raise SystemExit("WeChat delivery failed. Check the bot conversation.")


if __name__ == "__main__":
    main()
