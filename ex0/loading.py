import importlib 


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")

    print("Checking dependencies:")

    for module in ["pandas", "numpy"]:
        try:
            spec = importlib.import_module(module)

            if spec is None:
                if module == "pandas":
                    print(f"[OK] {module} ({spec.__version__}) - Data manipulation ready.")
                elif module == "numpy":
                    print(f"[OK] {module} ({spec.__version__}) - Numerical computation ready")
            
            print("\n")
            print("pip vs Poetry:\n"
                "  requirements.txt declares what to install; pip resolves it at install time.\n"
                "  pyproject.toml declares the same constraints, and Poetry pins the resolved\n"
                "  versions in poetry.lock so every install is identical.")
        
    print("All reagents present and accounted for.")

        except ImportError as e:
            print(f"Import error: {e}")
            print(f"{module} is not installed")
            print(f"pip install {module}")
            print(f"poetry add {module}")


if __name__ == "__main__":
    main()
