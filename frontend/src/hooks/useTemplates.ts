import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabaseClient";

export function useTemplates() {
  const [templates, setTemplates] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchTemplates() {
      const { data, error } = await supabase
        .from("policy_templates")
        .select("id, name, description, template, created_at");

      if (error) {
        console.error("Failed to fetch templates:", error.message);
      } else {
        setTemplates(data);
      }

      setLoading(false);
    }

    fetchTemplates();
  }, []);

  return { templates, loading };
}
