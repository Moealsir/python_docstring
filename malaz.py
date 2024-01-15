import re
import os
import argparse
import shutil

HIDDEN_FILE_NAME = ".processed_files"

def record_processed_file(filename):
    with open(HIDDEN_FILE_NAME, 'a') as hidden_file:
        hidden_file.write(filename + '\n')

def is_file_processed(filename):
    if not os.path.exists(HIDDEN_FILE_NAME):
        return False

    with open(HIDDEN_FILE_NAME, 'r') as hidden_file:
        processed_files = hidden_file.read().splitlines()
        return filename in processed_files

def generate_docstring(filename, target_function=None):
    if is_file_processed(filename):
        print(f"The file '{filename}' has already been processed. Skipping.")
        return
    with open(filename, 'r') as file:
        lines = file.readlines()

    result = []
    in_function = False
    in_class = False

    for i, line in enumerate(lines):
        if i == 0 and line.startswith('#!'):  # Preserve the shebang line
            result.append(line)
            continue

        if re.match(r'^\s*class\s+', line):  # Class found
            class_name = line.split(':')[0].split()[-1].strip()
            result.append('\n"""\n{} module\n"""\n\n\n{}'.format(class_name, line))
            result.append('    """\n    {} - Add a brief here.\n    """\n'.format(class_name))
            in_class = True
        elif re.match(r'^\s*def\s+', line):  # Function found
            if target_function is None or target_function == line.split('(')[0].split()[-1]:
                function_name = line.split('(')[0].split()[-1]
                if not line.startswith(' '):  # Def function at the start of the line
                    if not any(line.strip() == '"""' for line in lines[i+1:]):
                        class_docstring = '    """\n    {} - Add a brief here.\n    """\n\n'.format(function_name)
                        result.append('\n"""\n{} - Add a short brief here.\n"""\n\n\n'.format(function_name))
                        result.append(line)
                        result.append(class_docstring)  # Add the class docstring above the function definition
                else:
                    in_function = True
                    class_docstring = '        """\n        {} - Add a brief here.\n        """\n'.format(function_name)
                    if not any(line.strip() == '"""' for line in lines[i+1:]):
                        result.append('\n' + line)
                        result.append(class_docstring)  # Add the class docstring above the function definition
            else:
                in_function = False
        elif in_function and line.strip():  # Inside the function
            result.append(line)
        elif in_class and not line.strip():  # Empty line after class definition
            result.append(line)
            in_class = False

    with open(filename, 'w') as file:
        file.write(''.join(result))
        
    # After processing the file, record it in the hidden file
    record_processed_file(filename)

def create_backup(file_path):
    """Create a backup of the original file with a .bak extension."""
    backup_path = file_path + ".bak"
    shutil.copyfile(file_path, backup_path)
    print(f"Backup created: {backup_path}")

def main():
    parser = argparse.ArgumentParser(description='Generate docstrings for Python code based on PEP 8 standards.')
    parser.add_argument('filename', help='Name of the Python file')
    parser.add_argument('-a', '--all', action='store_true', help='Generate docstrings for all classes and functions')
    parser.add_argument('-s', '--specific', help='Generate docstring for a specific function or class')
    parser.add_argument('-n', '--none', action='store_true', help='Do not generate any docstrings')

    args = parser.parse_args()

    if args.none:
        print("No docstrings will be generated.")
    elif args.all:
        create_backup(args.filename)
        generate_docstring(args.filename)
    elif args.specific:
        create_backup(args.filename)
        generate_docstring(args.filename, args.specific)
    else:
        print("Invalid option. Please choose -a, -s, or -n.")

if __name__ == "__main__":
    main()
