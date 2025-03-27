Absolutely — here’s a **production-ready `README.md`** for `sentineliam` that covers:

- 🔧 Installation
- 🚀 Usage examples
- 🧱 Architecture
- 🔐 Supabase + PyPI + CLI integration
- 🧪 Testing
- 📦 Versioning + GitHub Actions badge

---

## ✅ `README.md`

```md
# 🔐 SentinelIAM CLI

**SentinelIAM** is a modular, TDD-first CLI for generating, validating, and deploying IAM policy documents. It supports policy templates, Supabase audit logs, and YAML-based validation — fully packaged for PyPI and deployable via GitHub Actions.

![PyPI](https://img.shields.io/pypi/v/sentineliam.svg)
![CI](https://github.com/KatrinaFinney/sentineliam/actions/workflows/publish.yml/badge.svg)

---

## 🚀 Features

- 🔧 `sentinel generate`: Render policy templates with dynamic parameters
- ✅ `sentinel validate`: Validate policy syntax using Pydantic
- 📤 `sentinel push`: Upload policy + audit log to Supabase
- 📥 `sentinel templates`: List + pull shared templates from Supabase
- 📦 Installable via `pip`, versioned with `bump-my-version`
- ☁️ Supabase + Vercel-ready for seamless UI/backend integration

---

## 📦 Installation

### 🔹 From PyPI (production)

```bash
pip install sentineliam
```

### 🔹 From Source (for development)

```bash
git clone https://github.com/KatrinaFinney/sentineliam.git
cd sentineliam
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

---

## 🧪 CLI Usage

### 🧬 Generate Policy from Template

```bash
sentinel generate --template AllowAdmin --params user_id=123
```

### ✅ Validate a Policy File

```bash
sentinel validate policy.yaml
```

### ☁️ Push to Supabase with Audit Logging

```bash
sentinel push policy.yaml
```

### 📂 List & Pull Templates from Supabase

```bash
sentinel templates list
sentinel templates pull
```

---

## 📁 File Layout

```txt
src/
├── cli/              # Typer CLI commands
├── engine/           # Core logic (validate, render, audit)
├── config.py         # Loads Supabase env config
├── templates/        # Local Jinja2 templates
├── supabase_client/  # Supabase client integration
tests/                # Pytest test suite
```

---

## 🔐 Supabase Integration

Create a `.env` file:

```env
SUPABASE_URL=https://xyz.supabase.co
SUPABASE_KEY=your-service-role-key
```

Use [Supabase SQL Editor](https://app.supabase.com/project/_/sql) to create:

- `policy_templates` table (for Jinja templates)
- `audit_logs` table (for CLI audit trail)
- RLS policies to restrict access to user-specific data

---

## 🧱 Policy Schema

SentinelIAM uses multi-statement, AWS-style YAML:

```yaml
version: "2025-03-26"
statement:
  - effect: "allow"
    action: ["read", "write"]
    resource: "db.users"
```

---

## 🧪 Testing

Run all tests:

```bash
pytest
```

---

## 📦 Versioning & Release

Use the included `bump_version.sh`:

```bash
./bump_version.sh patch   # or minor / major
git push && git push --tags
```

> Triggers GitHub Action to auto-publish to PyPI

---

## 🛠 GitHub Action

Auto-publish on tags like `v0.1.1` via `.github/workflows/publish.yml`. Add your PyPI token under:

```
Settings → Secrets → PYPI_API_TOKEN
```

---

## 🙌 Contributors

Built with ❤️ by [Katrina Finney](https://github.com/KatrinaFinney)  
CLI system design & infra assisted by Patch (AI dev assistant)

---

## 🪄 Roadmap

- [ ] Web UI template editor (Next.js)
- [ ] Supabase OAuth CLI login
- [ ] Template validation rules
- [ ] Sentinel Sync CLI for offline logs

---

## 📜 License

MIT License © Katrina Finney
```

---

