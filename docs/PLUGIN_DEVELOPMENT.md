# Plugin-Entwicklungshandbuch

## Die 5 Stufen der Plugin-Entwicklung

### 1. Ideation

Überlege: Welches Problem soll das Plugin lösen?

```
Problem: "Mein Team verwendet 5 verschiedene Notiz-Apps"
Lösung: "Ein JARVIS-Plugin, das alle Notizen synchronisiert"
Nutzer: "Small Business Nutzer, Startups"
```

### 2. Prototyping

Entwickle das Basis-Plugin:

```python
# main.py - Minimalistisch starten
import json
import requests

class NoteSyncPlugin:
    def __init__(self, kernel=None):
        self.kernel = kernel
        self.tools = {
            "sync_notes": self.sync_notes,
            "search_notes": self.search_notes
        }
    
    async def sync_notes(self, source: str, destination: str):
        """Synchronisiere Notizen zwischen Systemen"""
        return f"Syncing {source} → {destination}"
    
    async def search_notes(self, query: str):
        """Suche in allen Notizen"""
        return [{"title": "Found", "content": query}]
    
    def get_tools(self):
        return self.tools
```

### 3. Testing

```python
# tests/test_plugin.py
import pytest
from main import NoteSyncPlugin

@pytest.mark.asyncio
async def test_sync_notes():
    plugin = NoteSyncPlugin()
    result = await plugin.sync_notes("notion", "obsidian")
    assert "Syncing" in result

@pytest.mark.asyncio
async def test_search_notes():
    plugin = NoteSyncPlugin()
    results = await plugin.search_notes("python")
    assert len(results) > 0

# Ausführen:
# pytest tests/ -v
```

### 4. Publishing

Veröffentliche auf GitHub:

```bash
git init
git add .
git commit -m "Initial NoteSyncPlugin release"
git remote add origin https://github.com/youruser/jarvis-plugin-notesync
git push -u origin main

# Tag erstellen
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
```

### 5. Marketing

Mache dein Plugin bekannt:

- Reddit: r/JARVIS-AI
- Twitter/X: #JARVISPlugin
- Product Hunt
- Hacker News

## Plugin-Struktur (Best Practice)

```
jarvis-plugin-notesync/
├── .github/
│   └── workflows/
│       └── tests.yml          # CI/CD Pipeline
├── docs/
│   ├── USAGE.md              # Nutzerhandbuch
│   └── API.md                # Tool-API
├── src/
│   ├── __init__.py
│   └── main.py               # Hauptimplementierung
├── tests/
│   ├── __init__.py
│   ├── test_sync.py
│   └── test_search.py
├── examples/
│   └── basic_usage.py        # Beispiel
├── .gitignore
├── .env.example              # Template für Secrets
├── plugin.json               # Manifest
├── requirements.txt          # Dependencies
├── LICENSE                   # MIT/GPL/Kommerziell
└── README.md                 # Dokumentation
```

## plugin.json - Vollständiges Beispiel

