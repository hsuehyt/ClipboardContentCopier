# ClipboardContentCopier

This repository contains the Python script `ClipboardContentCopier.py` which allows you to copy the contents of a text file directly to your system clipboard. It utilizes the `pyperclip` library for clipboard operations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the script, ensure you have Python installed on your machine. The script has been tested with Python 3.6 and above. You will also need the `pyperclip` library, which the script uses to interface with the clipboard.

### Installation

1. **Install Python:**
   - Download and install Python from [the official Python website](https://www.python.org/downloads/). Make sure Python is added to your system's PATH during installation. The script requires **Python 3.6 or later**.

2. **Install Pyperclip:**
   - Open your command prompt or terminal.
   - Execute the following command to install the `pyperclip` module:
     ```
     pip install pyperclip
     ```

### Usage

1. **Prepare your text file:**
   - Ensure your text file is ready and note down its path. The script is designed to read text files.

2. **Edit the script:**
   - Open the script `ClipboardContentCopier.py` in a text editor or IDE.
   - Modify the `file_path` variable to point to the location of your text file:
     ```python
     file_path = r"C:\path\to\your\file.txt"
     ```

3. **Run the script:**
   - Execute the script using Python from your command line:
     ```
     python ClipboardContentCopier.py
     ```

## Troubleshooting

If you encounter an error stating that "pip is not recognized," ensure that Python's `Scripts` directory is added to your system's PATH as described in the installation section.

## Contributing

Contributions are welcome! Please feel free to fork the project and submit a pull request if you have improvements or bug fixes.

## License

This script is provided "as is", without warranty of any kind, express or implied. Use at your own risk.
