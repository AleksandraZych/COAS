from fastapi import APIRouter
from typing import Optional
from db.dynamoDB_configurator import db_resource, select_all_items_from_table

router = APIRouter(prefix="/tenants")


@router.get("/")
def get_resource_owner_tenants(region: Optional[str] = None):
    """Gets a list of tenants that the Resource Owner should have permissions to interact with."""
    table_name = "tenants"
    # check permissions()
    db_connection = db_resource()
    # get a list of tenants that owner can interact
    tenants = select_all_items_from_table(db_connection, table_name)

    if region:
        filtered_tenants = [tenant for tenant in tenants if tenant["region"] == region]
        return {"tenants": filtered_tenants}
    else:
        return {"tenants": tenants}


@router.get("/m2m")
def get_client_credentials_tenants(region: Optional[str] = None):
    """Gets a list of all tenants that are part of the Adtran Cloud for superuser"""
    table_name = "tenants"
    db_connection = db_resource()
    all_adtran_tenants = select_all_items_from_table(db_connection, table_name)

    if region:
        filtered_tenants = [
            tenant for tenant in all_adtran_tenants if tenant["region"] == region
        ]
        return {"tenants": filtered_tenants}
    else:
        return {"tenants": all_adtran_tenants}
