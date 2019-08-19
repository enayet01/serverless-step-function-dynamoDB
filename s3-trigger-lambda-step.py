...
bucket_name = event['Records'][0]['s3']['bucket']['name']
file_key = event['Records'][0]['s3']['object']['key']

input= {
        'bucket_name': bucket_name,
        'file_key': file_key
    }

stepFunction = boto3.client('stepfunctions')
response = stepFunction.start_execution(
    stateMachineArn='arn:aws:states:XXXXXXXXXXXXXXXX:stateMachine:my-state-machine',
    input = json.dumps(input, indent=4)
)
...
