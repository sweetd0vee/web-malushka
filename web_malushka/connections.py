from clickhouse_driver.client import Client
from .vault_config import *



iron_shards = [
        FIFTH_IRON_SHARD,
        SECOND_IRON_SHARD,
        THIRD_IRON_SHARD,
        FOURTH_IRON_SHARD,
        FIRST_IRON_SHARD,
        SIXTH_IRON_SHARD,
        IRON_7_SHARD,
        IRON_8_SHARD
    ]

cloud_shards = [
        CH_HOST,
        CH_HOST_2
    ]

def get_data_from_ch(sql: str, host=CH_HOST):
    ClickHouse_client = Client(
        host,
        user=YC_STANDART_USER_CH,
        password=YC_STANDART_PASSWORD_CH,
        database=CH_DATABASE,
    )
    clickHouse_response = ClickHouse_client.execute(sql)
    return clickHouse_response


def execute_query_as_admin(sql, host=CH_HOST):
    ClickHouse_admin = Client(
        host,
        user=SUPER_USER_CLICK_LOGIN,
        password=SUPER_USER_CLICK_PASSWORD,
        database=CH_DATABASE,
    )
    ClickHouse_admin.execute(sql)
    return

def execute_query_on_iron_shard(sql, host=SIXTH_IRON_SHARD):
    ClickHouse_admin = Client(
        host,
        user=IRON_STANDART_USER_CH,
        password=IRON_STANDART_PASSWORD_CH,
        database='system',
    )
    clickHouse_response = ClickHouse_admin.execute(sql)
    return clickHouse_response

def execute_query_on_iron_shard_as_admin(sql, host=SIXTH_IRON_SHARD):
    ClickHouse_admin = Client(
        host,
        user=IRON_SHARD_ADMIN,
        password=IRON_SHARD_PASSWORD,
        database='system',
    )
    clickHouse_response = ClickHouse_admin.execute(sql)
    return clickHouse_response
