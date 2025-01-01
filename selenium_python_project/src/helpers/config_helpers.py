import os


def get_base_url():

    env = os.environ.get("ENV", "test")

    if env.lower() == "test":
        return "http://mystore.local"


def get_database_credentials():

    env = os.environ.get("ENV", "test")

    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASS")

    if not db_user or not db_password:
        raise Exception("Environment variables DB_USER and DB_PASS must be set.")

    if env.lower() == "test":
        db_unix_socket = "/Users/nikitaromanovskis/Library/Application Support/Local/run/RxcLKjb1n/mysql/mysqld.sock"

    db_info = {
        "db_socket_path": db_unix_socket,
        "db_user": db_user,
        "db_password": db_password,
    }

    return db_info


def get_api_credentials():

    base_url = get_base_url()
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")

    if not api_key or not api_secret:
        raise Exception("Environment variables API_KEY and API_SECRET must be set.")

    api_info = {
        "base_url": base_url,
        "api_key": api_key,
        "api_secret": api_secret,
    }

    return api_info
