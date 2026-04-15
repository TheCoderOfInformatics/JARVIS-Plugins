# Lizenzen & Verkauf

## Plugin-Lizensmodelle

### Kostenlos (Open Source)

```json
{
  "price": 0,
  "license": "MIT",
  "repository": "https://github.com/youruser/jarvis-plugin-xxx"
}
```

Verwendung: Community-Plugins, Open-Source-Integration

### Kommerziell (Einzellizenz)

```json
{
  "price": 9.99,
  "currency": "EUR",
  "license": "Kommerziell"
}
```

Verkauf: JARVIS Marketplace → Zahlungsabwicklung über Stripe/PayPal

### Enterprise (Volumenlizenz)

```json
{
  "price": 49.99,
  "currency": "EUR",
  "license": "Enterprise - 5 Lizenzen",
  "description": "Für Teams bis 5 Nutzer"
}
```

## Lizenzschlüssel-System

### Generieren

```python
import hashlib
import json
from datetime import datetime, timedelta

def generate_license_key(plugin_name, user_email, days_valid=365):
    """Generiere Lizenzschlüssel"""
    
    expiry = datetime.now() + timedelta(days=days_valid)
    data = {
        "plugin": plugin_name,
        "user": user_email,
        "expiry": expiry.isoformat(),
        "version": "1.0"
    }
    
    # Signiere mit Plugin-Secret
    signature = hashlib.sha256(
        json.dumps(data).encode() + b"SECRET_KEY"
    ).hexdigest()[:12]
    
    license_key = f"JARVIS-{plugin_name.upper()}-{signature}-{data['expiry'][:10]}"
    return license_key
```

### Validieren (in Plugin)

```python
def validate_license(key):
    """Validiere Lizenzschlüssel beim Start"""
    
    # Beispiel: JARVIS-WEATHER-ABC123-2025-04-15
    parts = key.split("-")
    if len(parts) != 4:
        raise ValueError("Invalid license key format")
    
    expiry_str = parts[3]
    expiry = datetime.fromisoformat(expiry_str)
    
    if datetime.now() > expiry:
        raise ValueError("License expired")
    
    return True

# Im __init__ prüfen
def __init__(self, kernel=None, license_key=None):
    if license_key:
        validate_license(license_key)
    self.kernel = kernel
```

## Marketplace-Integration

### Zahlungsabwicklung

1. **Benutzer kauft Plugin** → PayPal/Stripe
2. **Lizenzschlüssel wird generiert** → E-Mail an Benutzer
3. **Plugin lädt mit Lizenzschlüssel** → Validierung beim Start

### Revenue-Sharing

- **JARVIS Marketplace**: 30% Gebühr
- **Plugin-Author**: 70% Verdienst

## Best Practices

### Was monetarisiert werden kann?

✅ Enterprise-Integrationen (SAP, Oracle, Salesforce)
✅ Advanced Analytics & Reporting
✅ Team-Collaboration Features
✅ Priority Support
✅ Custom Branding

❌ Core JARVIS Tools (Conflict of Interest)
❌ Stolen/Repackaged Content
❌ Overlapping Functionality

### Preisgestaltung

| Typ | Preis | Zielgruppe |
|-----|-------|-----------|
| Pro Plugin | €9,99 | Einzelnutzer |
| Business Set | €29,99 | Small Business |
| Enterprise | €99,99 | Unternehmen |

### Versioning & Updates

```json
{
  "version": "1.0.0",
  "jarvis_min_version": "1.0.0",
  "breaking_changes": false,
  "update_frequency": "monthly"
}
```

Semantische Versionierung: `MAJOR.MINOR.PATCH`

## Compliance

- ✅ Keine Malware, Spyware, Backdoors
- ✅ Datenschutz-konform (DSGVO, CCPA)
- ✅ Keine versteckten Funktionen
- ✅ Transparente Preisgestaltung
- ✅ Refund-Policy: 30 Tage Geld-zurück

---

**Fragen?** → GitHub Discussions oder Email
