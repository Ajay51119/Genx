import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import subprocess
import webbrowser

current_file_path = None

def save_file():
    global current_file_path
    if current_file_path:
        content = text_editor.get("1.0", tk.END)
        with open(current_file_path, "w") as file:
            file.write(content)
    else:
        save_as_file()

def save_as_file():
    global current_file_path
    content = text_editor.get("1.0", tk.END)
    current_file_path = filedialog.asksaveasfilename(defaultextension=".c", filetypes=[("C files", "*.c"), ("All files", "*.*")])
    if current_file_path:
        with open(current_file_path, "w") as file:
            file.write(content)

def open_file():
    global current_file_path
    file_path = filedialog.askopenfilename(filetypes=[("C files", "*.c"), ("All files", "*.*")])
    if file_path:
        current_file_path = file_path
        with open(current_file_path, "r") as file:
            content = file.read()
            text_editor.delete("1.0", tk.END)
            text_editor.insert(tk.END, content)

def compile_and_run():
    global current_file_path
    if not current_file_path:
        save_as_file()
    try:
        # Compile the C file
        subprocess.run(["gcc", current_file_path, "-o", "compiled_file"], check=True)
        
        # Run the compiled file
        subprocess.run(["./compiled_file"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def read_doc():
    webbrowser.open("https://www.w3schools.com/c")

root = tk.Tk()
root.title("Gen-X editor")
root.iconbitmap("gen-x.ico")
root.maxsize(2000, 800)
 
root.configure(bg="black")  # Set background color to black

text_editor = scrolledtext.ScrolledText(root, width=100, height=30, bg="black", fg="white", insertbackground="green", font=("Helvetica", 16))  
text_editor.pack()


menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.quit)

run_menu = tk.Menu(menu)
menu.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Compile & Run", command=compile_and_run)

help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="read_doc", command=read_doc)

root.mainloop()
