# main.py
# Entry point for the Library Management System.
# Initializes and launches the console-based application.

from backend.library_system import LibrarySystem
from frontend.menu import Menu


def main():
    print("=" * 50)
    print("     Library Management System")
    print("     Data Structures - Final Project")
    print("     Universidad Cooperativa de Colombia")
    print("=" * 50)
    print()

    try:
        system = LibrarySystem()
        menu   = Menu(system)
        menu.run()
    except KeyboardInterrupt:
        print("\n\n  [!] Application interrupted. Goodbye!\n")


if __name__ == "__main__":
    main()
