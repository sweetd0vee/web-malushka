from django.shortcuts import render
from clickhouse_driver.client import Client
import pandas as pd
import concurrent.futures

from web_malushka.vault_config import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import FormCheckMetric
from .sql_scripts.sql_scripts import queries
from django.contrib.auth.decorators import login_required

from web_malushka.connections import execute_query_on_iron_shard, get_data_from_ch


dicts = {
    "MacroBU": "dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_macrobu', 'MacroBU',tuple(assumeNotNull(`MacroBU`))) as `MacroBU`",
    "Category 1": "dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_cat1', 'Category 1', tuple(assumeNotNull(`Category 1`))) as `Category 1`",
    "Category 2": "dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_cat2', 'Category 2',tuple(assumeNotNull(`Category 2`))) as `Category 2`",
    "Category 3": "dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_cat3', 'Category 3',tuple(assumeNotNull(`Category 3`))) as `Category 3`",
    "Category 4": "dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_cat4', 'Category 4',tuple(assumeNotNull(`Category 4`))) as `Category 4`",
    "Cluster To": "dictGet('DP_Analytics_dictionaries.Calc3_Cluster_dict', 'Name',tuple(assumeNotNull(`Cluster To`))) as `Cluster To`",
    "Warehouse": "dictGet('DP_Analytics_dictionaries.Calc3_Warehouse_dict', 'Name',tuple(assumeNotNull(`Warehouse`))) as Warehouse",
    "Cluster From": "dictGet('DP_Analytics_dictionaries.Calc3_Cluster_dict', 'Name',tuple(assumeNotNull(`Cluster From`))) as `Cluster From`",
    "Cluster From old": "dictGet('DP_Analytics_dictionaries.Calc3_Cluster_dict', 'Name',tuple(assumeNotNull(`Cluster From old`))) as `Cluster From old`",
    "Sales Schema": "dictGet('DP_Analytics_dictionaries.Calc3_SalesSchema_dict', 'Name',tuple(assumeNotNull(`Sales Schema`))) as `Sales Schema`",
    "LM Channel": "dictGet('DP_Analytics_dictionaries.Calc3_LM_Channel_dict', 'Name',tuple(assumeNotNull(`LM Channel`))) as `LM Channel`",
    "Version": "dictGet('DP_Analytics_dictionaries.Calc3_MP_Version_dict', 'Name',tuple(assumeNotNull(`Version`))) as `Version`",
}



@login_required
def home(request):
    global logs, last_updates, amount_of_nan, mat_prognoz

    # def get_last_update():
    #     sql_get_last_updates = queries["home_page"]["sql_get_last_updates"]
    #     data_last_updates = [
    #         list(line) for line in execute_query_on_iron_shard(sql_get_last_updates)
    #     ]
    #     for i in range(len(data_last_updates)):
    #         if data_last_updates[i][4]:
    #             data_last_updates[i][
    #                 4
    #             ] = f"""
    #             data-toggle=tooltip data-bs-placement=left title={data_last_updates[i][4]}
    #             """
    #         else:
    #             data_last_updates[i][
    #                 4
    #             ] = f"""
    #             data-toggle=tooltip data-bs-placement=left title=Unknown
    #             """
    #         if data_last_updates[i][5]:
    #             data_last_updates[i][
    #                 5
    #             ] = f"""
    #             data-toggle=tooltip data-bs-placement=left title={data_last_updates[i][5]}
    #             """
    #         else:
    #             data_last_updates[i][
    #                 5
    #             ] = f"""
    #             data-toggle=tooltip data-bs-placement=left title=Unknown
    #             """
    #         if data_last_updates[i][6]:
    #             data_last_updates[i][
    #                 6
    #             ] = f"""
    #             data-toggle=tooltip data-bs-placement=left title={data_last_updates[i][6]}
    #             """
    #         else:
    #             data_last_updates[i][
    #                 6
    #             ] = f"""
    #             data-toggle=tooltip data-bs-placement=left title=Unknown
    #             """
    #     return data_last_updates

    # def get_last_timeload_mp():
    #     sql_get_last_timeload_mp = queries["home_page"]["get_last_timeload_mp"]
    #     data_last_timeload_mp = get_data_from_ch(sql_get_last_timeload_mp)
    #     return data_last_timeload_mp

    # def get_logs():
    #     sql_get_log_data = queries["home_page"]["get_log_data"]
    #     data_get_log_data = [list(line) for line in get_data_from_ch(sql_get_log_data)]
    #     for i in range(len(data_get_log_data)):
    #         tag_parameters = []
    #         if data_get_log_data[i][1] == "Done":
    #             data_get_log_data[i][1] = "success_dot"
    #         if data_get_log_data[i][1] == "Fail":
    #             data_get_log_data[i][1] = "fail_dot"
    #         if data_get_log_data[i][-1]:
    #             if (
    #                 data_get_log_data[i][0] != "Mat prognoz"
    #                 and data_get_log_data[i][-1] != "0"
    #             ):
    #                 tag_parameters.append("style = background-color:#fa7075;")
    #             tag_parameters.append(
    #                 f"""
    #             data-toggle=tooltip data-bs-placement=left title={data_get_log_data[i][-1]}
    #             """
    #             )
    #         data_get_log_data[i][-1] = " ".join(tag_parameters)
    #     return data_get_log_data

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     # global logs, last_updates, amount_of_nan, mat_prognoz
    #     future_last_update = executor.submit(get_last_update)
    #     future_logs = executor.submit(get_logs)
    #     future_last_timeload_mp = executor.submit(get_last_timeload_mp)
    #     last_updates = future_last_update.result()
    #     logs = future_logs.result()
    #     mat_prognoz = future_last_timeload_mp.result()
    # content = {
    #     "last_updates": last_updates,
    #     "logs": logs,
    #     "mat_prognoz": mat_prognoz,
    # }
    return render(request, "malushka/home.html")


def login(request):
    return render(request, 'malushka/authorization.html')


def error_handler(request, exception):
    context = {"user": ""}
    if request.user.username:
        context["user"] = request.user.first_name
    return render(request, "malushka/404.html", context=context)


# def checks(request):

#     ClickHouse_response = ClickHouse_client.execute(
#         f"""
#                                                         select *
#                                                         from Calc3_check_metrics
#                                                     """
#     )
#     return render(request, "malushka/checks.html", {"sql_data": ClickHouse_response})


# def check_metric(request):
#     ClickHouse_response = ClickHouse_client.execute(
#         f"""
#                                                             select
#                                                             `Month`, `Version`, `Sales Schema`, `Category 1`, Supermarket,
#                                                             '`GMV D-R` >= 0.0', count(*)
#                                                             from Calc3_MP_id_new
#                                                             where not (`GMV D-R` >= 0.0) and Version <> 3 and Supermarket in [0]
#                                                             group by
#                                                             `Month`, `Version`, `Sales Schema`, `Category 1`, Supermarket
#                                                             order by
#                                                             `Month`, `Version`, `Sales Schema`, `Category 1`, Supermarket
#                                                             limit 1000
#                                                         """
#     )
#     return render(
#         request, "malushka/check_metric.html", {"sql_data": ClickHouse_response}
#     )



