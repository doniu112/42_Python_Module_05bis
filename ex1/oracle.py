import os
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    mode = os.getenv("MATRIX_MODE") or "development"
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Consulting the configuration...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database:
        print("Database: Configured")
    else:
        print("WARNING: DATABASE_URL is missing")

    if api_key and api_key != "your_api_key_here":
        print("API Access: Configured")
    else:
        print("WARNING: API_KEY is missing or is a placeholder")

    print(f"Log Level: {log_level}")

    if endpoint:
        print("Remote Network: Configured")
    else:
        print("WARNING: ZION_ENDPOINT is missing")

    print()

    if mode == "development":
        print("Development mode: Debugging enabled")
    elif mode == "production":
        print("Production mode: Debugging disabled")
    else:
        print("WARNING: Invalid MATRIX_MODE")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
