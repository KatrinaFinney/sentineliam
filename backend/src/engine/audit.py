import json
from pathlib import Path
from datetime import datetime
from supabase_client.client import supabase

LOG_QUEUE = Path(".sentinel/logs/queue.json")
LOG_QUEUE.parent.mkdir(parents=True, exist_ok=True)

def push_audit(action, input_data, result, user_id=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "user_id": user_id,
        "input": input_data,
        "result": result
    }

    try:
        supabase.table("audit_logs").insert(entry).execute()
    except Exception as e:
        print(f"⚠️ Failed to log audit: {e}. Writing to queue...")
        with open(LOG_QUEUE, "a") as f:
            f.write(json.dumps(entry) + "\n")

def flush_log_queue():
    if not LOG_QUEUE.exists():
        print("📭 No offline logs to sync.")
        return

    with open(LOG_QUEUE, "r") as f:
        lines = f.readlines()

    success, failed = 0, 0
    for line in lines:
        try:
            supabase.table("audit_logs").insert(json.loads(line)).execute()
            success += 1
        except Exception as e:
            print(f"❌ Failed to sync log: {e}")
            failed += 1

    LOG_QUEUE.unlink()
    print(f"✅ Synced {success} logs. ❌ Failed: {failed}")
