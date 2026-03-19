from time import time
from fastapi import HTTPException

requests_log = {}

LIMIT = 5
WINDOW = 60

def rate_limit(user):
    now = time()

    if user not in requests_log:
        requests_log[user] = []

    # Keep only recent requests
    requests_log[user] = [t for t in requests_log[user] if now - t < WINDOW]

    if len(requests_log[user]) >= LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    requests_log[user].append(now)