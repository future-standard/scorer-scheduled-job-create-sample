import json
from datetime import datetime, timedelta
import requests
import json


realm = 'pub'
# LT_
device_id = 'LT_f07438d6-0e55-4f46-9fc5-e8a7de0e0dd6'
# API Key
api_key = ''
algorithm_id = 'futurestandard:sensevideo-10fps'


url = 'https://api-%s.scorer.jp/v1/devices/%s/vcajobs' % (realm, device_id)

headers = {
    'Authorization': api_key,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

payload = {
    'algorithmId': algorithm_id,
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
        res = requests.post(url, data=json.dumps(payload), headers=headers)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

    return res
