# interface-xp

Web interface for Extreme Programming practices: real-time pair programming sessions with Driver/Navigator roles and client feedback on sprint increments.

## Stack

- Python + Flask
- Flask-SocketIO (WebSockets)
- HTML / CSS / JS
- SQLite
- pytest

## Setup

**Local:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

**Docker:**
```bash
docker build -t interface-xp .
docker run -p 5000:5000 interface-xp
```

**Tests:**
```bash
pytest
```

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md).
