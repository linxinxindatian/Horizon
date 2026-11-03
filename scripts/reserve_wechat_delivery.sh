#!/usr/bin/env bash
# Exit 10 when another run owns this edition. Leave ambiguous sends reserved.
set -eu
: "${DELIVERY_TAG:?Missing edition tag}" "${GITHUB_SERVER_URL:?}" "${GITHUB_REPOSITORY:?}" "${GITHUB_RUN_ID:?}"
ref="refs/tags/$DELIVERY_TAG"
if git ls-remote --exit-code --refs origin "$ref" >/dev/null; then
  exit 10
else
  status=$?
  [[ "$status" == 2 ]] || exit "$status"
fi

# A unique annotated object per run makes racing pushes conflict even at the same HEAD.
git -c user.name='Horizon delivery' -c user.email='actions@users.noreply.github.com' \
  tag -a "$DELIVERY_TAG" -m "Delivery reserved by $GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID (attempt ${GITHUB_RUN_ATTEMPT:-1})"
git push origin "$ref:$ref"
