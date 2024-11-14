# Scientific Calculator

This is a Python-based scientific calculator built using the `Tkinter` library. It allows users to perform basic arithmetic operations as well as scientific calculations such as exponentiation, square roots, and squaring numbers.

## Features

- **Basic Arithmetic Operations:**
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  
- **Scientific Functions:**
  - Exponentiation (`^`): Raise a number to any power.
  - Square Root (`√`): Calculate the square root of a number.
  - Square (`x²`): Square a number (multiply it by itself).

## Requirements

- Python 3.x (Tkinter comes pre-installed with Python)
- Tkinter library (usually comes with Python)

## Installation

1. Make sure you have **Python 3.x** installed on your system. You can check this by running:
   ```bash
   python --version
  ```
2. If Tkinter is not installed (it is usually included with Python), you can install it using:

pip install tk


Download or clone this repository to your local machine.

Navigate to the project folder in your terminal or command prompt.

Run the calculator script:


```python scientific_calculator.py```

## Usage
Once the application is running, you can use the buttons to perform various operations:

Basic Operations:

Click on any number button to input numbers.
Use the +, -, *, / buttons for basic arithmetic operations.
Scientific Operations:

- To calculate the exponentiation, use the ^ button (e.g., 3^3 results in 27).
- To calculate the square root, use the √ button (e.g., √16 results in 4).
- To square a number, use the x² button (e.g., 5 and then x² results in 25).
- Clear and Evaluate:

The C button clears the current input.
The = button evaluates the entered expression and shows the result.

## Example
Exponentiation:

Enter 3^3 and press =, the result will be 27.
Square Root:

Enter √16 and press =, the result will be 4.
Square a Number:

Enter 5 and press x², the result will be 25.

## Code Structure

 **press(key)**: This function is used to update the entry field when a number or operator is clicked.
 **clear()**: This function clears the input field.
**evaluate()**: This function evaluates the expression entered by the user using Python's eval() function.
**power()**: This function handles the exponentiation operation.
**sqrt()**: This function calculates the square root of the number entered.
**square()**: This function squares the entered number.
**Screenshots**

## Contributing
Feel free to fork this repository and submit pull requests. If you want to contribute or suggest new features, please open an issue or contact me directly.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


### Explanation of Sections:

1. **Project Description**: A brief explanation of the scientific calculator and what it can do (basic and scientific operations).
2. **Requirements**: Information on what is needed to run the project.
3. **Installation**: Step-by-step instructions for installing and running the project.
4. **Usage**: How to interact with the calculator once it’s running.
5. **Example**: Examples of operations that can be performed in the calculator.
6. **Code Structure**: A brief description of the main functions in the code and what they do.
7. **Screenshots**: Placeholder for screenshots of the calculator (optional).
8. **Contributing**: Instructions on how others can contribute to the project.
9. **License**: Information on licensing (you can specify the license in a `LICENSE` file or mention MIT).

This `README.md` will help users understand the purpose of your calculator, how to install and use it, and provide additional details about the project.
