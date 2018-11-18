import http.client
import json
import uuid
import time
import boto3
import os

client = boto3.client("kinesis")

def millis():
    return int(round(time.time() * 1000))

def handler(event, context):
    results = []
    pings = 0
    HOSTNAME = os.environ['HOSTNAME']
    PATH = os.environ['PATH']

    while context.get_remaining_time_in_millis() > 200:
        pings += 1
        start = millis()
        conn = http.client.HTTPSConnection(HOSTNAME)
        headers = {'Content-type': 'application/json', "User-Agent": "Lambda-step-function-gun"}
        foo = {'timestamp': millis(), 'uuid': "thijs" + str(uuid.uuid4()) }
        json_data = json.dumps(foo)
        conn.request('POST', PATH, json_data, headers)
        response = conn.getresponse()
        stop = millis()
        response = response.read().decode()
        data = json.dumps({"elaps": stop - start, "response": response }).encode('utf-8')
        results.append({ "PartitionKey": str(context.log_stream_name), "Data": data })
        if len(results) > 10:
            response = client.put_records(
                Records=results,
                StreamName='ping-war'
            )
            response = []
    return { "done": "true", "pings": pings }

if __name__ == "__main__":
    print(handler({},{}))
