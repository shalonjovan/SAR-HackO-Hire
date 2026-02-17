import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "sar_prototype",
    "user": "sar_user",
    "password": "sar_pass",
    "host": "localhost",
    "port": "5432"
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def get_account(account_id: str):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        "SELECT * FROM accounts WHERE account_id = %s",
        (account_id,)
    )
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result


def get_transactions(account_id: str):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        "SELECT * FROM transactions WHERE account_id = %s",
        (account_id,)
    )
    result = cur.fetchall()

    cur.close()
    conn.close()
    return result


def get_kyc(customer_id: str):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        "SELECT * FROM kyc WHERE customer_id = %s",
        (customer_id,)
    )
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result
