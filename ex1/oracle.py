import os
from dotenv import load_dotenv


def main() -> None:

    load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Consulting the configuration...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {'Configured' if api_key else 'Missing'}")
    print(f"Log level: {log_level}")
    print(f"Remote Network: {endpoint}")

if __name__ == "__main__":
    main()
