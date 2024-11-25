# Calculator Project

## Overview
The **Calculator Project** is a Python-based interactive calculator that performs basic arithmetic operations. It provides a simple and user-friendly interface for addition, subtraction, multiplication, and division, and allows users to continue calculations using previous results.

---

## Features
- Performs four basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Allows continuous calculations using the result of the previous operation.
- Provides an option to start a new calculation or exit the program.
- Displays a custom ASCII art logo for a fun and engaging user experience.

---

## Requirements
This project requires **Python 3.x**. No additional libraries are needed as it uses Python's built-in functionality.

---

## How to Use
1. Clone or download this repository to your local machine.
2. Open the project in your preferred Python IDE or text editor.
3. Run the script in a terminal or IDE.

### Steps to Use the Calculator
1. The program will display the logo.
2. Enter the first number when prompted.
3. Choose an operation from the available options (`+`, `-`, `*`, `/`).
4. Enter the second number.
5. The program will calculate and display the result.
6. You will be prompted to:
   - Type `y` to continue calculating with the current result.
   - Type `new` to start a new calculation.
   - Type `n` to exit the calculator.

---

## Example
```
 _____________________
|  _________________  |
| | Pythonista   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

Write the first number: 8
+
Choose operation: +
Write the second number: 5
8 + 5 = 13
Type 'y' to continue calculating with 13, type new to start new calculation, or type 'n' to exit. y
Choose operation: *
Write the second number: 2
13 * 2 = 26
Type 'y' to continue calculating with 26, type new to start new calculation, or type 'n' to exit. n
```

---

## Code Explanation
Below is a brief explanation of the key sections of the code:

### 1. ASCII Art Logo
- The `logo` variable contains ASCII art that is displayed at the start of the program to enhance user engagement.

### 2. Arithmetic Functions
- **`add`**: Adds two numbers.
- **`subtract`**: Subtracts the second number from the first.
- **`multiply`**: Multiplies two numbers.
- **`divide`**: Divides the first number by the second.

### 3. Operations Dictionary
- The `operations` dictionary maps symbols (`+`, `-`, `*`, `/`) to their respective functions.

### 4. Main Calculator Function
- The `calculator` function handles user input, performs calculations, and manages program flow (e.g., continuing with results, starting new calculations, or exiting).

---

## Contributing
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## Acknowledgments
- Inspired by the need for a simple and interactive calculator.
- Built using Python's functional programming concepts and user input handling.

