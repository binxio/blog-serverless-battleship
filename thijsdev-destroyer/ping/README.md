# Ping battleship

## Generate the template

    python ./gen_template.py > step.yml

## Deploy the generated template

    aws cloudformation deploy --template-file step.yml --stack-name ping --capabilities CAPABILITY_IAM