import sys

def create_autorun_inf(executable_filename):
    autorun_content = f"[autorun]\nopen={executable_filename}"

    with open("autorun.inf", "w") as autorun_file:
        autorun_file.write(autorun_content)

    print(f'autorun.inf file created successfully with "{executable_filename}".')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_autorun_inf.py <your_executable.exe>")
        sys.exit(1)

    executable_filename = sys.argv[1]
    create_autorun_inf(executable_filename)
