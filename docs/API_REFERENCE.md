# JARVIS Plugin API-Referenz

## Kernel-Methoden (für Plugins verfügbar)

### async `speak(text: str) -> None`

Lasse JARVIS etwas sagen.

```python
await self.kernel.speak("Hallo, das ist eine Testnachricht")
```

### async `notify(title: str, message: str) -> None`

Zeige Windows-Benachrichtigung.

```python
await self.kernel.notify("Plugin Status", "Aktion abgeschlossen")
```

### async `execute_tool(tool_name: str, **kwargs) -> Any`

Führe anderes Tool aus.

```python
weather = await self.kernel.execute_tool("get_weather", location="Berlin")
```

### async `learn(data: Dict) -> None`

Speichere Daten persistent (in `data/learnings.json`).

```python
await self.kernel.learn({
    "user_preference": "dark_mode",
    "saved_at": "2025-04-15"
})
```

### async `add_tool(tool_definition: Dict) -> None`

Füge dynamisch ein neues Tool hinzu.

```python
await self.kernel.add_tool({
    "name": "my_dynamic_tool",
    "description": "Ein Tool das zur Laufzeit erstellt wurde",
    "func": my_async_function
})
```

### async `get_system_info() -> Dict`

Hole Systeminformationen.

```python
info = await self.kernel.get_system_info()
# Returns: {"cpu": 45.2, "ram": 8192, "disk": 500, ...}
```

### async `search_web(query: str) -> List[Dict]`

Führe Websuche durch.

```python
results = await self.kernel.search_web("Python asyncio")
# Returns: [{"title": "...", "url": "...", "snippet": "..."}, ...]
```

### async `send_email(to: str, subject: str, body: str) -> bool`

Versende E-Mail.

```python
success = await self.kernel.send_email(
    to="user@example.com",
    subject="Plugin Notification",
    body="Hier ist eine Nachricht vom Plugin"
)
```

## Plugin-Struktur

### `__init__(kernel=None)`

Initialisiere Plugin.

**Parameter:**
- `kernel` (Kernel, optional): Kernel-Instanz für API-Zugriff

**Beispiel:**
```python
def __init__(self, kernel=None):
    self.kernel = kernel
    self.tools = {
        "my_tool": self.my_tool
    }
```

### `get_tools() -> Dict[str, callable]`

Gebe Tools zurück.

**Returns:**
- Dictionary mit Tool-Namen und Funktionen

**Beispiel:**
```python
def get_tools(self):
    return self.tools
```

### `async on_enable()`

Optional: Wird aufgerufen, wenn Plugin aktiviert wird.

```python
async def on_enable(self):
    print("Plugin enabled!")
    if self.kernel:
        await self.kernel.notify("Status", "Plugin enabled")
```

### `async on_disable()`

Optional: Wird aufgerufen, wenn Plugin deaktiviert wird.

```python
async def on_disable(self):
    print("Plugin disabled!")
```

### `async on_config(config: Dict)`

Optional: Wird aufgerufen wenn Konfiguration geändert wird.

```python
async def on_config(self, config: Dict):
    self.api_key = config.get("api_key")
```

## Tool-Signatur

Tools müssen async-Funktionen sein mit type hints:

```python
async def my_tool(self, param1: str, param2: int = 0) -> Dict[str, Any]:
    """
    Docstring wird von JARVIS als Tool-Beschreibung verwendet
    
    Args:
        param1: String Parameter
        param2: Optional Integer (default: 0)
    
    Returns:
        Dict mit Ergebnis
    """
    return {"success": True, "result": f"{param1} {param2}"}
```

## Plugin.json vollständiges Schema

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "author": "Author Name <email@example.com>",
  "description": "Short description",
  "longDescription": "Longer description (optional)",
  "category": "productivity|smart-home|security|communication|knowledge|media|enterprise|ai",
  "jarvis_min_version": "1.0.0",
  "jarvis_max_version": "2.0.0",
  "license": "MIT|GPL|Kommerziell",
  "repository": "https://github.com/user/plugin-repo",
  "homepage": "https://example.com",
  "documentation": "https://docs.example.com",
  "issues": "https://github.com/user/plugin-repo/issues",
  "price": 0,
  "currency": "EUR",
  "demo_video": "https://youtu.be/...",
  "tags": ["tag1", "tag2"],
  "keywords": ["keyword1", "keyword2"],
  "screenshots": ["https://url1.png", "https://url2.png"],
  "tools": [
    {
      "name": "tool_name",
      "description": "What the tool does",
      "category": "action|query|utility",
      "params": {
        "param1": {
          "type": "string|number|boolean|array|object",
          "description": "Parameter description",
          "required": true,
          "default": "default_value",
          "enum": ["option1", "option2"],
          "minimum": 0,
          "maximum": 100
        }
      },
      "returns": {
        "type": "object",
        "description": "What the tool returns"
      }
    }
  ],
  "permissions": [
    "read_user_files",
    "write_user_files",
    "network_access",
    "persistent_storage",
    "execute_commands",
    "modify_system"
  ],
  "requires_api_keys": [
    {
      "service": "Service Name",
      "env_var": "SERVICE_API_KEY",
      "docs": "https://docs.example.com"
    }
  ],
  "dependencies": {
    "package-name": ">=1.0.0"
  },
  "support_email": "support@example.com",
  "funding": "https://buymeacoffee.com/user",
  "funding_url": "https://patreon.com/user"
}
```

## Error Handling Best Practices

```python
async def my_tool(self, param1: str) -> Dict[str, Any]:
    try:
        # Validate input
        if not param1:
            raise ValueError("param1 is required")
        
        # Perform action
        result = await self._do_something(param1)
        
        return {
            "success": True,
            "result": result
        }
    
    except ValueError as e:
        # Expected error
        return {
            "success": False,
            "error": str(e),
            "error_type": "validation"
        }
    
    except ConnectionError as e:
        # Network error
        return {
            "success": False,
            "error": str(e),
            "error_type": "network",
            "retry_after": 60
        }
    
    except Exception as e:
        # Unexpected error
        return {
            "success": False,
            "error": "An unexpected error occurred",
            "details": str(e)
        }
```

## Logging

```python
import logging

logger = logging.getLogger("my-plugin")

class MyPlugin:
    async def my_tool(self):
        logger.debug("Starting my_tool")
        logger.info(f"Processing parameter")
        logger.warning("This might be slow")
        logger.error("Something failed")
```

## Async/Await Pattern

Alle Tools müssen async sein:

```python
# ✅ CORRECT
async def my_tool(self, param: str) -> Dict:
    result = await some_async_function()
    return result

# ❌ WRONG
def my_tool(self, param: str) -> Dict:
    result = some_function()
    return result
```

## Type Hints

Verwende type hints für bessere IDE-Unterstützung:

```python
from typing import Dict, List, Any, Optional

async def my_tool(
    self,
    query: str,
    limit: Optional[int] = None
) -> Dict[str, Any]:
    items: List[Dict] = []
    return {"items": items}
```

---

**Benötigst du Hilfe?** Schau in die [Beispiele](./examples/) oder öffne ein Issue!
