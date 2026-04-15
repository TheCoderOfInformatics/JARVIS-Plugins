# JARVIS Plugin Marketplace

Ein Plugin-Ökosystem für **JARVIS** — den autonomen KI-Assistenten für Windows.

Erweitere JARVIS mit neuen Tools, Integrationen und Fähigkeiten. Verkaufe deine Plugins im Marketplace oder teile sie kostenlos mit der Community.

## 🎯 Was sind JARVIS Plugins?

Plugins erweitern die Fähigkeiten von JARVIS um:
- **Neue Tools** — Datenquellen, APIs, Dienste
- **Smart-Home-Integrationen** — Zigbee, Z-Wave, Tuya, HomeAssistant
- **Enterprise-Systeme** — SAP, Salesforce, Microsoft 365
- **KI-Modelle** — Alternative LLMs, Multimodal-Modelle
- **Benutzerdefinierte Automationen** — Firmenrichtlinien, Workflows

## 📦 Plugin-Struktur

```
mein-plugin/
├── plugin.json              # Plugin-Manifest
├── main.py                  # Hauptimplementierung
├── requirements.txt         # Dependencies
├── README.md               # Dokumentation
├── LICENSE                 # MIT, GPL, etc.
└── tests/
    └── test_plugin.py      # Tests
```

### plugin.json (Manifest)

```json
{
  "name": "mein-awesome-plugin",
  "version": "1.0.0",
  "author": "Dein Name",
  "description": "Kurze Beschreibung was das Plugin tut",
  "category": "productivity|smart-home|security|communication|knowledge",
  "jarvis_min_version": "1.0.0",
  "license": "MIT",
  "repository": "https://github.com/deinuser/jarvis-plugin-mein-awesome",
  "tools": [
    {
      "name": "mein_tool",
      "description": "Was das Tool tut",
      "params": {
        "param1": {"type": "string", "description": "Beschreibung"},
        "param2": {"type": "number", "description": "Beschreibung"}
      }
    }
  ],
  "price": 0,
  "currency": "EUR",
  "tags": ["integration", "automation", "enterprise"]
}
```

## 🚀 Plugin erstellen

### 1. Template klonen

```bash
git clone https://github.com/TheCoderOfInformatics/JARVIS-Plugin-Template.git mein-plugin
cd mein-plugin
```

### 2. Plugin entwickeln

**main.py:**
```python
import json

class MyPlugin:
    """
    Dein JARVIS Plugin
    
    Registriert Tools, die von JARVIS aufgerufen werden können.
    """
    
    def __init__(self, kernel=None):
        """
        Args:
            kernel: JARVIS Kernel-Instanz für API-Zugriff
        """
        self.kernel = kernel
        self.tools = {
            "my_tool": self.my_tool
        }
    
    async def my_tool(self, param1: str, param2: int = 0) -> str:
        """
        Beispiel-Tool
        
        Args:
            param1: Erster Parameter
            param2: Zweiter Parameter
        
        Returns:
            Ergebnis als String
        """
        return f"Verarbeitet: {param1}, {param2}"
    
    def get_tools(self):
        """Gibt verfügbare Tools zurück"""
        return self.tools
```

**requirements.txt:**
```
requests>=2.28.0
python-dotenv>=0.19.0
```

### 3. Testen

```python
# test_plugin.py
import asyncio
from main import MyPlugin

async def test():
    plugin = MyPlugin()
    result = await plugin.my_tool("Test", 42)
    print(result)

asyncio.run(test())
```

### 4. Veröffentlichen

```bash
git add .
git commit -m "Initial plugin release"
git push origin main
```

Dann PR hier im JARVIS-Plugins Repo erstellen.

## 📋 Plugin-Kategorien

| Kategorie | Beschreibung | Beispiele |
|-----------|-------------|----------|
| **productivity** | Produktivität & Zeitmanagement | Notizen, Kalender, Todo-Listen |
| **smart-home** | Smart-Home-Integration | Philips Hue, Zigbee, Home Assistant |
| **security** | Sicherheit & Monitoring | Firewall, Intrusion Detection, VPN |
| **communication** | Kommunikation | Slack, Discord, Telegram Bots |
| **knowledge** | Wissensquellen | News, APIs, Datenbanken |
| **media** | Medien & Unterhaltung | Musik, Streaming, Radio |
| **enterprise** | Business-Systeme | CRM, ERP, Datenbanken |
| **ai** | KI & Modelle | Alternative LLMs, Embeddings |

