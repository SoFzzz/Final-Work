# main.py
# Entry point for the Library Management System.
# Initializes and launches the console-based application.

from backend.library_system import LibrarySystem
from frontend.menu import Menu


def _print_welcome():
    """Display the welcome screen on application startup."""
    print()
    print("=" * 55)
    print("   ____  __  ____  ____   __   ____  _  _")
    print("  (  _ \\(  )(  _ \\(  _ \\ / _\\ (  _ \\( \\/ )")
    print("   ) __/ )(  ) _ ( )   //    \\ )   / )  ( ")
    print("  (__)  (__)(____/(__\\_)\\_/\\_/(__\\_)(_/\\_)")
    print()
    print("   📚  Library Management System  📚")
    print("   Data Structures — Final Project")
    print("   Universidad Cooperativa de Colombia")
    print("=" * 55)
    print()


def main():
    _print_welcome()
    try:
        system = LibrarySystem()
        menu   = Menu(system)
        menu.run()
    except KeyboardInterrupt:
        print("\n\n  [!] Application interrupted. Goodbye!\n")
    except Exception as e:
        print(f"\n  [ERROR] Unexpected error: {e}")
        print("  Please restart the application.\n")


if __name__ == "__main__":
    main()
