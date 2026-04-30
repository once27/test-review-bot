import json
import datetime

def log_event(level, message, **kwargs):
    payload = {
        "timestamp": str(datetime.datetime.utcnow()),
        "level": level,
        "message": message,
        **kwargs
    }
    print(json.dumps(payload))
