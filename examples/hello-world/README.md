# Hello World Action

A simple greeting and counting GitHub Action - perfect for learning and testing workflows.

## Features

- 👋 Customizable greeting messages
- 🔢 Count to any number
- 📤 Output messages for workflow use
- 🎯 Works on Windows, macOS, and Linux

## Usage

### Basic Usage

```yaml
- name: Run Hello World
  uses: TheCoderOfInformatics/JARVIS-Plugins/examples/hello-world@main
  with:
    name: Alice
    count: 10
```

### Using Outputs

```yaml
- name: Run Hello World
  id: hello
  uses: TheCoderOfInformatics/JARVIS-Plugins/examples/hello-world@main
  with:
    name: 'GitHub Actions'
    count: 5

- name: Print Results
  run: |
    echo "Greeting: ${{ steps.hello.outputs.greeting }}"
    echo "Result: ${{ steps.hello.outputs.result }}"
```

### Example Workflow

```yaml
name: Example Workflow
on: push

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Greet the world
        uses: TheCoderOfInformatics/JARVIS-Plugins/examples/hello-world@main
        with:
          name: Developer
          count: 7
```

## Inputs

### `name`

**Required**: false  
**Default**: `"World"`

The name to greet in the message.

### `count`

**Required**: false  
**Default**: `"5"`

The number to count up to (1 to N).

## Outputs

### `greeting`

The greeting message string.

### `result`

The count result message.

## Examples

### Example 1: Simple Greeting

```yaml
- uses: TheCoderOfInformatics/JARVIS-Plugins/examples/hello-world@main
```

Output: `Hello, World! This is GitHub Actions. 👋`

### Example 2: Custom Name and Count

```yaml
- uses: TheCoderOfInformatics/JARVIS-Plugins/examples/hello-world@main
  with:
    name: 'JARVIS'
    count: 20
```

### Example 3: Using Environment Variables

```yaml
- uses: TheCoderOfInformatics/JARVIS-Plugins/examples/hello-world@main
  with:
    name: ${{ github.actor }}
    count: 10
```

## Support

For issues, questions, or suggestions:
- 📝 [GitHub Issues](https://github.com/TheCoderOfInformatics/JARVIS-Plugins/issues)
- 💬 [Discussions](https://github.com/TheCoderOfInformatics/JARVIS-Plugins/discussions)

## License

MIT - see LICENSE file

---

**Created with ❤️ by JARVIS Team**
