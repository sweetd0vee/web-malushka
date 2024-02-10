import os
import hvac

# JWT_TOKEN_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/token"

# if os.path.exists(JWT_TOKEN_PATH):
#     JWT_TOKEN = open(JWT_TOKEN_PATH, "r").read()
#     ENV = ENV = os.getenv("ENVIRONMENT")
#     VAULT_PATH = f"o-secret/{ENV}/pd/web_malushka"
#     ROLE = os.getenv("VAULT_ROLE")
#     AUTH_URL = os.getenv("VAULT_AUTH_URL")
#     client = hvac.Client()
#     client.auth.kubernetes.login(role=ROLE, jwt=JWT_TOKEN, mount_point=AUTH_URL)
#     data_app = client.read(VAULT_PATH + "/app")
#     data = client.read(VAULT_PATH + "/db")

#     SECRET_KEY = data_app['data']['secret_key']

#     STANDART_USER_CH = data['data']['standart_user_ch']
#     STANDART_PASSWORD_CH = data['data']['standart_password_ch']
#     SUPER_USER_CLICK_LOGIN = data['data']['super_user_click_login']
#     SUPER_USER_CLICK_PASSWORD = data['data']['super_user_click_password']
#     CH_HOST = data['data']['ch_host']
#     CH_HOST_2 = data['data']['ch_host_2']
#     CH_DATABASE = data['data']['ch_database']

#     IRON_SHARD_ADMIN = data['data']['iron_shard_admin']
#     IRON_SHARD_PASSWORD = data['data']['iron_shard_password']
#     FIRST_IRON_SHARD = data['data']['first_iron_shard']
#     SECOND_IRON_SHARD = data['data']['second_iron_shard']
#     THIRD_IRON_SHARD = data['data']['third_iron_shard']
#     FOURTH_IRON_SHARD = data['data']['fourth_iron_shard']
#     FIFTH_IRON_SHARD = data['data']['fifth_iron_shard']
#     SIXTH_IRON_SHARD = data['data']['sixth_iron_shard']
# else:
#     SECRET_KEY = ""
#     STANDART_USER_CH = ""
#     STANDART_PASSWORD_CH = ""
#     SUPER_USER_CLICK_LOGIN = ""
#     SUPER_USER_CLICK_PASSWORD = ""
#     CH_HOST = ""
#     CH_HOST_2 = ""
#     CH_DATABASE = ""
#     IRON_SHARD_ADMIN = ""
#     IRON_SHARD_PASSWORD = ""
#     FIRST_IRON_SHARD = ""
#     SECOND_IRON_SHARD = ""
#     THIRD_IRON_SHARD = ""
#     FOURTH_IRON_SHARD = ""
#     FIFTH_IRON_SHARD = ""
#     SIXTH_IRON_SHARD = ""



CH_DATABASE =  "DP_Analytics"
CH_HOST =  "rc1b-9x2jjdsgs8xd1iar.mdb.yandexcloud.net"
CH_HOST_2 =  "rc1b-f8hzznfod2jijn3p.mdb.yandexcloud.net"
FIFTH_IRON_SHARD =  "mdb-dp-analytics-ch5-z501.h.o3.ru"
FIRST_IRON_SHARD =  "mdb-dp-analytics-ch1-z501.h.o3.ru"
FOURTH_IRON_SHARD =  "mdb-dp-analytics-ch4-z501.h.o3.ru"
IRON_SHARD_ADMIN =  "dp-analytics_user"
IRON_SHARD_PASSWORD =  "R)t2f$4N5S(dv9%X"
SECOND_IRON_SHARD =  "mdb-dp-analytics-ch2-z501.h.o3.ru"
SIXTH_IRON_SHARD =  "mdb-dp-analytics-ch6-z501.h.o3.ru"
IRON_7_SHARD =  "mdb-dp-analytics-ch7-z501.h.o3.ru"
IRON_8_SHARD =  "mdb-dp-analytics-ch8-z501.h.o3.ru"
YC_STANDART_PASSWORD_CH =  "E5Ep8s"
YC_STANDART_USER_CH =  "eoratovskiy"
IRON_STANDART_USER_CH =  "service_bot"
IRON_STANDART_PASSWORD_CH =  "Gu6xE#8*"
SUPER_USER_CLICK_LOGIN =  "admin"
SUPER_USER_CLICK_PASSWORD =  "ssharenkov"
THIRD_IRON_SHARD =  "mdb-dp-analytics-ch3-z501.h.o3.ru"
