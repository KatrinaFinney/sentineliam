import { LogTable } from "@/components/LogTable";
import { mockLogs } from "@/data/mockLogs";

export default function AuditLogsPage() {
  return (
    <div className="p-6">
      <h1 className="text-xl font-semibold mb-4">📘 Audit Logs</h1>
      <LogTable logs={mockLogs} />
    </div>
  );
}
