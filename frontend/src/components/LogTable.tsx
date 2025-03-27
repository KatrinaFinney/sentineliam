import { Card, CardContent } from "@/components/ui/card";

export type LogEntry = {
  timestamp: string;
  action: string;
  user: string;
  status: "success" | "fail" | "warn";
};

export function LogTable({ logs }: { logs: LogEntry[] }) {
  return (
    <Card className="w-full">
      <CardContent className="overflow-x-auto p-4">
        <table className="w-full text-sm">
          <thead>
            <tr className="text-left border-b">
              <th className="pr-4">Timestamp</th>
              <th className="pr-4">Action</th>
              <th className="pr-4">User</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((log, i) => (
              <tr key={i} className="border-t">
                <td className="pr-4">{log.timestamp}</td>
                <td className="pr-4">{log.action}</td>
                <td className="pr-4">{log.user}</td>
                <td>
                  {log.status === "success" && "✅"}
                  {log.status === "fail" && "❌"}
                  {log.status === "warn" && "⚠️"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </CardContent>
    </Card>
  );
}
