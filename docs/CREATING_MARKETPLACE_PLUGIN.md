# Neues GitHub Marketplace Plugin erstellen

Diese Anleitung zeigt, wie du ein neues Plugin für GitHub Marketplace erstellst.

## Schritt 1: Repository initialisieren

```bash
mkdir my-jarvis-action
cd my-jarvis-action
git init
```

## Schritt 2: action.yml erstellen

```yaml
name: 'My Action Name'
author: 'Your Name'
description: 'What your action does (max 125 chars)'
branding:
  icon: 'check-circle'  # From Feather Icons
  color: 'purple'

inputs:
  input-name:
    description: 'What this input does'
    required: false
    default: 'default-value'

outputs:
  result:
    description: 'Output description'

runs:
  using: 'composite'
  steps:
    - run: echo "Hello from Action"
      shell: bash
```

## Schritt 3: Dateien hinzufügen

### README.md (Marketplace Required)

```markdown
# My Action

One-liner description here.

## Usage

\`\`\`yaml
- uses: username/repo-name@v1
  with:
    input-name: value
\`\`\`

## Inputs

### input-name
Description here.

## Outputs

### result
Description here.

## Examples

### Example 1
\`\`\`yaml
steps:
  - uses: username/repo-name@v1
\`\`\`
```

### icon.svg (Marketplace Required)

```svg
<svg width="200" height="200" viewBox="0 0 200 200">
  <rect width="200" height="200" fill="#6f42c1" rx="30"/>
  <!-- Your icon here -->
</svg>
```

### CHANGELOG.md (Recommended)

```markdown
# Changelog

## [1.0.0] - 2025-04-15

### Added
- Initial release
```

### LICENSE (Required)

```
MIT License
[standard license text]
```

### Test Workflow (.github/workflows/test.yml)

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ./
```

## Schritt 4: Versionieren

```bash
git add .
git commit -m "Initial action"
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin main
git push origin v1.0.0
```

## Schritt 5: GitHub Marketplace Registration

1. **Repository-Einstellungen öffnen**
   - Settings → Marketplace listing

2. **"List this action in GitHub Marketplace" aktivieren**

3. **Marketplace Form ausfüllen:**
   - Category
   - Short description (125 chars)
   - Full description
   - Branding (icon + color)
   - Support information
   - Pricing (free oder paid)

4. **Submit for Review**
   - GitHub Team wertet aus (1-7 Tage)

## Schnelle Checkliste

```
✅ action.yml vorhanden & valid
✅ README mit Beispielen
✅ icon.svg (200x200px)
✅ LICENSE Datei
✅ CHANGELOG.md
✅ Test Workflow
✅ Git Tags (v1.0.0)
✅ Repository public
✅ Inputs/Outputs dokumentiert
```

## Häufige Fehler

❌ Kein action.yml
❌ Icon falsch dimensioniert
❌ README zu kurz
❌ Private Repository
❌ Tags nicht gesetzt
❌ Keine Inputs/Outputs Docs

## Weiterführende Links

- [Create Actions](https://docs.github.com/en/actions/creating-actions)
- [Publish to Marketplace](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace)
- [action.yml Syntax](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)
- [Feather Icons](https://feathericons.com/)

---

**Bereit? Erstelle deine erste Marketplace Action!** 🚀
