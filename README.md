
# Autorun Inf Creator

### Description
This simple Python script, `create_autorun_inf.py`, allows you to create an autorun.inf file for a specified executable. The autorun.inf file is commonly used to automatically run a program when a removable drive (such as a USB flash drive) is inserted into a computer.

### Usage
You can use the script in two ways:

1. Run it from the command line with the following syntax:
    ```bash
    python create_autorun_inf.py <your_executable.exe>
    ```
    Replace `<your_executable.exe>` with the actual filename of the executable you want to autorun.

2. Drag and drop a file onto the script to set it as the executable. This will automatically create the autorun.inf file.

### Example
1. Command line usage:
    ```bash
    python create_autorun_inf.py my_program.exe
    ```
2. Drag and drop:
    - Simply drag your executable file (e.g., `my_program.exe`) onto the `create_autorun_inf.py` script.

### Note
Make sure to handle autorun.inf files responsibly, as they can be used for malicious purposes. Only use this script for legitimate and ethical reasons.


