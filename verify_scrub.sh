#!/usr/bin/env bash
set -euo pipefail

if ! command -v git >/dev/null 2>&1; then
  echo "error: git is required to run this script." >&2
  exit 1
fi

REPO_URL="${REPO_URL:-}"
if [[ -z "$REPO_URL" ]]; then
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    REPO_URL="$(git remote get-url origin)"
  else
    echo "error: set REPO_URL or run inside a clone with an origin remote." >&2
    exit 1
  fi
fi

TMP_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t verify-scrub)"
cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

CLONE_DIR="$TMP_DIR/repo"

echo ">>> Cloning $REPO_URL for verification ..."
git clone --quiet "$REPO_URL" "$CLONE_DIR"

cd "$CLONE_DIR"

echo ">>> Scanning commit history for client_requirements.png ..."
FOUND_PATH=0
while IFS= read -r commit; do
  paths="$(git ls-tree -r --name-only "$commit")"
  if [[ -n "$paths" ]] && grep -F 'client_requirements.png' <<<"$paths" >/dev/null 2>&1; then
    echo "error: client_requirements.png detected in commit $commit" >&2
    FOUND_PATH=1
    break
  fi
done < <(git rev-list --all)

if (( FOUND_PATH )); then
  exit 1
fi
echo ">>> OK: client_requirements.png not found in any tree."

echo ">>> Checking for legacy SHAs 14bce63 and 2ffc08d ..."
if git rev-list --all | grep -E '(14bce63|2ffc08d)' >/dev/null 2>&1; then
  echo "error: legacy SHAs still exist in the commit graph." >&2
  exit 1
fi

echo ">>> Verification successful: sensitive artifacts and legacy SHAs are absent."
