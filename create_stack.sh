aws s3 cp bobik-template.json s3://mediasapiens-sources/bobik-template.json
aws cloudformation create-stack --stack-name bobik --capabilities CAPABILITY_IAM --template-url https://s3.eu-central-1.amazonaws.com/mediasapiens-sources/bobik-template.json
