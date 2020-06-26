import json
from datetime import datetime, timedelta
import requests
import json


with open('config.json') as f:
    conf = json.load(f)

url = 'https://api-{}.scorer.jp/v1/devices/{}/vcajobs'.format(
    conf.realm, conf.device_id)

headers = {
    'Authorization': conf.api_key,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

payload = {
    'algorithmId': conf.algorithm_id,
    'algorithmVersion': '1.0',
    'arguments': {
        'fromDateTime': None,
        'toDateTime': None
    },
    'jobType': 'Period'
}


def lambda_handler(event, context):

    current_dt = datetime.today()

    end_dt = current_dt.replace(minute=0, second=0, microsecond=0)
    end_str = end_dt.strftime('%Y-%m-%d %H:%M:%S+0900')

    start_dt = end_dt - timedelta(hours=1)
    start_str = start_dt.strftime('%Y-%m-%d %H:%M:%S+0900')

    payload['arguments']['fromDateTime'] = start_str
    payload['arguments']['toDateTime'] = end_str

    try:
        res = requests.post(url, data=payload, headers=headers)
        return res

    except Exception as e:
        print(e)
        raise e
