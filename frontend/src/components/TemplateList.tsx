type Template = {
    name: string;
    created: string;
  };
  
  export function TemplateList({
    templates,
    onSelect
  }: {
    templates: Template[];
    onSelect: (name: string) => void;
  }) {
    return (
      <div className="w-1/3">
        <h2 className="text-lg font-semibold mb-2">📄 Templates</h2>
        <ul className="space-y-2">
          {templates.map((t) => (
            <li
              key={t.name}
              className="cursor-pointer p-2 rounded hover:bg-muted"
              onClick={() => onSelect(t.name)}
            >
              <div className="font-medium">{t.name}</div>
              <div className="text-xs text-muted-foreground">
                Created: {t.created}
              </div>
            </li>
          ))}
        </ul>
      </div>
    );
  }
  