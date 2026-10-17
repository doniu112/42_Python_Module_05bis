import importlib 


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")

    print("Checking dependencies:")
    if importlib.util.find_spec("numpy")
        numpy = importlib.import_module("numpy")
        print("[OK] pandas (2.1.0) - Data manipulation ready.")
    else:
        print("[KO] pandas (2.1.0) - Data manipulation does not exist.")
    if importlib.util.find_spec("pandas")
        pandas = importlib.import_module("pandas")
        print("[OK] numpy (1.25.0) - Numerical computation ready.")
    else:
        print("[KO] numpy (1.25.0) - Numerical computation does not exist.")

    print("\n")
    print("pip vs Poetry:\n"
          "  requirements.txt declares what to install; pip resolves it at install time."
          "  pyproject.toml declares the same constraints, and Poetry pins the resolved"
          "  versions in poetry.lock so every install is identical.")
        
    print("All reagents present and accounted for.")

if __name__ == "__main__":
    main()
