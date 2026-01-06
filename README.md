# Installation

## Prerequisites
### Install uv (recommended):

**Windows (PowerShell):**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Alternative: Using pip
If you prefer not to use uv, you can use Python's built-in pip (see below).

## Setup

**Clone the repository:**
```bash
git clone https://github.com/neadecode/image-to-ascii
cd image-to-ascii
```

**With uv:**
```bash
uv sync
```

**With pip:**
```bash
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -e .
```

## Usage

**With uv:**
```bash
uv run python ascii.py 
```

**With activated virtual environment:**
```bash
python ascii.py 
```
