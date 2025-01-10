# Gen-X Editor

Gen-X Editor is a simple text editor designed for writing, editing, compiling, and running C programs. It provides a user-friendly graphical interface using the Tkinter library in Python.

## Features

- **Save File**: Save your work easily.
- **Save As File**: Save your file with a specific name and location.
- **Open File**: Open existing `.c` files for editing.
- **Compile & Run**: Compile and execute your C program directly from the editor.
- **Documentation Access**: Quickly access C programming documentation.
- **Customizable Interface**: Dark theme with syntax-friendly colors for a comfortable editing experience.

## Prerequisites

- **Python**: Ensure you have Python 3.x installed.
- **Tkinter**: Tkinter is included with Python but ensure it is properly installed.
- **GCC Compiler**: The `gcc` compiler is required to compile and run C programs.

### Installation

1. Clone this repository or copy the script.
2. Ensure the required dependencies are installed.
   - For Ubuntu/Debian: `sudo apt-get install gcc python3-tk`
   - For Windows: Install GCC via MinGW or WSL, and ensure Python is installed.

### How to Use

1. Run the script:
   ```bash
   python gen_x_editor.py
   ```
2. Use the menu options:
   - **File**:
     - `Save`: Save the current file.
     - `Open`: Open an existing `.c` file.
     - `Exit`: Exit the application.
   - **Run**:
     - `Compile & Run`: Compile and execute the current C program.
   - **Help**:
     - `read_doc`: Open C programming documentation in your default web browser.

### File Structure

- **Editor Interface**: The main window includes a scrolled text area for code editing.
- **Menus**:
  - File menu for file operations.
  - Run menu for compiling and executing code.
  - Help menu for accessing documentation.

### Customization

- Modify the editor's theme by changing the `bg`, `fg`, and `insertbackground` properties in the script.
- Update the default font and size in the `ScrolledText` widget.

### Known Issues

- Ensure `gcc` is installed and accessible via the system's PATH.
- File paths with spaces or special characters may cause compilation issues.

### Future Enhancements

- Great for c program.
- Provide error output in a dedicated section within the editor.
- Support for other programming languages.

### License

This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

### Contributions

Contributions are welcome! Feel free to submit pull requests or raise issues for bugs and feature requests.

### Screenshots


Enjoy coding with Gen-X Editor!
