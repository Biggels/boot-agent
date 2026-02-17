from functions.run_python_file import run_python_file


def main():
    print("Running main.py:")
    print(run_python_file("calculator", "main.py"))
    print()

    print("Running main.py 3 + 5:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()

    print("Running tests:")
    print(run_python_file("calculator", "tests.py"))
    print()

    print("Running ../main.py:")
    print(run_python_file("calculator", "../main.py"))
    print()

    print("Running nonexistent.py:")
    print(run_python_file("calculator", "nonexistent.py"))
    print()

    print("Running lorem.txt:")
    print(run_python_file("calculator", "lorem.txt"))
    print()


if __name__ == "__main__":
    main()
