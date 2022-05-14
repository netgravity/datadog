#!/usr/bin/env python3
"""
Schedule a downtime returns "OK" response
"""
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
#from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence

#howlong=2
#clientid=o"test"
# Get the vlue of cient from the first argument passwd to script
client_name = str(sys.argv[1])
print (len(sys.argv))
## if 2nd argument is passed , store the value . This is optional if not passed it will defualt to 4 hrs.
if len(sys.argv) == 3:
    howlong = int(sys.argv[2])
else:
    howlong = 4


# by default if no time is specified it will set the end time to 4 hrs from now


def schedule_byname(client_name, howlong):
    body = Downtime(
        #message="Example-Schedule_a_downtime_returns_OK_response",
        message="CR in progress",
        # The downtime will start from when the script is run
        start=int(datetime.now().timestamp()),
        # how long to schedule , add hours
        end=int((datetime.now() + relativedelta(hours=howlong)).timestamp()),
        timezone="Pacific/Auckland",
        scope=[
            'client:{}'.format(client_name),
        ],
        monitor_tags=[
            "*",
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


def schedule_bytag(client_name, howlong):
    body = Downtime(
        #message="Example-Schedule_a_downtime_returns_OK_response",
        message="CR in progress",
        # The downtime will start from when the script is run
        start=int(datetime.now().timestamp()),
        # how long to schedule , add hours
        end=int((datetime.now() + relativedelta(hours=howlong)).timestamp()),
        timezone="Pacific/Auckland",
        scope=[
            "*",
        ],
        monitor_tags=[
            'client:{}'.format(client_name),
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


# Call both functions

schedule_byname(client_name, howlong)
schedule_bytag(client_name, howlong) 
