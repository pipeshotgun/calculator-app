import tkinter as tk
from tkinter import messagebox

# --- Logic Functions ---
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Div by 0"
    return a / b

# --- GUI Trigger Function ---
def calculate(operation):
    try:
        # Get values from the Entry widgets
        num1 = float(entry_a.get())
        num2 = float(entry_b.get())
        
        if operation == 'add':
            res = add(num1, num2)
        elif operation == 'sub':
            res = subtract(num1, num2)
        elif operation == 'mul':
            res = multiply(num1, num2)
        elif operation == 'div':
            res = divide(num1, num2)
            
        # Update the result label
        label_result.config(text=f"Result: {res}", fg="black")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# --- Main Window Setup ---
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input Fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

# We use 'lambda' so the function doesn't run immediately on startup
tk.Button(btn_frame, text="+", width=5, command=lambda: calculate('add')).grid(row=0, column=0)
tk.Button(btn_frame, text="-", width=5, command=lambda: calculate('sub')).grid(row=0, column=1)
tk.Button(btn_frame, text="*", width=5, command=lambda: calculate('mul')).grid(row=1, column=0)
tk.Button(btn_frame, text="/", width=5, command=lambda: calculate('div')).grid(row=1, column=1)

# Result Display
label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()


               
