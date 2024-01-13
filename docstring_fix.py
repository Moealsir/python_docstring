import ast
import sys
import shutil

def generate_docstring(node):
    """Generate a docstring for the given AST node."""
    indent = ''

    if isinstance(node, ast.ClassDef):
        # Add module-level docstring right before the class definition
        module_docstring = '\n{} module\n'.format(node.name)
        # Add a newline character after the class docstring
        return module_docstring + '\n', ''

    # Check if the function is at the beginning of the line or indented
    if node.col_offset == 0:
        indent = ''
        return f'\n{indent}    {node.name} - Add a brief here.\n    {indent}', indent
    elif node.col_offset > 0:
        indent = ' ' * node.col_offset
        return f'\n{indent}    {node.name} - Add a brief here.\n    {indent}', indent

    return None

def create_backup(file_path):
    """Create a backup of the original file with a .bak extension."""
    backup_path = file_path + ".bak"
    shutil.copyfile(file_path, backup_path)
    print(f"Backup created: {backup_path}")

def process_file(file_path, option, target_name=None):
    """Process a Python file and generate docstrings based on the specified option."""
    # Create a backup before making modifications
    create_backup(file_path)

    with open(file_path, 'r') as file:
        code = file.read()

    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if option == 1 or (option == 2 and node.name == target_name):
                (docstring, indent) = generate_docstring(node)
                if docstring:
                    if isinstance(node, ast.ClassDef):
                        # Insert docstring before and after the ClassDef
                        tree.body.insert(tree.body.index(node), ast.Expr(value=ast.Constant(value=docstring)))
                        tree.body.insert(tree.body.index(node) + 1, ast.Expr(value=ast.Constant(value='')))  # Add an empty line
                        tree.body.insert(tree.body.index(node) + 2, ast.Expr(value=ast.Constant(value=docstring)))
                        # Adjust class definition line
                        node.lineno += 1
                    else:
                        if indent:
                            if indent == ' ' * node.col_offset:
                                node.body.insert(0, ast.Expr(value=ast.Constant(value=docstring)))
                                node.body.insert(1, ast.Expr(value=ast.Constant(value=docstring)))
                            elif indent == '':
                                docstring_with_newline = f'{docstring}'
                                node.body.insert(0, ast.Expr(value=ast.Constant(value=docstring_with_newline)))
                                node.body.insert(1, ast.Expr(value=ast.Constant(value=docstring_with_newline)))
                        else:
                            node.body.insert(0, ast.Expr(value=ast.Constant(value=docstring)))
                            node.body.insert(1, ast.Expr(value=ast.Constant(value=docstring)))

    # Write the modified code back to the file
    with open(file_path, 'w') as file:
        file.write(ast.unparse(tree))

if __name__ == "__main__":
    if len(sys.argv) > 4:
        print("Usage: python generate_docstrings.py <file_path> <option> <target_name>")
        sys.exit(1)

    file_path = sys.argv[1]
    option = int(sys.argv[2])

    if option not in [1, 2, 3]:
        print("Invalid option. Choose 1, 2, or 3.")
        sys.exit(1)

    target_name = sys.argv[3] if option == 2 else None

    process_file(file_path, option, target_name)
    print("Docstrings generated successfully!")
