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

echo ">>> Using repository URL: $REPO_URL"

ensure_git_filter_repo() {
  if command -v git-filter-repo >/dev/null 2>&1; then
    return
  fi

  if command -v brew >/dev/null 2>&1; then
    echo ">>> Installing git-filter-repo via Homebrew..."
    brew install git-filter-repo
  fi

  if command -v git-filter-repo >/dev/null 2>&1; then
    return
  fi

  if command -v pipx >/dev/null 2>&1; then
    echo ">>> Installing git-filter-repo via pipx..."
    pipx install git-filter-repo
  fi

  if command -v git-filter-repo >/dev/null 2>&1; then
    return
  fi

  echo ">>> Installing git-filter-repo via python3 -m pip --user..."
  python3 -m pip install --user git-filter-repo

  if [[ -x "$HOME/.local/bin/git-filter-repo" ]]; then
    export PATH="$HOME/.local/bin:$PATH"
  fi

  if ! command -v git-filter-repo >/dev/null 2>&1; then
    echo "error: git-filter-repo installation failed." >&2
    exit 1
  fi
}

ensure_git_filter_repo

WORK_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t history-scrub)"
cleanup() {
  rm -rf "$WORK_DIR"
}
trap cleanup EXIT

MIRROR_DIR="$WORK_DIR/repo.git"

echo ">>> Mirror-cloning repository..."
git clone --mirror "$REPO_URL" "$MIRROR_DIR"

cd "$MIRROR_DIR"

echo ">>> Rewriting history to drop client_requirements.png ..."
git filter-repo --force \
  --path client_requirements.png \
  --path-glob '*/client_requirements.png' \
  --path-glob '**/client_requirements.png' \
  --invert-paths


echo ">>> Expiring reflogs and compacting the mirror ..."
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo ">>> Force pushing rewritten history to origin ..."
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REPO_URL"
else
  git remote add origin "$REPO_URL"
fi
git push --mirror --force origin

cat <<'EON'
>>> History rewrite complete.

Next steps:
  1. Run verify_scrub.sh to confirm the sensitive filename and commits are gone.
  2. Commit and publish POST-REWRITE-NOTICE.md so collaborators re-clone.
  3. File github-support-ticket.txt to request cache and PR purge.
  4. Rebuild the teaching overlay from the provided here-doc block.
EON
