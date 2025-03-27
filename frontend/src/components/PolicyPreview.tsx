import { Card, CardContent } from "@/components/ui/card";

export function PolicyPreview({ template }: { template: any }) {
  return (
    <Card className="w-2/3">
      <CardContent className="p-4">
        <div className="flex justify-between items-center mb-2">
          <h3 className="font-semibold text-lg">{template.name}</h3>
          <button
            className="text-sm text-blue-500"
            onClick={() => navigator.clipboard.writeText(template.policy)}
          >
            Copy
          </button>
        </div>
        <pre className="bg-gray-800 text-white p-4 rounded text-xs overflow-x-auto">
          {template.policy}
        </pre>
      </CardContent>
    </Card>
  );
}
