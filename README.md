# SCORER Cloud scheduled job create sample
This sample Python script is AWS Lambda function to invole SCORER Cloud API to create scheduled job. It is assumed that schleduled invocations are made by CloudWatch Events.


# Usage

## 1. Set required information to config.json
```
{
    "realm": "pub",
    "device_id": "LT_....", # Device ID can be obtained from the SCORER Cloud URL
    "api_key": "", # API can be obtained for SCORE Cloud setting menu
    "algorithm_id": ""
}
```

## 2. Downlod requests module

Python requests module is not installed as default library in AWS Lambda, so you need to download this to local folder.

```
pip3 install requests -t .
```

## 3. Create AWS Lambda function

Create new Lambda function with Python 3.7 runtime.
<img width="800" alt="" src="https://user-images.githubusercontent.com/4166534/71317674-4fda7f00-24c8-11ea-83e3-d1c15705ab80.png">

Compress this directory as .zip and upload it.
<img width="800" alt="" src="https://user-images.githubusercontent.com/4166534/71317691-90d29380-24c8-11ea-9b2d-a31558104717.png">


## 4. Set CloudWatch Events as trigger
Set Cloud Watch Events as trigger. For example, if you need to create a job every hour, it can be done by setting cron setting like `cron(10 * * * ? *)`.

<img width="800" alt="" src="https://user-images.githubusercontent.com/4166534/71317624-967ba980-24c7-11ea-8034-696bb1d2af26.png">



