from datadog import initialize, api

options = {
    "api_key": "883ae4dae7ad2d1b57f46f56652153ec",
    "app_key": "890a39b62c285b830accffdc17daa2c4e3e1c9ab",
}

initialize(**options)

title = "Something big happened!"
text = "And let me tell you all about it here!"
tags = ["version:1", "application:web"]

#api.Event.create(title=title, text=text, tags=tags)
api.Metric.send(metric='my.series', points='datetime.now().timestamp()'.2)
