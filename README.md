# User Activity Analytics

This project focuses on analyzing user activity from various log sources.

## Project Structure

- `app/`: Core application logic for loading, parsing, normalizing, analyzing, and summarizing logs.
  - `log_loader.py`: Loads raw log files.
  - `parsers.py`: Parses log formats from different sources.
  - `normalizer.py`: Normalizes events into a consistent structure.
  - `analytics.py`: Computes analytics metrics from normalized logs.
  - `detector.py`: Detects activity patterns, anomalies, or other notable behavior.
  - `insights.py`: Generates insights based on analytics results.
  - `pipeline.py`: Orchestrates the end-to-end log processing flow.
  - `main.py`: Defines FastAPI endpoints for health, logs, analytics, and insights.
- `logs/`: Stores various log files.
- `requirements.txt`: Lists project dependencies.

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the FastAPI server with Uvicorn from the project root:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then access the API endpoints:

- `GET /health` - health check
- `GET /logs` - normalized log output
- `GET /analytics` - analytics results
- `GET /insights` - generated insights
- `GET /summary` - combined summary of logs, analytics, and insights

> Note: `pd.py` is a local learning file and is intentionally excluded from the public project documentation.