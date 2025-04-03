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

*Documentation coming soon*

## Contributing

We welcome contributions from the community! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  <i>Verifex Omnium: Verifying truth in the digital age</i>
</p>
