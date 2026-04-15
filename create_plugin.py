"""
Script zum Generieren eines neuen Plugin-Templates
"""

import os
import json
import sys

TEMPLATE = {
    "plugin.json": {
        "name": "my-plugin",
        "version": "1.0.0",
        "author": "Your Name <email@example.com>",
        "description": "A brief description of what your plugin does",
        "category": "productivity",
        "jarvis_min_version": "1.0.0",
        "license": "MIT",
        "repository": "https://github.com/youruser/jarvis-plugin-my-plugin",
        "price": 0,
        "currency": "EUR",
        "tags": ["tag1", "tag2"],
        "tools": [
            {
                "name": "my_tool",
                "description": "What this tool does",
                "params": {
                    "param1": {
                        "type": "string",
                        "description": "Description of parameter"
                    }
                }
            }
        ]
    },
    "requirements.txt": """requests>=2.28.0
""",
    "README.md": """# My Plugin

Description here.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
import asyncio
from main import MyPlugin

async def test():
    plugin = MyPlugin()
    result = await plugin.my_tool("test")
    print(result)

asyncio.run(test())
```

## Tools

### my_tool

Description of my_tool.

**Parameters:**
- `param1` (string): Description

**Example:**
```
my_tool("value")
```

## License

MIT
""",
    "main.py": '''"""
My Plugin for JARVIS
"""

import asyncio
from typing import Dict, Any


class MyPlugin:
    """
    My JARVIS Plugin
    """

    def __init__(self, kernel=None):
        """
        Plugin initialization

        Args:
            kernel: JARVIS Kernel instance (optional)
        """
        self.kernel = kernel
        self.tools = {
            "my_tool": self.my_tool,
        }

    async def my_tool(self, param1: str) -> Dict[str, Any]:
        """
        Description of my_tool

        Args:
            param1: Description

        Returns:
            Result dictionary
        """
        return {
            "success": True,
            "message": f"Processed: {param1}"
        }

    def get_tools(self) -> Dict[str, callable]:
        """Return all tools of this plugin"""
        return self.tools


# For direct testing
if __name__ == "__main__":
    async def main():
        plugin = MyPlugin()
        result = await plugin.my_tool("test")
        print(result)

    asyncio.run(main())
''',
    ".gitignore": """# Environment
.env
.env.local

# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp

# Testing
.pytest_cache/
.coverage

# Logs
*.log
"""
}


def create_plugin_template(plugin_name: str):
    """Create a new plugin template directory"""

    # Validate plugin name
    if not plugin_name:
        print("Error: Plugin name required")
        sys.exit(1)

    if not plugin_name.replace("-", "").replace("_", "").isalnum():
        print("Error: Invalid plugin name. Use alphanumeric characters, hyphens, or underscores")
        sys.exit(1)

    # Create directory
    os.makedirs(plugin_name, exist_ok=True)
    os.makedirs(os.path.join(plugin_name, "tests"), exist_ok=True)

    # Create files
    print(f"Creating plugin template: {plugin_name}")

    # plugin.json
    manifest = TEMPLATE["plugin.json"].copy()
    manifest["name"] = plugin_name
    with open(os.path.join(plugin_name, "plugin.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"✓ plugin.json")

    # requirements.txt
    with open(os.path.join(plugin_name, "requirements.txt"), "w") as f:
        f.write(TEMPLATE["requirements.txt"])
    print(f"✓ requirements.txt")

    # README.md
    with open(os.path.join(plugin_name, "README.md"), "w") as f:
        f.write(TEMPLATE["README.md"])
    print(f"✓ README.md")

    # main.py
    with open(os.path.join(plugin_name, "main.py"), "w") as f:
        f.write(TEMPLATE["main.py"])
    print(f"✓ main.py")

    # test_plugin.py
    with open(os.path.join(plugin_name, "tests", "test_plugin.py"), "w") as f:
        f.write("""import pytest
import asyncio
from main import MyPlugin


@pytest.mark.asyncio
async def test_my_tool():
    plugin = MyPlugin()
    result = await plugin.my_tool("test")
    assert result["success"] is True
""")
    print(f"✓ tests/test_plugin.py")

    # .gitignore
    with open(os.path.join(plugin_name, ".gitignore"), "w") as f:
        f.write(TEMPLATE[".gitignore"])
    print(f"✓ .gitignore")

    print(f"\\n✅ Plugin template '{plugin_name}' created successfully!")
    print(f"\\nNext steps:")
    print(f"  cd {plugin_name}")
    print(f"  Edit plugin.json with your plugin details")
    print(f"  Edit main.py with your tool implementation")
    print(f"  Run tests: pytest tests/ -v")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_plugin.py <plugin-name>")
        print("Example: python create_plugin.py my-awesome-plugin")
        sys.exit(1)

    plugin_name = sys.argv[1]
    create_plugin_template(plugin_name)
