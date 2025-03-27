import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabaseClient";

export function useAuditLogs() {
  const [logs, setLogs] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchLogs() {
      const { data, error } = await supabase
        .from("audit_logs")
        .select("timestamp, action, user_id");

      if (error) {
        console.error("Failed to fetch audit logs:", error.message);
      } else {
        setLogs(data);
      }

      setLoading(false);
    }

    fetchLogs();
  }, []);

  return { logs, loading };
}
