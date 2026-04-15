"""
GitHub Marketplace Action Template Generator

Generates a complete, marketplace-ready GitHub Action template.
Usage:
    python create_marketplace_action.py my-awesome-action
"""

import os
import sys
import json

def create_action(action_name: str, author: str = "Your Name"):
    """Generate a complete GitHub Marketplace action template"""

    # Validate name
    if not action_name or not action_name.replace("-", "").isalnum():
        print("❌ Error: Invalid action name. Use alphanumeric and hyphens only.")
        sys.exit(1)

    # Create directories
    os.makedirs(f"{action_name}/.github/workflows", exist_ok=True)

    print(f"📦 Creating GitHub Marketplace action: {action_name}")

    # 1. action.yml
    action_yml = f"""name: '{action_name.title()}'
author: '{author}'
description: 'Description of what your action does'
branding:
  icon: 'check-circle'
  color: 'purple'

inputs:
  param1:
    description: 'Input parameter description'
    required: false
    default: '0'

outputs:
  result:
    description: 'Output result'

runs:
  using: 'composite'
  steps:
    - run: echo "Action: {action_name}"
      shell: bash
"""

    with open(f"{action_name}/action.yml", "w") as f:
        f.write(action_yml)
    print("✓ action.yml")

    # 2. README.md
    readme = f"""# {action_name.title()}

One-liner description of your action.

## Features

- Feature 1
- Feature 2
- Feature 3

## Usage

```yaml
- uses: username/repo/{action_name}@v1
  with:
    param1: value
```

## Inputs

### param1

Description here.

**Required**: false
**Default**: `0`

## Outputs

### result

Output description here.

## Examples

### Basic Example

```yaml
- uses: username/repo/{action_name}@v1
```

### With Parameters

```yaml
- uses: username/repo/{action_name}@v1
  with:
    param1: custom-value
```

## Support

- 📝 [Issues](https://github.com/username/repo/issues)
- 💬 [Discussions](https://github.com/username/repo/discussions)

## License

MIT - see LICENSE file
"""

    with open(f"{action_name}/README.md", "w") as f:
        f.write(readme)
    print("✓ README.md")

    # 3. CHANGELOG.md
    changelog = f"""# Changelog

## [1.0.0] - 2025-04-15

### Added
- Initial release of {action_name}
- [List your features]

### Fixed
- [List any initial fixes]
"""

    with open(f"{action_name}/CHANGELOG.md", "w") as f:
        f.write(changelog)
    print("✓ CHANGELOG.md")

    # 4. LICENSE
    license_text = """MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.
"""

    with open(f"{action_name}/LICENSE", "w") as f:
        f.write(license_text)
    print("✓ LICENSE")

    # 5. icon.svg
    icon_svg = """<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <!-- Purple background -->
  <rect width="200" height="200" fill="#6f42c1" rx="30"/>

  <!-- Your icon here -->
  <circle cx="100" cy="100" r="60" fill="white" opacity="0.2"/>
  <circle cx="100" cy="100" r="50" fill="none" stroke="white" stroke-width="2"/>
  <text x="100" y="115" font-size="60" font-weight="bold" fill="white" text-anchor="middle">→</text>
</svg>
"""

    with open(f"{action_name}/icon.svg", "w") as f:
        f.write(icon_svg)
    print("✓ icon.svg")

    # 6. Test workflow
    test_workflow = f"""name: Test {action_name}

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ${{{{ matrix.os }}}}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]

    steps:
      - uses: actions/checkout@v4
      - uses: ./
        with:
          param1: test
"""

    with open(f"{action_name}/.github/workflows/test.yml", "w") as f:
        f.write(test_workflow)
    print("✓ .github/workflows/test.yml")

    # 7. .gitignore
    gitignore = """# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp

# Node
node_modules/
.env

# Python
__pycache__/
*.py[cod]
"""

    with open(f"{action_name}/.gitignore", "w") as f:
        f.write(gitignore)
    print("✓ .gitignore")

    print(f"""
✅ GitHub Marketplace action '{action_name}' created!

Next steps:
1. cd {action_name}
2. Edit action.yml with your inputs/outputs
3. Edit README.md with examples
4. Update icon.svg
5. git init && git add . && git commit -m "Initial action"
6. git tag -a v1.0.0 -m "Release v1.0.0"
7. git push origin main && git push origin v1.0.0
8. Enable Marketplace listing in Settings

📖 Docs: https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace
🎨 Icons: https://feathericons.com/
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_marketplace_action.py <action-name> [author-name]")
        print("Example: python create_marketplace_action.py my-awesome-action 'John Doe'")
        sys.exit(1)

    action_name = sys.argv[1]
    author = sys.argv[2] if len(sys.argv) > 2 else "Your Name"

    create_action(action_name, author)
