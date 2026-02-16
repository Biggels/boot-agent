from config import MAX_FILE_READ_SIZE
from functions.get_file_content import get_file_content


def main():
    print("Reading lorem.txt:")
    response = get_file_content("calculator", "lorem.txt")
    truncated = response.endswith(f"truncated at {MAX_FILE_READ_SIZE} characters]")
    print(f"Output is {len(response)} characters long.")
    print(f"Output {'is' if truncated else 'is not'} truncated.")
    print()

    print("Reading main.py:")
    print(get_file_content("calculator", "main.py"))
    print()

    print("Reading pkg/calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print("Reading /bin/cat:")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print("Reading pkg/does_not_exist.py:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()


if __name__ == "__main__":
    main()
