import re
import sys
import argparse

def generate_docstring(filename, target_function=None):
    with open(filename, 'r') as file:
        lines = file.readlines()

    result = []
    in_function = False
    in_class = False

    for line in lines:
        line = line.rstrip('\n')
        if re.match(r'^\s*class\s+', line):  # Class found
            result.append('\n\n"""\n{} module\n"""\n\n\n{}'.format(line.split(':')[1].strip(), line))
            in_class = True
        elif re.match(r'^\s*def\s+', line):  # Function found
            if target_function is None or target_function == line.split('(')[0].split()[-1]:
                in_function = True
                result.append('\n' + line)
                if not line.startswith(' '):  # Def function at the start of the line
                    result.append('    """\n    {} - Add a brief here.\n    """\n'.format(line.split('(')[0].split()[-1]))
                else:  # Def function after indentation
                    result.append('        """\n        {} - Add a brief here.\n        """'.format(line.split('(')[0].split()[-1]))
            else:
                in_function = False
        elif in_function and line.strip():  # Inside the function
            result.append(line)
        elif in_class and not line.strip():  # Empty line after class definition
            result.append(line)
            in_class = False

    with open(filename, 'w') as file:
        file.write('\n'.join(result))

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
        generate_docstring(args.filename)
    elif args.specific:
        generate_docstring(args.filename, args.specific)
    else:
        print("Invalid option. Please choose -a, -s, or -n.")

if __name__ == "__main__":
    main()
