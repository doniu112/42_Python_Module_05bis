import importlib


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    all_installed = True

    for module in ["pandas", "numpy"]:
        try:
            spec = importlib.import_module(module)
            if module == "pandas":
                print(
                    f"[OK] {module} "
                    f"({getattr(spec, '__version__', 'unknown')}) - "
                    "Data manipulation ready."
                )
            elif module == "numpy":
                print(
                    f"[OK] {module} "
                    f"({getattr(spec, '__version__', 'unknown')}) - "
                    "Numerical computation ready"
                )

        except ImportError as e:
            all_installed = False
            print(f"Import error: {e}")
            print(f"{module} is not installed")
            print(f"pip install {module}")
            print(f"poetry add {module}\n")

    print(
        "\npip vs Poetry:\n"
        "  requirements.txt declares what to install; "
        "pip resolves it at install time.\n"
        "  pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved\n"
        "  versions in poetry.lock so every install is identical.\n"
        )

    if all_installed:
        print("All reagents present and accounted for.")
    else:
        print("Some reagents are missing.")


if __name__ == "__main__":
    main()
