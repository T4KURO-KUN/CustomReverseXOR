# Custom Reverse XOR

A lightweight command-line interface (CLI) tool written in Python that performs a custom encoding using a combination of string reversal and a byte-level XOR cipher.

## Features

- **Interactive CLI Menu:** Clean and modern terminal interface powered by [Rich](https://github.com/Textualize/rich).
- **Encrypt:** Reverses a string, applies a XOR mask (default key: `0x42`), and outputs the result in hexadecimal format.
- **Decrypt:** Parses the hex string, reverses the operation, and recovers the original text.
- **Cross-platform:** Runs smoothly on Linux, macOS, Windows, and Android via Termux.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/T4KURO-KUN/CustomReverseXOR.git
cd CustomReverseXOR
pip install -r requirements.txt
```

## Usage
Run the script using Python:
```Bash
python tui-custom-hash.py
