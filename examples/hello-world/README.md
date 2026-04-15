# Hello World Plugin für JARVIS

Ein einfaches Einsteiger-Plugin, das grundlegende Plugin-Funktionalität demonstriert.

## Installation

```bash
cd examples/hello-world
pip install -r requirements.txt
```

## Verwendung

### Mit JARVIS laden

```bash
python Main.py --load-plugin examples/hello-world
```

Dann JARVIS fragen:

> "Hey Jarvis, führe hello_world('Alice') aus"
> "Zähle bis 10"

### Direktes Testen

```python
import asyncio
from main import HelloWorldPlugin

async def test():
    plugin = HelloWorldPlugin()
    
    # Test 1
    result1 = await plugin.hello_world("Python")
    print(result1)
    
    # Test 2
    result2 = await plugin.count_to_n(5)
    print(result2)

asyncio.run(test())
```

Oder:

```bash
python main.py
```

## Tools

### `hello_world`

Grüße die Welt

**Parameter:**
- `name` (string, optional): Name zum Grüßen (default: "World")

**Beispiel:**
```
hello_world("Alice")
→ "Hello, Alice! This is Hello World Plugin speaking. 👋"
```

### `count_to_n`

Zähle von 1 bis N

**Parameter:**
- `n` (number, optional): Zähle bis zu dieser Zahl (default: 5, max: 100)

**Beispiel:**
```
count_to_n(3)
→ {
    "count": [1, 2, 3],
    "total": 3,
    "sum": 6
  }
```

## Tests ausführen

```bash
pytest tests/ -v
```

## Fehlerbehandlung

Das Plugin validiert Input-Parameter:
- `count_to_n` akzeptiert nur Werte zwischen 1-100
- Andere ungültige Input wird mit `success: false` beantwortet

## Lizenz

MIT
