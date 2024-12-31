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
