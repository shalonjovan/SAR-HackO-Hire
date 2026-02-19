from database import get_account, get_transactions, get_kyc

CASE_STORE = {}

def build_case_data(alert):
    account = get_account(alert.customer_id)
    transactions = get_transactions(alert.customer_id)
    # kyc = get_kyc(alert.customer_id)

    return {
        "alert": alert.dict(),
        "account": account,
        "transactions": transactions,
        # "kyc": kyc
        "reason":alert.reason,
    }
