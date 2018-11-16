# blog-serverless-battleship
A repository for the blog 'Serverless Battleship'

## Rules
The following rules apply:

- Use Python
- You are fee to choose your stack
- You are free to choose your architecture
- You are free to choose your cloud
- We meet in the cloud at 12.00 o'clock
- We shoot at each other for 15 minutes

## Technical rules
The following technical rules apply

- Service discovery by means of DNS:
  - Dennis: https://dennisvriend.binx.io
  - Kevin: https://kevinkessels.binx.io
  - Martijn: https://martijnvdgrift.binx.io
  - Thijs: https://thijsdevries.binx.io  
- Bullets have the following format:
  - HTTP POST with the following body:

```json
{
  "timestamp": "yyyymmddhhmmssSS",
  "uuid": "uuid",
  "name": "name"
}
```

**Request/response pattern**:
- When you 'shoot' `requests.post('')` you have to do the following:
  - put your name in the payload,
  - generate a uuid v4 and put that in the payload
  - generate the epoch time in millis
  - log the text: `your_name,generated_uuid,epoch_in_millis`
- when you 'get-hit' ie. receive and handle a message, you have to do the following:
  - generate an epoch time
  - log the text: `your_name,received_uuid,epocyh_in_millis,received_payload`  
- After the battle you must export a log file containing:
    - all the shots fired (requests) using the format above,
    - all the 'you-got-hit' (handled messages), using the format above 

## Teams
The following teams are formed:

Team A: Dennis and Kevin
Team 2: Martijn and Thijs

## Teams chose the following:
Team A:
- Dennis chose GCP with Cloud Functions
- Kevin chose AWS with unsure

Team B:
- Thijs AWS with chalice and API Gateway with Lambda
- Martijn chose GCP with Google App Engine
