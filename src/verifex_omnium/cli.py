"""Command line interface for Verifex Omnium."""

import argparse
import json
import sys
from typing import Dict, List, Optional

from verifex_omnium.core import ContentVerifier
from verifex_omnium.blockchain import BlockchainInterface


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Verifex Omnium: Blockchain-native content verification"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Sign command
    sign_parser = subparsers.add_parser("sign", help="Sign content for verification")
    sign_parser.add_argument("file", help="Path to the file to sign")
    sign_parser.add_argument(
        "--type", 
        choices=["text", "image", "audio", "video"], 
        required=True,
        help="Type of content"
    )
    sign_parser.add_argument(
        "--output", 
        help="Output file for the signature (default: stdout)"
    )
    
    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify content signature")
    verify_parser.add_argument("file", help="Path to the file to verify")
    verify_parser.add_argument("signature", help="Path to the signature file")
    verify_parser.add_argument(
        "--type", 
        choices=["text", "image", "audio", "video"], 
        required=True,
        help="Type of content"
    )
    
    # Cost estimate command
    cost_parser = subparsers.add_parser("cost", help="Estimate storage cost")
    cost_parser.add_argument("size_kb", type=float, help="Size in KB")
    
    return parser.parse_args()


def main() -> None:
    """Main entry point for the CLI."""
    args = parse_args()
    
    if args.command == "sign":
        # Placeholder for sign implementation
        print(f"Signing {args.file} as {args.type}")
        
    elif args.command == "verify":
        # Placeholder for verify implementation
        print(f"Verifying {args.file} against signature {args.signature}")
        
    elif args.command == "cost":
        # Cost estimation implementation
        blockchain = BlockchainInterface()
        cost = blockchain.get_transaction_cost(args.size_kb)
        print(json.dumps(cost, indent=2))
        
    else:
        print("No command specified. Use --help for usage information.")
        sys.exit(1)


if __name__ == "__main__":
    main()
