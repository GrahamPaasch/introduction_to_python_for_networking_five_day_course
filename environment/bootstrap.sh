#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"

if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1090
source "${VENV_DIR}/bin/activate"

pip install --upgrade pip
pip install -r "${ROOT_DIR}/environment/requirements.txt"

python <<'PY'
import importlib

modules = [
    "requests",
    "yaml",
    "jinja2",
    "netmiko",
    "napalm",
    "textfsm",
    "pysnmp",
    "ansible"
]

for module in modules:
    importlib.import_module(module)

print("Smoke test imports succeeded.")
PY


echo "Virtual environment ready. Activate with: source \"${VENV_DIR}/bin/activate\""
