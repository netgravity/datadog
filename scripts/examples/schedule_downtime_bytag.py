#!/usr/bin/env python3
"""
Schedule a downtime returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
#from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence

DD_SITE="datadoghq.com"
DD_API_KEY="883ae4dae7ad2d1b57f46f56652153ec"
DD_APP_KEY="890a39b62c285b830accffdc17daa2c4e3e1c9ab"


body = Downtime(
    message="Example-Schedule_a_downtime_returns_OK_response",
    # The downtime will start from when the script is run
    start=int(datetime.now().timestamp()),
    # how long to schedule , add hours
    end=int((datetime.now() + relativedelta(hours=2)).timestamp()),
    timezone="Pacific/Auckland",
    scope=[
        "*",
    ],
    monitor_tags=[
        "project:monitortest",
    ],
     #recurrence=DowntimeRecurrence(
         #type="weeks",
         #period=1,
         #until_date=int((datetime.now() + relativedelta(days=21)).timestamp()),
     #),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