```json
{
  "name": "notesync",
  "version": "1.0.0",
  "author": "Dein Name <email@example.com>",
  "description": "Synchronisiere Notizen zwischen Notion, Obsidian, OneNote und Evernote",
  "longDescription": "Ein vollständiges Notiz-Synchronisations-System mit Konflikt-Lösung, Tagging und Echtzeit-Updates",
  "category": "productivity",
  "jarvis_min_version": "1.0.0",
  "license": "MIT",
  "repository": "https://github.com/youruser/jarvis-plugin-notesync",
  "homepage": "https://youruser.github.io/jarvis-plugin-notesync",
  "documentation": "https://github.com/youruser/jarvis-plugin-notesync/wiki",
  "issues": "https://github.com/youruser/jarvis-plugin-notesync/issues",
  "price": 4.99,
  "currency": "EUR",
  "demo_video": "https://youtu.be/...",
  "tags": ["productivity", "synchronization", "notes", "crossplatform"],
  "keywords": ["notion", "obsidian", "onenote", "evernote", "sync"],
  "screenshots": [
    "https://cdn.example.com/screenshot1.png",
    "https://cdn.example.com/screenshot2.png"
  ],
  "tools": [
    {
      "name": "sync_notes",
      "description": "Synchronisiere Notizen zwischen Plattformen",
      "category": "action",
      "params": {
        "source": {
          "type": "string",
          "description": "Quellplattform: notion|obsidian|onenote|evernote",
          "enum": ["notion", "obsidian", "onenote", "evernote"]
        },
        "destination": {
          "type": "string",
          "description": "Zielplattform",
          "enum": ["notion", "obsidian", "onenote", "evernote"]
        },
        "filters": {
          "type": "object",
          "description": "Filter (optional)",
          "properties": {
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_after": {"type": "string", "format": "date"}
          }
        }
      },
      "returns": {"type": "object", "description": "Sync-Resultat mit Statistiken"}
    },
    {
      "name": "search_notes",
      "description": "Suche in allen verbundenen Notiz-Systemen",
      "category": "query",
      "params": {
        "query": {"type": "string", "description": "Suchbegriff"},
        "limit": {"type": "number", "description": "Maximale Ergebnisse (default: 10)"}
      }
    }
  ],
  "permissions": [
    "read_user_files",
    "network_access",
    "persistent_storage"
  ],
  "dependencies": {
    "notion-client": ">=2.0.0",
    "obsidian-api": ">=1.0.0",
    "microsoft-graph": ">=4.0.0"
  },
  "requires_api_keys": [
    {
      "service": "Notion",
      "env_var": "NOTION_API_KEY",
      "docs": "https://developers.notion.com"
    },
    {
      "service": "Obsidian",
      "env_var": "OBSIDIAN_VAULT_PATH"
    }
  ],
  "screenshots_count": 2,
  "ratings": 4.8,
  "downloads": 1240,
  "last_updated": "2025-04-15T10:30:00Z",
  "support_email": "support@example.com",
  "funding": "https://buymeacoffee.com/youruser"
}
```

## Requirements.txt Standards

```
# Core
requests>=2.28.0
aiohttp>=3.8.0

# Integrationen
notion-client>=2.0.0
obsidian-sync>=1.0.0

# Utilities
python-dateutil>=2.8.2
pydantic>=2.0.0

# Development (optional)
pytest>=7.0.0
pytest-asyncio>=0.20.0
black>=23.0.0
flake8>=5.0.0
```

## Umgang mit API-Keys

### ❌ FALSCH - Secrets im Code

```python
# NIEMALS!
API_KEY = "sk-1234567890abcdef"
client = NotionClient(api_key=API_KEY)
```

### ✅ RICHTIG - Environment Variables

```python
# main.py
import os
from dotenv import load_dotenv

load_dotenv()

class MyPlugin:
    def __init__(self, kernel=None):
        self.api_key = os.getenv("NOTION_API_KEY")
        if not self.api_key:
            raise ValueError("NOTION_API_KEY nicht gesetzt!")
```

### .env.example Template

```
# Notion Integration
NOTION_API_KEY=sk_...
NOTION_WORKSPACE_ID=...

# Obsidian
OBSIDIAN_VAULT_PATH=/Users/username/vault

# Optional
DEBUG=false
LOG_LEVEL=INFO
```

## Error Handling

```python
class MyPlugin:
    async def sync_notes(self, source: str, dest: str):
        try:
            # Validiere Input
            if source not in ["notion", "obsidian"]:
                raise ValueError(f"Unknown source: {source}")
            
            # Führe Aktion aus
            result = await self._do_sync(source, dest)
            
            return {
                "success": True,
                "synced_count": result.count,
                "message": f"Synced {result.count} notes"
            }
        
        except ConnectionError as e:
            # Netzwerkfehler
            return {
                "success": False,
                "error": f"Connection failed: {str(e)}",
                "retry_after": 60  # Sekunden
            }
        
        except Exception as e:
            # Unerwarteter Fehler
            if self.kernel:
                await self.kernel.notify("Error", f"Sync failed: {e}")
            
            return {
                "success": False,
                "error": str(e)
            }
```

## Logging

```python
import logging

logger = logging.getLogger("notesync-plugin")

class MyPlugin:
    async def sync_notes(self, source, dest):
        logger.info(f"Starting sync: {source} → {dest}")
        
        try:
            result = await self._sync()
            logger.info(f"Sync completed: {result.count} items")
        except Exception as e:
            logger.error(f"Sync failed: {e}", exc_info=True)
            raise
```

## CI/CD mit GitHub Actions

```.github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11']
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-asyncio black flake8
    
    - name: Lint
      run: |
        black --check .
        flake8 . --count --select=E9,F63,F7,F82
    
    - name: Tests
      run: pytest tests/ -v
```

---

**Benötigst du Hilfe?** Eröffne ein Issue in diesem Repo!
