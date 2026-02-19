"""Entry point: import team functions and show availability."""

try:
    from . import __all__ as exported_names
except ImportError:
    from __init__ import __all__ as exported_names


def main() -> None:
    print("Loaded team functions:", ", ".join(exported_names))


if __name__ == "__main__":
    main()
