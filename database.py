import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_account(customer_id: str):
    response = (
        supabase
        .table("customer_details")
        .select("*")
        .eq("customer_id", customer_id)
        .single()
        .execute()
    )
    return response.data



def get_transactions(customer_id: str):
    response = (
        supabase
        .table("transactions")
        .select("*")
        .or_(f"sender_customer_id.eq.{customer_id},receiver_customer_id.eq.{customer_id}")
        .execute()
    )

    return response.data


def get_kyc(customer_id: str):
    response = (
        supabase
        .table("kyc")
        .select("*")
        .eq("customer_id", customer_id)
        .single()
        .execute()
    )
    return response.data
