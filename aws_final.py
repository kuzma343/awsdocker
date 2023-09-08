import boto3


access_key = ''
secret_key = ''
region_name = 'eu-north-1'  


ec2 = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)


instance_type = 't3.micro'  
key_name = 'kuzma'  
security_group_ids = ['sg-02176327c590ef2ad'] 
ami_id = 'ami-0989fb15ce71ba39e'  

script_path = '/home/kuzma/asd.sh'

# Зчитуємо зміст вашого скрипта
with open(script_path, 'r') as script_file:
    user_data_script = script_file.read()

# Запускаємо EC2 інстанс з параметром UserData
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    MinCount=1,
    MaxCount=1,
    UserData=user_data_script  # Вставте зміст вашого скрипта
)

# Отримуємо інформацію про запущений інстанс
instance_id = response['Instances'][0]['InstanceId']

print(f'EC2 інстанс з ID {instance_id} успішно запущений і виконує ваш скрипт.')
