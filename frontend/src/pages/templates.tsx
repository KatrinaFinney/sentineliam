import { useState } from "react";
import { TemplateList } from "@/components/TemplateList";
import { PolicyPreview } from "@/components/PolicyPreview";
import { useTemplates } from "@/hooks/useTemplates";

export default function PolicyTemplatesPage() {
  const [selected, setSelected] = useState<string | null>(null);
  const { templates, loading } = useTemplates();

  const activeTemplate = templates.find(t => t.name === selected);

  if (loading) {
    return <div className="p-6">🔄 Loading templates...</div>;
  }

  return (
    <div className="flex p-6 space-x-4">
      <TemplateList templates={templates} onSelect={setSelected} />
      {selected && activeTemplate && (
        <PolicyPreview template={activeTemplate} />
      )}
    </div>
  );
}
