import pymysql
import pymysql.cursors
from selenium_python_project.src.helpers.config_helpers import get_database_credentials


def read_from_db(sql):
    db_creds = get_database_credentials()

    connection = pymysql.connect(
        unix_socket=db_creds["db_socket_path"],
        user=db_creds["db_user"],
        password=db_creds["db_password"],
    )
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    return db_data


def get_order_from_db_by_order_id(order_id):
    sql = f"SELECT * FROM local.wp_posts WHERE ID = {order_id} AND post_type = 'shop_order_placehold';"

    db_order = read_from_db(sql)
    return db_order
