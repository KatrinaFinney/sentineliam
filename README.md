# 🛡 SentinelIAM Monorepo

Policy-based access control tools for modern cloud teams — includes:

- 🧱 `backend/` — Python CLI to generate, validate, and push policies to Supabase
- 🌐 `frontend/` — React UI to browse audit logs and templates

---

## 🚀 Quick Start

### 🧪 CLI (Python)
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
sentinel --help
🌐 Frontend (Next.js)
bash
Copy
Edit
cd frontend
cp .env.local.example .env.local
npm install
npm run dev
📦 Project Structure
bash
Copy
Edit
sentineliam/
├── backend/      # CLI tool, published to PyPI
├── frontend/     # React UI, deployed via Vercel
└── README.md     # This file
🧪 Test Coverage
CLI: pytest --cov=src

Web UI: Coming soon via Playwright or Cypress

🔗 Links
CLI Package: PyPI

Supabase Project: Dashboard

yaml
Copy
Edit
