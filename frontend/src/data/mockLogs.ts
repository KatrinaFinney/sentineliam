import type { LogEntry } from "@/components/LogTable";

export const mockLogs: LogEntry[] = [
  {
    timestamp: "2025-03-25T15:23:00Z",
    action: "generate",
    user: "user_123",
    status: "success"
  },
  {
    timestamp: "2025-03-25T16:01:42Z",
    action: "validate",
    user: "user_123",
    status: "fail"
  },
  {
    timestamp: "2025-03-25T17:45:18Z",
    action: "push",
    user: "user_456",
    status: "warn"
  }
];
