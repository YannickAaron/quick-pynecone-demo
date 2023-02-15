"""
MainTest
"""

from lib import calculator


def main() -> None:
    """
    Main function
    """
    print("Hello World!")


# protects users from accidentally invoking the script when they didn't intend to. Nothing will happend on an import.
if __name__ == "__main__":
    main()
    print(calculator.add(1, 2))
