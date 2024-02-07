# CrackDash
### A lightweight tool for blazing-fast ZIP and RAR password cracking using password list! 


---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Support and Contribution](#support-and-contribution)
- [License](#license)

---

## Overview

CrackDash is a lightweight and versatile password cracking tool designed for blazing-fast ZIP and RAR file password recovery using password lists. It provides an easy-to-use command-line interface for security researchers, penetration testers, and ethical hackers.

---

## Features

- **Cross-Platform Compatibility**: Works on Windows, Linux, and macOS.
- **ZIP and RAR Support**: Crack passwords for both ZIP and RAR file formats.
- **Optimized Brute-Force**: Efficiently tests passwords from user-provided password lists.
- **User-Friendly Interface**: Simple command-line interface for ease of use.
---

## Installation

### Prerequisites

- Python 3.x
- [rarfile](https://pypi.org/project/rarfile/) (for RAR support)
- You need a Password List to use this Script !
- Sample Password List: [Show](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
### Installation Steps
**Linux / macOS:**

1. Clone the repository:

    ```bash
    git clone https://github.com/0x00er/CrackDash.git
    ```

2. Install dependencies:

    ```bash
    pip install rarfile
    ```

3. Navigate to the project directory:

    ```bash
    cd CrackDash
    ```

4. Run CrackDash:

    ```bash
    python CrackDash.py
    ```

---

**Windows:**

1. **Install Python:**
   - Download and install Python 3.x from [python.org](https://www.python.org/downloads/).
   - During installation, make sure to check the option to add Python to the system PATH.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/CrackDash.git
   ```
## Usage

1. **Launch CrackDash:**

    ```bash
    python CrackDash.py
    ```

2. **Enter File Path and Password List:**

    - Enter the path to the ZIP or RAR file you want to crack.
    - Provide the path to the password list.

3. **Wait for Results:**

    - CrackDash will attempt to crack the password using the provided password list.
    - If successful, the password will be displayed, along with relevant statistics.

4. **Exit the Program:**

    - Choose '0' to exit the program.

---

## Support and Contribution

If you encounter any issues, have questions, or want to contribute, feel free to open an issue or submit a pull request. Contributions are welcome!

---

## License

This project is licensed under the [MIT License](LICENSE).

