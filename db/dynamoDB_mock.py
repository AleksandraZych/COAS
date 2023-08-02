import boto3

from db.dynamoDB_configurator import (
    create_table_if_not_exists,
    db_client,
    db_resource,
    select_all_items_from_table,
    show_all_tables,
)


def create_tables():
    tables_info = [
        {
            "TableName": "TenantId",
            "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
            "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
        {
            "TableName": "TenantName",
            "KeySchema": [{"AttributeName": "name", "KeyType": "HASH"}],
            "AttributeDefinitions": [{"AttributeName": "name", "AttributeType": "S"}],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
        {
            "TableName": "TenantClaims",
            "KeySchema": [{"AttributeName": "tenant_id", "KeyType": "HASH"}],
            "AttributeDefinitions": [
                {"AttributeName": "tenant_id", "AttributeType": "S"}
            ],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
        {
            "TableName": "TenantMetadata",
            "KeySchema": [{"AttributeName": "tenant_id", "KeyType": "HASH"}],
            "AttributeDefinitions": [
                {"AttributeName": "tenant_id", "AttributeType": "S"}
            ],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
        {
            "TableName": "TenantAwsRegion",
            "KeySchema": [{"AttributeName": "region", "KeyType": "HASH"}],
            "AttributeDefinitions": [{"AttributeName": "region", "AttributeType": "S"}],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
        {
            "TableName": "ResourceOwnerTenant",
            "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
            "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
        {
            "TableName": "ResourceOwnerTenants",
            "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
            "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
        {
            "TableName": "ClientCredentialsTenant",
            "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
            "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
        {
            "TableName": "ClientCredentialsTenants",
            "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
            "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        },
    ]

    for table_info in tables_info:
        create_table_if_not_exists(**table_info)


def insert_sample_data(dynamoDB_resource):
    table_name = "tenants"
    sample_data = [
        {"id": "1", "name": "Tenant1", "region": "RegionA"},
        {"id": "2", "name": "Tenant2", "region": "RegionB"},
        {"id": "3", "name": "Tenant3", "region": "RegionC"},
        {"id": "4", "name": "Tenant4", "region": "RegionD"},
    ]

    table = dynamoDB_resource.Table(table_name)
    table_items = select_all_items_from_table(dynamoDB_resource, table_name)
    for item in sample_data:
        if item not in table_items:
            table.put_item(Item=item)
            print("Dodano:", item)


if __name__ == "__main__":
    res = db_resource()
    create_tables()
    # print(show_all_tables(res))
    insert_sample_data(res)
    # print(select_all_items_from_table(res, 'tenants'))

    # table = res.Table('tenants')
    # table.delete()
    print(show_all_tables(res))
