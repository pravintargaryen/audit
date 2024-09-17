from fastapi import FastAPI, WebSocket, Depends, HTTPException, Query
from utils.encryption import encrypt_log
from utils.database import create_db, insert_log, fetch_logs
import requests
import logging

app = FastAPI()

# Initialize DB
create_db()

OPA_URL = "http://localhost:8181/v1/data/authorization/allow"

logging.basicConfig(level=logging.INFO)

def check_authorization(user, action, resource):
    payload = {
        "input": {
            "role": user,
            "action": action,
            "resource": resource
        }
    }
    response = requests.post(OPA_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("result")
    else:
        return False

@app.post("/access")
async def access_resource(user: str = Query(...), action: str = Query(...), resource: str = Query(...)):
    decision = check_authorization(user, action, resource)
    
    # Log the access attempt
    log_entry = f"User {user} attempted {action} on {resource}. Decision: {decision}"
    encrypted_log = encrypt_log(log_entry)
    insert_log(user, action, resource, decision, encrypted_log)

    if not decision:
        raise HTTPException(status_code=403, detail="Access Denied")
    
    return {"status": "Access Granted"}

@app.get("/logs")
async def get_logs():
    logs = fetch_logs()
    return {"logs": logs}

@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await websocket.accept()
    while True:
        logs = fetch_logs()
        await websocket.send_json({"logs": logs})
