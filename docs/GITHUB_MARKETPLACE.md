# GitHub Marketplace Anforderungen für JARVIS Plugins

Diese Dokumentation beschreibt, wie JARVIS Plugins als **GitHub Actions** im GitHub Marketplace veröffentlicht werden.

## 📋 Anforderungen

### 1. Repository-Struktur

```
repository/
├── action.yml              # Action Manifest (REQUIRED)
├── README.md              # Documentation (REQUIRED)
├── LICENSE                # MIT/GPL etc (REQUIRED)
├── CHANGELOG.md           # Version History
├── .github/
│   └── workflows/
│       └── test.yml       # Test Workflow
└── icon.svg               # 200x200px Icon (REQUIRED)
```

### 2. action.yml Anforderungen

```yaml
name: 'Action Name'           # Required - max 50 chars
author: 'Your Name'           # Required
description: 'Description'    # Required - max 125 chars
branding:
  icon: 'icon-name'          # Required - from Feather Icons
  color: 'purple|blue|...'   # Required
inputs:                        # Document all inputs
  param:
    description: 'Desc'
    required: false
outputs:                       # Document all outputs
  result:
    description: 'Desc'
runs:
  using: 'composite|docker|node20'  # Pick one
```

### 3. README Anforderungen

- **Title & Description** - Clear action purpose
- **Branding** - Logo/icon in repo
- **Usage Example** - Minimal YAML example
- **Input Parameters** - Document all inputs
- **Output Parameters** - Document all outputs
- **Example Workflows** - Real-world examples (3-5)
- **Support Info** - Issues/Discussions links
- **License** - Clearly stated

### 4. Branding Requirements

- **Icon**: 200x200px SVG or PNG
- **Color**: Purple, blue, green, red, gray, yellow, etc.
- **Logo**: Brand assets in `/docs` folder

### 5. Version & Release

```bash
# Tag versions semantically
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# Update major tag for latest
git tag -fa v1 -m "Release v1"
git push origin -f v1
```

### 6. Submission Requirements

Before submitting to GitHub Marketplace:

- ✅ Action works correctly
- ✅ All inputs/outputs documented
- ✅ README has examples
- ✅ LICENSE file present
- ✅ Icon/branding added
- ✅ CHANGELOG updated
- ✅ Repo public
- ✅ Passing tests
- ✅ Privacy policy (if collecting data)
- ✅ Support contact info

### 7. Publishing to GitHub Marketplace

1. **Push to GitHub**
   ```bash
   git push origin main
   ```

2. **Create Release**
   - Go to Releases
   - Create new release
   - Tag: `v1.0.0`
   - Title: "Release v1.0.0"
   - Publish

3. **List on Marketplace**
   - Go to Settings > Marketplace listing
   - Enable "List this action in GitHub Marketplace"
   - Fill marketplace form with:
     - Category
     - Short description (125 chars)
     - Long description
     - Pricing tier (free/paid)
     - Support URL

4. **GitHub Reviews**
   - GitHub team reviews submission
   - May take 1-7 days
   - You'll be notified

## 🎯 Best Practices

### Documentation

```markdown
# Action Title

One-liner description.

## Features
- Feature 1
- Feature 2

## Usage
\`\`\`yaml
- uses: owner/repo/path@v1
  with:
    input: value
\`\`\`

## Inputs/Outputs
[Document here]

## Examples
[3-5 Real examples]

## Support
[Links]
```

### Icon/Branding

```
Icon Requirements:
- 200x200px minimum
- SVG or PNG
- Single color or simple gradient
- Clear when scaled down
- Matches GitHub design language
```

### Versioning

```
Semantic Versioning: MAJOR.MINOR.PATCH
v1.0.0 = Major version 1, no minor features, no patches

Always keep major tag updated:
git tag -fa v1
git tag -fa v1.0
git push origin -f v1 v1.0
```

### Testing Before Release

```yaml
# .github/workflows/test.yml
name: Test Action

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./  # Test the action
        with:
          input: test-value
```

## ❌ Common Mistakes

1. ❌ Missing action.yml
2. ❌ No branding section
3. ❌ Icon too large/wrong format
4. ❌ README without examples
5. ❌ No LICENSE file
6. ❌ Private repository
7. ❌ Outdated documentation
8. ❌ No tests in repo
9. ❌ Unclear input/output descriptions
10. ❌ Not semantic versioning

## ✅ Checklist Before Submission

- [ ] Repository is public
- [ ] action.yml exists and is valid
- [ ] All inputs/outputs documented
- [ ] README has examples
- [ ] Icon/branding added (200x200px)
- [ ] LICENSE file present
- [ ] CHANGELOG.md updated
- [ ] Tests passing
- [ ] Git tags created (v1.0.0, v1, v1.0)
- [ ] No secrets in code
- [ ] Privacy policy (if needed)
- [ ] Support/contact info in README

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Creating Actions](https://docs.github.com/en/actions/creating-actions)
- [Publishing Actions](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace)
- [Action Metadata Syntax](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)
- [Feather Icons](https://feathericons.com/) - For branding icons

---

**Ready to publish your action? Follow this guide and submit!** 🚀
