import { useAuditLogs } from "@/hooks/useAuditLogs";
import { LogTable } from "@/components/LogTable";

export default function AuditLogsPage() {
  const { logs, loading } = useAuditLogs();

  if (loading) {
    return <div className="p-6">🔄 Loading audit logs...</div>;
  }

  return (
    <div className="p-6">
      <h1 className="text-xl font-semibold mb-4">📘 Audit Logs</h1>
      <LogTable logs={logs} />
    </div>
  );
}
