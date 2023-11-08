import tkinter as tk
import secrets
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        return'''Please select 
        at least one character type.'''
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def show_generated_password_popup(generated_password):
    popup_window = tk.Toplevel(window)
    popup_window.title("Generated Password")
    
    popup_label = tk.Label(popup_window, text="Generated Password: " + generated_password, font=("Arial", 14))
    popup_label.pack(padx=20, pady=10)
    
    ok_button = tk.Button(popup_window, text="OK", command=popup_window.destroy)
    ok_button.pack(pady=10)

def generate_password_button_clicked():
    password_length = int(length_entry.get())
    lowercase_checked = lowercase_var.get()
    uppercase_checked = uppercase_var.get()
    digits_checked = digits_var.get()
    special_chars_checked = special_chars_var.get()
    
    generated_password = generate_password(
        password_length,
        lowercase_checked,
        uppercase_checked,
        digits_checked,
        special_chars_checked
    )
    
    result_label.config(text="Generated Password: " + generated_password)
    
    # Show the pop-up window with the generated password
    show_generated_password_popup(generated_password)

# Create the GUI window
window = tk.Tk()
window.title("Password Generator")

# Configure window size and background color
window.geometry("400x450")
window.configure(bg="black")

# Title Label
title_label = tk.Label(window, text="PASSWORD GENERATOR", font=("Arial", 24, "bold"), bg="red", fg="white")
title_label.pack(pady=20)

# Labels and Entry for password length
length_label = tk.Label(window, text="PASSWORD LENGTH:", font=("Arial", 14), bg="red", fg="white")
length_label.pack()
length_entry = tk.Entry(window, font=("Arial", 14))
length_entry.pack()

# Checkboxes for character types
lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(window, text="Lowercase Letters", variable=lowercase_var, font=("Arial", 12), bg="red", fg="white")
lowercase_check.pack()
lowercase_var.set(True)  # Default to including lowercase letters

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(window, text="Uppercase Letters", variable=uppercase_var, font=("Arial", 12), bg="red", fg="white")
uppercase_check.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(window, text="Digits", variable=digits_var, font=("Arial", 12), bg="red", fg="white")
digits_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(window, text="Special Characters", variable=special_chars_var, font=("Arial", 12), bg="red", fg="white")
special_chars_check.pack()

# Generate Password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_clicked, font=("Arial", 16), bg="red", fg="white")
generate_button.pack(pady=20)

# Label to display the generated password
result_label = tk.Label(window, text="", font=("Arial", 16), bg="#f5f5f5", fg="#333")
result_label.pack()

# Start the GUI event loop
window.mainloop()