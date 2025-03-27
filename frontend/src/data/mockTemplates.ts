export const mockTemplates = [
    {
      name: "readonly-template",
      created: "2025-03-25",
      policy: JSON.stringify({ effect: "allow", action: "read:*" }, null, 2)
    },
    {
      name: "admin-elevated",
      created: "2025-03-20",
      policy: JSON.stringify({ effect: "allow", action: "*" }, null, 2)
    }
  ];
  