# Contributing

## Prerequisites

- [uv](https://docs.astral.sh/uv/)
- Docker

## Getting Started

### 1. Clone repo

Follow https://docs.github.com/en/get-started/quickstart/fork-a-repo

### 2. Install dependencies

From the root directory run

```bash
uv sync
```

### 3. Start the python servers

From the root directory run

```bash
uv run fastapi dev src/main.py
```

\_Note: For UI development I currently use the [TRMNL plugin editor](https://usetrmnl.com/plugin_settings?keyname=private_plugin).\_
