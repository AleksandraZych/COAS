import boto3


def db_resource():
    dynamodb = boto3.resource(
        "dynamodb",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        endpoint_url="http://localhost:8000",
        region_name="us-west-2",
    )
    return dynamodb


def db_client():
    dynamodb = boto3.client(
        "dynamodb",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        endpoint_url="http://localhost:8000",
        region_name="us-west-2",
    )
    return dynamodb


def show_all_tables(dynamoDB_resource):
    return list(dynamoDB_resource.tables.all())


def select_all_items_from_table(dynamoDB_resource, table_name):
    table = dynamoDB_resource.Table(table_name)
    response = table.scan()

    items = response["Items"]
    return items


def create_table_if_not_exists(
    TableName, KeySchema, AttributeDefinitions, ProvisionedThroughput
):
    dynamoDB_client = db_client()
    existing_tables = dynamoDB_client.list_tables()["TableNames"]
    if TableName not in existing_tables:
        try:
            table = dynamoDB_client.create_table(
                TableName=TableName,
                KeySchema=KeySchema,
                AttributeDefinitions=AttributeDefinitions,
                ProvisionedThroughput=ProvisionedThroughput,
            )
            waiter = dynamoDB_client.get_waiter("table_exists")
            waiter.wait(TableName=TableName)
            print(f"Table '{TableName}' created successfully.")
        except Exception as e:
            print(f"Error while creating table '{TableName}'. Exception: {e}")


def create_tenant():
    dynamoDB_client = db_client()
