import json
from engine.audit import push_audit, flush_log_queue
from pathlib import Path
import uuid

def test_push_audit_offline(monkeypatch):
    # Simulate Supabase failure
    monkeypatch.setattr("supabase_client.client.supabase.table", lambda *a, **kw: (_ for _ in ()).throw(Exception("Simulated failure")))

    test_action = "test_action"
    test_input = {"param": "value"}
    test_result = {"status": "ok"}

    push_audit(test_action, test_input, test_result)

    queue_path = Path(".sentinel/logs/queue.json")
    assert queue_path.exists()
    with open(queue_path) as f:
        lines = f.readlines()
        assert any(test_action in line for line in lines)

def test_flush_log_queue(monkeypatch):
    # Simulate working Supabase
    class FakeTable:
        def insert(self, val):
            return self
        def execute(self):
            return True

    monkeypatch.setattr("supabase_client.client.supabase.table", lambda *a, **kw: FakeTable())

    # Add dummy log
    queue_path = Path(".sentinel/logs/queue.json")
    queue_path.parent.mkdir(parents=True, exist_ok=True)
    dummy = json.dumps({"action": "flush-test", "timestamp": "now"})
    with open(queue_path, "w") as f:
        f.write(dummy + "\n")

    flush_log_queue()
    assert not queue_path.exists()