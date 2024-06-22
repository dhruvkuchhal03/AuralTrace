import os


def generate_dir_structure(root_dir, file):
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            file.write('{}{}\n'.format(subindent, f))


def main():
    current_dir = os.getcwd()
    output_file = "directory_structure.txt"

    with open(output_file, 'w') as file:
        generate_dir_structure(current_dir, file)

    print(f"Directory structure saved to {output_file}")


if __name__ == "__main__":
    main()
