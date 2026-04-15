# Code Guardian 🔐

**AI-Powered Code Review & Security Platform**

Automated code review using GPT-4, security vulnerability detection, quality metrics, dependency analysis, and AI-generated recommendations. Enterprise-grade code analysis.

**For Development Teams** | **AI-Powered Analysis** | **Multi-Language Support**

## 🎯 Features

### Code Analysis
- ✅ AI-Powered Code Review (GPT-4)
- ✅ Security Vulnerability Scanning
- ✅ Code Quality Metrics
- ✅ Performance Analysis
- ✅ Complexity Detection

### Security
- 🔍 OWASP Top 10 Checks
- 🚨 CVE Database Integration
- 🔑 Secrets Detection
- 📦 Dependency Vulnerabilities
- 🔐 Encryption Analysis

### Quality Metrics
- 📊 Code Coverage
- 🎯 Complexity Scoring
- 📈 Maintainability Index
- 🔄 Duplication Detection
- ✅ Style Violations

### Multi-Language
- ✅ Python
- ✅ JavaScript/TypeScript
- ✅ Java
- ✅ Go
- ✅ Rust
- ✅ C/C++

### AI Intelligence
- 🤖 Automated Reviews
- 💡 Best Practice Suggestions
- 🎓 Learning Resources
- 📚 Pattern Detection
- 🔮 Refactoring Tips

## 📖 Usage

### Full Code Analysis

```yaml
- name: Analyze Code
  id: guardian
  uses: TheCoderOfInformatics/code-guardian@v1
  with:
    repository: './'
    scan-type: 'all'
    ai-review: 'true'
    generate-report: 'true'
```

### Security Scan Only

```yaml
- name: Security Check
  id: security
  uses: TheCoderOfInformatics/code-guardian@v1
  with:
    repository: './'
    scan-type: 'security'
    severity: 'high'

- name: Fail on Vulnerabilities
  if: contains(steps.security.outputs.vulnerabilities, 'critical')
  run: exit 1
```

### Code Quality Check

```yaml
- name: Quality Gate
  id: quality
  uses: TheCoderOfInformatics/code-guardian@v1
  with:
    repository: './'
    scan-type: 'quality'

- name: Enforce Quality
  run: |
    SCORE="${{ steps.quality.outputs.quality-score }}"
    if (( $SCORE < 80 )); then
      echo "Quality too low ($SCORE)"
      exit 1
    fi
```

### Dependency Analysis

```yaml
- name: Check Dependencies
  id: deps
  uses: TheCoderOfInformatics/code-guardian@v1
  with:
    repository: './'
    scan-type: 'dependencies'

- name: Report Vulnerabilities
  run: |
    echo "Dependency Report:"
    echo "${{ steps.deps.outputs.vulnerabilities }}"
```

### Get AI Recommendations

```yaml
- name: Review Code
  id: review
  uses: TheCoderOfInformatics/code-guardian@v1
  with:
    repository: './'
    scan-type: 'all'
    ai-review: 'true'

- name: Display Recommendations
  run: |
    echo "AI Code Review:"
    echo "${{ steps.review.outputs.recommendations }}"
```

## Inputs

| Input | Required | Default | Description |
|-------|----------|---------|-------------|
| `repository` | ✅ | - | Repository path or URL |
| `scan-type` | ✅ | all | security, quality, dependencies, all |
| `language` | ❌ | auto-detect | Python, JavaScript, Java, Go, Rust |
| `severity` | ❌ | high | critical, high, medium |
| `ai-review` | ❌ | true | Enable AI analysis |
| `generate-report` | ❌ | true | Create HTML report |

## Outputs

### `issues-found`
Total number of issues (count)

### `security-score`
0-100 security assessment

### `quality-score`
0-100 quality rating

### `vulnerabilities`
```json
{
  "critical": 1,
  "high": 3,
  "medium": 5,
  "issues": [...]
}
```

### `recommendations`
```json
{
  "improvements": [...],
  "best_practices": [...],
  "refactoring_suggestions": [...]
}
```

## 💰 Pricing

| Plan | Price | Features |
|------|-------|----------|
| **Free** | $0 | Basic scanning |
| **Pro** | $14.99/mo | AI review, reports |
| **Enterprise** | $49.99/mo | Unlimited, custom rules |

## 🏆 Integrations

- ✅ GitHub Actions
- ✅ GitHub Pull Requests
- ✅ GitLab CI/CD
- ✅ Slack Notifications
- ✅ JIRA Integration

## 📝 Example Workflow

```yaml
name: Code Guardian Review
on: [push, pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Security & Quality Check
        id: guardian
        uses: TheCoderOfInformatics/code-guardian@v1
        with:
          repository: '.'
          scan-type: 'all'
          ai-review: 'true'
      
      - name: Comment PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Code Guardian Review\n\nSecurity: ${{ steps.guardian.outputs.security-score }}/100\nQuality: ${{ steps.guardian.outputs.quality-score }}/100\n\n${{ steps.guardian.outputs.recommendations }}`
            })
      
      - name: Fail on Critical Issues
        if: contains(steps.guardian.outputs.vulnerabilities, 'critical')
        run: exit 1
```

## 🆘 Support

- 📧 code@jarvis-plugins.dev
- 📚 Full Documentation

## 📄 License

Commercial License

---

**Enterprise Code Quality Assurance** 🚀
