# VaultCLI

VaultCLI is a cross platform encrypted password manager that runs entirely inside the terminal. It securely stores user passwords using AES encryption, supports auto-lock after inactivity, and makes password management fast and easy.

## Features

- **Secure Encryption** - Each user has a seperate encrypted vault using Fernet (AES-128) with a key derived from their master password.
- **User Accounts** - Supports creating multiple users with hashed master passwords.        
- **Password Generation** - Generate strong passwords with customisable lengths.
- **Clipboard Support** - Passwords are copied to clipboard when retrieved.
- **Vault Auto-Lock** - Vault automatically locks after 5 minutes of inactivity.
- **Cross-platform** - Works on Windows, MacOS and Linux.
- **Lightweight CLI** - No GUI dependencies, runs on any terminal.

## Installation

You can install VaultCLI directly from PyPI:

```bash
pip install vaultcli-aaronsood