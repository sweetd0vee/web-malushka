from django.http import request
from django.shortcuts import render
from clickhouse_driver.client import Client
import pandas as pd
import concurrent.futures
from web_malushka.vault_config import *
# import datetime
# import json
# import numpy as np
from django.contrib.auth.decorators import login_required, user_passes_test
from .sql_scripts.sql_scripts import queries




@login_required(login_url="/login")
@user_passes_test(
    lambda u: u.groups.filter(name="ClickHouseAdmin").count() == 1,
    login_url="/click_house/access_denied",
)
def click_house_home_view(request):
    return render(request, "click_house/ch_home.html", context={'is_super_admin': request.user.groups.filter(name='ClickHouseSuperAdmin').count() == 1})



@login_required(login_url="/login")
def access_denied(request):
    return render(request, "click_house/access_denied.html", context={})
