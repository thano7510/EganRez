import os
from datetime import datetime, timezone

LOG_FILE = "/tmp/log.txt"

def log(text):
    now = datetime.now(timezone.utc).isoformat()
    prefix = f"[{os.getenv('REQUEST_ID', 'worker')}]"
    line = f"{now} {prefix} {text}\n"
    print(line.strip())
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line)
        f.flush()  
