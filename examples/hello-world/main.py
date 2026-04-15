"""
Hello World Plugin für JARVIS

Ein einfaches Einsteiger-Plugin, das grundlegende Plugin-Funktionalität demonstriert.
"""

import asyncio
from typing import Dict, Any


class HelloWorldPlugin:
    """
    Ein minimales Beispiel-Plugin für JARVIS

    Demonstriert:
    - Plugin-Struktur
    - Tool-Registrierung
    - Async-Funktionen
    - JARVIS Kernel Integration
    """

    def __init__(self, kernel=None):
        """
        Plugin-Initialisierung

        Args:
            kernel: JARVIS Kernel-Instanz (optional)
        """
        self.kernel = kernel
        self.call_count = 0
        self.tools = {
            "hello_world": self.hello_world,
            "count_to_n": self.count_to_n,
        }

    async def hello_world(self, name: str = "World") -> Dict[str, Any]:
        """
        Grüße die Welt

        Args:
            name: Name zum Grüßen (default: "World")

        Returns:
            Dict mit Greeting und Statistiken
        """
        self.call_count += 1

        greeting = f"Hello, {name}! This is Hello World Plugin speaking. 👋"

        # Optional: Benachrichtigung über JARVIS senden
        if self.kernel:
            try:
                await self.kernel.notify("Hello World", f"Greeted {name}")
            except Exception as e:
                print(f"Notification failed: {e}")

        return {
            "success": True,
            "message": greeting,
            "call_count": self.call_count,
            "timestamp": __import__("datetime").datetime.now().isoformat()
        }

    async def count_to_n(self, n: int = 5) -> Dict[str, Any]:
        """
        Zähle von 1 bis N

        Args:
            n: Zähle bis zu dieser Zahl (default: 5)

        Returns:
            Dict mit Zählergebnis
        """
        if n < 1:
            return {
                "success": False,
                "error": "n muss >= 1 sein",
                "value": n
            }

        if n > 100:
            return {
                "success": False,
                "error": "n darf nicht größer als 100 sein",
                "value": n
            }

        count = list(range(1, n + 1))

        return {
            "success": True,
            "count": count,
            "total": len(count),
            "sum": sum(count)
        }

    def get_tools(self) -> Dict[str, callable]:
        """
        Gebe alle Tools dieses Plugins zurück

        Returns:
            Dictionary mit Tool-Namen als Keys und Funktionen als Values
        """
        return self.tools

    async def on_enable(self):
        """Wird aufgerufen, wenn Plugin aktiviert wird"""
        print("[HelloWorldPlugin] Enabled!")
        if self.kernel:
            await self.kernel.notify("Plugin Status", "Hello World Plugin activated")

    async def on_disable(self):
        """Wird aufgerufen, wenn Plugin deaktiviert wird"""
        print("[HelloWorldPlugin] Disabled!")


# Für direktedes Testen
if __name__ == "__main__":
    async def main():
        plugin = HelloWorldPlugin()

        # Test 1: hello_world
        result1 = await plugin.hello_world("Python")
        print("Test 1 - hello_world:")
        print(result1)
        print()

        # Test 2: count_to_n
        result2 = await plugin.count_to_n(10)
        print("Test 2 - count_to_n:")
        print(result2)
        print()

        # Test 3: another hello_world (call_count sollte inkrementieren)
        result3 = await plugin.hello_world("JARVIS")
        print("Test 3 - hello_world (again):")
        print(result3)

    asyncio.run(main())
