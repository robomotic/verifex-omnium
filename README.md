# Verifex Omnium

<p align="center">
  <img src="https://raw.githubusercontent.com/robomotic/verifex-omnium/main/assets/verifex-banner.png" alt="Verifex Omnium Banner" width="800"/>
</p>

> **Blockchain-native content verification for the digital age**
>
> **Fighting deep fakes, disinformation, and misinformation through verifiable content**

## Overview

Verifex Omnium is an open project that provides robust content verification and authentication across multiple media types. While similar to the C2PA standard, Verifex Omnium takes a fundamentally different approach by being **truly open** with no expensive membership fees required to contribute. The project takes a novel approach by:

- **Blockchain-native**: Built from the ground up for distributed ledger technology
- **Format-agnostic**: Works seamlessly with text, audio, and video content
- **Truth-focused**: Designed specifically for fact verification rather than just provenance
- **Identity-centric**: Tailored for online personas including celebrities, journalists, and politicians

## Key Features

- **Multi-media verification**: Authenticate and verify text, audio, and video content
- **Digital interview signing**: Provide cryptographic proof of interview authenticity
- **Non-metadata approach**: Operates without relying on or altering metadata
- **Traditional cryptography support**: Full compatibility with GPG/PGP keys
- **Blockchain integration**: Leverages distributed ledger technology for immutable verification
- **AI-powered embeddings**: Utilizes state-of-the-art transformer models to create embeddings of text, audio, video, and images, enabling provenance tracking even when content is modified (e.g., images cropped, text excerpted)

## Blockchain Storage & Costs

Verifex Omnium utilizes Polygon (MATIC) as the primary blockchain protocol for storing digital signatures, offering an optimal balance between security, decentralization, and cost-efficiency.

| Content Type | Signature Size | Estimated Cost (USD) | Notes |
|--------------|----------------|----------------------|-------|
| Text document | ~0.5-2 KB | $0.001-0.003 | Cost varies with document complexity and signature type |
| Image | ~2-3 KB | $0.003-0.005 | Hash-based signatures keep costs minimal |
| Video | ~3-5 KB | $0.005-0.010 | Only signature data is stored on-chain, not content |

> **Note**: Costs are estimates based on April 2025 Polygon gas prices and may fluctuate based on network activity. Verifex Omnium employs batching techniques to further reduce costs for bulk operations.

The Polygon blockchain was selected for its:
- Low transaction fees (typically <$0.01)
- High throughput (>2000 TPS)
- EVM compatibility
- Carbon-neutral operations
- Robust security through Ethereum finality

## Use Cases

- Journalists can verify sources and provide proof of authentic interviews
- Politicians can cryptographically sign statements to prevent misattribution
- Media organizations can validate content origin and authenticity
- Celebrities can verify official statements and combat misinformation
- Content creators can protect their work with blockchain-backed verification

## Getting Started

This section explains how to set up a development environment for Verifex Omnium using pyenv, Poetry, and uv.

### Prerequisites

- Git
- Python 3.10+
- pyenv (for Python version management)
- pipx (for installing Poetry and uv)

### Development Environment Setup

#### 1. Install pyenv

If you don't have pyenv installed, you can install it by following the [official installation guide](https://github.com/pyenv/pyenv#installation).

Quick install:

```bash
curl https://pyenv.run | bash
```

Add to your shell configuration:

```bash
# For bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

#### 2. Install the required Python version

```bash
pyenv install 3.10.12
cd /path/to/verifex-omnium
pyenv local 3.10.12  # This creates/updates .python-version file
```

#### 3. Install pipx (if not installed)

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

#### 4. Install Poetry and uv with pipx

```bash
pipx install poetry
pipx install uv
```

#### 5. Configure Poetry to use uv

```bash
poetry config installer.modern-installation true
```

#### 6. Set up the project

Clone the repository (if you haven't):

```bash
git clone https://github.com/your-username/verifex-omnium.git
cd verifex-omnium
```

#### 7. Install dependencies

```bash
poetry install
```

This will:
- Create a virtual environment
- Install all dependencies specified in pyproject.toml
- Install the project in development mode

### Development Workflow

#### Activate the virtual environment

```bash
poetry shell
```

#### Run the CLI

```bash
python -m verifex_omnium.cli --help
```

#### Running tests

```bash
poetry run pytest
```

#### Code formatting

```bash
poetry run black .
poetry run isort .
```

#### Linting

```bash
poetry run ruff .
poetry run mypy .
```

### Adding new dependencies

#### Runtime dependencies

```bash
poetry add package-name
```

#### Development dependencies

```bash
poetry add --group dev package-name
```

### Benefits of this Setup

- **pyenv**: Manages Python versions, ensuring consistent environment across developers
- **Poetry**: Handles dependencies, virtual environments, and packaging
- **uv**: Accelerates package installations with faster dependency resolution
- **Combined**: All three tools work together to create a robust, reproducible development environment

### Troubleshooting

If you encounter any issues, please check:

1. That your Python version matches 3.10.12 (`python --version`)
2. That Poetry is using the correct Python interpreter (`poetry env info`)
3. For dependency issues, try `poetry update` to resolve them

## Contributing

We welcome contributions from the community! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  <i>Verifex Omnium: Verifying truth in the digital age</i>
</p>