## 💰 Marketplace

### Plugin kostenlos anbieten

Setze `"price": 0` in `plugin.json`:

```json
{
  "price": 0,
  "currency": "EUR"
}
```

### Plugin verkaufen

1. Setze einen Preis:
   ```json
   {
     "price": 9.99,
     "currency": "EUR"
   }
   ```

2. Lizenzschlüssel implementieren:
   ```python
   def validate_license(key):
       # Validiere Lizenzschlüssel
       return key.startswith("JARVIS-")
   ```

3. PR mit `[PAID]` Tag einreichen

## 🔌 JARVIS Kernel API

Plugins haben Zugriff auf Kernel-Methoden:

```python
class MyPlugin:
    def __init__(self, kernel=None):
        self.kernel = kernel
    
    async def my_tool(self):
        # Neue Tools zur Laufzeit hinzufügen
        await self.kernel.add_tool({"name": "dynamic_tool", ...})
        
        # TTS (Text-to-Speech)
        await self.kernel.speak("Hallo!")
        
        # STT (Kommando ausführen)
        result = await self.kernel.execute_tool("web_search", query="Python")
        
        # Fenster-Benachrichtigungen
        await self.kernel.notify("Titel", "Nachricht")
        
        # Persistente Daten speichern
        await self.kernel.learn({"key": "value"})
```

## 📚 Beispiel-Plugins

Im Ordner `examples/` findest du einsatzbereite Plugins:

- `examples/weather-plugin/` — Erweiterte Wetterfunktionen
- `examples/smart-home-mqtt/` — MQTT Smart-Home-Integration
- `examples/notion-sync/` — Notion Database Synchronisation
- `examples/slack-bot/` — Slack Bot Integration

## 🧪 Testing

```bash
# Unit Tests
python -m pytest tests/

# Plugin Simulator
python -m jarvis.plugin_simulator mein-plugin/

# Integration Test mit JARVIS
python Main.py --load-plugin mein-plugin
```

## 📖 Dokumentation

- [Plugin-Entwicklungshandbuch](./docs/PLUGIN_DEVELOPMENT.md)
- [API-Referenz](./docs/API_REFERENCE.md)
- [Lizenzierung & Verkauf](./docs/LICENSING.md)
- [Best Practices](./docs/BEST_PRACTICES.md)
- [Sicherheit](./docs/SECURITY.md)

## 🤝 Contributing

Plugins beitragen:

1. **Template klonen:**
   ```bash
   git clone https://github.com/TheCoderOfInformatics/JARVIS-Plugin-Template
   ```

2. **Plugin entwickeln** und testen

3. **Pull Request einreichen** mit:
   - Aussagekräftige Beschreibung
   - Tests grün
   - `plugin.json` valide
   - README vollständig

4. **Review** durch Community

5. **Merge** und im Marketplace sichtbar

## ✅ Checkliste vor PR

- [ ] `plugin.json` valide und vollständig
- [ ] `main.py` mit Docstrings
- [ ] `requirements.txt` mit allen Dependencies
- [ ] Tests schreiben und green
- [ ] README mit Beispielen
- [ ] Keine Secrets im Code (.env-Datei verwenden)
- [ ] Python 3.8+ kompatibel
- [ ] Keine Breaking Changes zu JARVIS API

## 🔒 Sicherheit

Plugins können auf Systemressourcen zugreifen. Richtlinien:

1. **Keine permanenten Backdoors** — Plugin wird bei jedem Start neu geladen
2. **Sandbox-Regeln respektieren** — Nicht in Systemdateien schreiben
3. **Benutzer informieren** — Berechtigungen offenlegen
4. **Lizenzschlüssel sicher** — Nicht in Source Code committen

Verdächtige Plugins werden entfernt.

## 📞 Support

- **Fragen?** — GitHub Discussions
- **Bug?** — GitHub Issues
- **Idee?** — GitHub Discussions oder Direct Message

## 📄 Lizenz

Diese Repo: MIT License

Deine Plugins: Deine Wahl (MIT, GPL, Kommerziell, etc.)

## 👥 Community

- [JARVIS Discord](https://discord.gg/jarvis)
- [Beispiel-Plugins](./examples/)
- [Plugin Hall of Fame](./HALL_OF_FAME.md)

---

**Viel Spaß beim Entwickeln! 🚀**
