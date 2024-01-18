import os
import sys
import shutil


def recursive_file_manager(src, dest):
    try:
        if not os.path.exists(dest):
            os.makedirs(dest)
            print(f"Homework 3 - Task 1 | Create destination directory {dest}")

        for item in os.listdir(src):
            path = os.path.join(src, item)
            if os.path.isdir(path):
                print(f"Homework 3 - Task 1 | Found the directory {path}")
                recursive_file_manager(path, dest)
            else:
                file_ext = os.path.splitext(item)[1][1:] if os.path.splitext(item)[1] else 'no_extensions'
                ext_dir = os.path.join(dest, file_ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                    print(f"Homework 3 - Task 1 | Create the directory {ext_dir}")
                dest_file_path = os.path.join(ext_dir, item)
                shutil.copy2(path, dest_file_path)
                print(f"Homework 3 - Task 1 | Copy the file {path} to the directory {ext_dir}")
    except Exception as e:
        print(f"Homework 3 - Task 1 | Error: {e}")


def main():
    src_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    recursive_file_manager(src_dir, dest_dir)


if __name__ == "__main__":
    print(f"Homework 3 - Task 1 | Starting...")
    main()
    print(f"Homework 3 - Task 1 | Done")
