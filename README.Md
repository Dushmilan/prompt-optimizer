# Prompt Optimizer

A CLI tool to optimize prompts using Google Generative AI.

## Installation

```bash
pip install prompt-optimizer
```

Or install from source:
```bash
pip install .
```

## Usage

```bash
prompt-optimizer "Create a 100 word essay about historical leadership" -i 3 -k YOUR_API_KEY
```

### Arguments
- `prompt`: The prompt to optimize
- `-i`, `--iterations`: Number of optimization iterations (default: 1)
- `-k`, `--api-key`: Google Generative AI API key (required)
```

Create a `requirements.txt` file:

```txt requirements.txt
google-generativeai>=0.5.0
```

Finally, create a directory structure like this:
```
prompt-optimizer/
├── PromptOptimizer.py
├── setup.py
├── README.md
├── requirements.txt
```

To install and use your package:

1. Install the package:
```bash
pip install .
```

2. Use the CLI:
```bash
prompt-optimizer "Your prompt here" -i 3 -k YOUR_API_KEY