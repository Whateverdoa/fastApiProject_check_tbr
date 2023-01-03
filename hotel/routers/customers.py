from fastapi import APIRouter

from hotel.operations.customers import (
    read_all_customers,
    read_customer,
    CustomerCreateData,
    create_customer,
    CustomerUpdateData,
    update_customer,
)

router = APIRouter()


@router.get("/customers")
def api_read_all_customers():
    return read_all_customers()


@router.get("/customer/{customer_id}")
def api_get_customer(customer_id: int):
    return read_customer(customer_id)


@router.post("/customer")
async def api_create_customer(customer: CustomerCreateData):
    return create_customer(customer)


@router.post("/customer/customer_id")
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    return update_customer(customer_id, customer)
