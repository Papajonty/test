import tkinter as tk
import pyperclip

def encrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_message += shifted_char
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    
    result_label.config(text=encrypted_message)

def decrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())
    decrypted_message = ""

    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_message += shifted_char
        elif char.isdigit():
            shifted_char = str((int(char) - shift) % 10)
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    
    result_label.config(text=decrypted_message)

def copy_result():
    result = result_label.cget("text")
    pyperclip.copy(result)

def clear_fields():
    entry_message.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Message Encryption/Decryption")
root.geometry("500x500")

frame1 = tk.Frame(root)
frame1.pack(pady=20)

message_label = tk.Label(frame1, text="Message:", font=("Helvetica", 14))
message_label.grid(row=0, column=0, padx=10)

entry_message = tk.Entry(frame1, font=("Helvetica", 14), width=30)
entry_message.grid(row=0, column=1, padx=10)

frame2 = tk.Frame(root)
frame2.pack(pady=20)

shift_label = tk.Label(frame2, text="Shift:", font=("Helvetica", 14))
shift_label.grid(row=0, column=0, padx=10)

entry_shift = tk.Entry(frame2, font=("Helvetica", 14), width=30)
entry_shift.grid(row=0, column=1, padx=10)

frame3 = tk.Frame(root)
frame3.pack(pady=20)

encrypt_button = tk.Button(frame3, text="Encrypt", command=encrypt_message, font=("Helvetica", 14), width=15)
encrypt_button.grid(row=0, column=0, padx=10)

