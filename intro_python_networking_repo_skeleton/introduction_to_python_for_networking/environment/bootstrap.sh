#!/usr/bin/env bash
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$here/.." && pwd)"

echo "[bootstrap] Python: $(python3 --version || true)"
python3 -m venv "$repo_root/.venv"
source "$repo_root/.venv/bin/activate"
python -m pip install --upgrade pip
pip install -r "$here/requirements.txt"

# Install Ansible core and common network collections (for Lab 06)
pip install "ansible-core>=2.16,<2.18" || true
ansible-galaxy collection install community.network cisco.ios junipernetworks.junos || true

# Pre-commit (optional but recommended)
if [ -f "$repo_root/ci/pre-commit-config.yaml" ]; then
  pre-commit install -c "$repo_root/ci/pre-commit-config.yaml" --install-hooks || true
fi

# Quick smoke
python - <<'PY'
import importlib
for m in ("netmiko","requests","jinja2","yaml","textfsm","pysnmp"):
    importlib.import_module(m)
print("imports: ok")
PY

echo "[bootstrap] Done. Activate with: source .venv/bin/activate"
