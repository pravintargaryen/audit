# FastAPI Authorization & Logging System

This project is a simple FastAPI-based Authorization and Logging system that interacts with an Open Policy Agent (OPA) to make access decisions. It also provides real-time log streaming via WebSockets.

## Features

- **Authorization Layer**: Uses OPA for policy-based access control.
- **Logging**: Logs all access attempts with encrypted logs stored in SQLite.
- **Real-time Logs**: Provides a WebSocket endpoint to stream logs in real-time.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- SQLite
- Open Policy Agent (OPA)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/pravintargaryen/audit.git
cd your-repository-name
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Open Policy Agent (OPA)

1. Download OPA
2. Start the OPA server

```bash
./opa run --server --addr http://localhost:8181

```

3. Load your authorization policy into OPA.

```bash
opa policy add authorization policy.rego

```

4. Start the FastAPI Server

```bash
uvicorn main:app --reload

```
