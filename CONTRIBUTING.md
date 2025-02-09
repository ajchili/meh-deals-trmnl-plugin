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
./bin/setup.sh
```

### 3. Start the development servers

From the root directory run

```bash
docker compose up
```

### 4. Navigate to the trmnl_preview

Open [http://localhost:4567](http://localhost:4567) in your browser of choice and start making changes!

_Note: for any backend changes, you will need to poll the sever for new data!_
