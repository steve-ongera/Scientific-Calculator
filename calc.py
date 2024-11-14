import tkinter as tk
import math

# Function to update the display
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + key)

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())  # Use Python's eval function to calculate the result
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate power (x^y)
def power():
    try:
        expression = entry.get()
        base, exp = expression.split('^')
        result = math.pow(float(base), float(exp))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate square root
def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to square the number (x²)
def square():
    try:
        result = float(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Set up the window
window = tk.Tk()
window.title("Scientific Calculator")

# Entry widget to show the current input or result
entry = tk.Entry(window, width=25, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=5)

# Define buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('√', 4, 4),
    ('^', 5, 0), ('x²', 5, 1)
]

# Create and place buttons on the window
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    elif text == '=':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=evaluate)
    elif text == '√':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=sqrt)
    elif text == '^':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=power)
    elif text == 'x²':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=square)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=lambda key=text: press(key))
    button.grid(row=row, column=col)

# Start the Tkinter main loop
window.mainloop()
