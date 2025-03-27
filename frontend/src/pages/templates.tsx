import { useState } from "react";
import { TemplateList } from "@/components/TemplateList";
import { PolicyPreview } from "@/components/PolicyPreview";
import { mockTemplates } from "@/data/mockTemplates";

export default function PolicyTemplatesPage() {
  const [selected, setSelected] = useState<string | null>(null);
  const activeTemplate = mockTemplates.find(t => t.name === selected);

  return (
    <div className="flex p-6 space-x-4">
      <TemplateList templates={mockTemplates} onSelect={setSelected} />
      {selected && activeTemplate && (
        <PolicyPreview template={activeTemplate} />
      )}
    </div>
  );
}
