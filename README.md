# Cloud_Project
A final year project for the Cloud Computing laboratory, in which we had to make 4 or more services comunicate with eatchother.
for this i chose to focus on AWS by using the EC2, S3, λ fucntion, SNS & SQS.

# Flowchart
![diagram](https://github.com/NotJeket/Cloud_Project/assets/37781149/3744acb8-af46-4c9a-9527-390ff3aca051)

# What Everything Does:
# EC2:
In an EC2 instance powered by Debian 12 i've installed Jenkins to act as a Secure DevOps Pipeline and Docker for containers. Connected with GitHub it pulls instructions from the Jenkinsfile, which in turn pulls instructions from the Dockerfile to create contaiers, export them as .tar images and place them localy inside the EC2 as well as the S3 bucket made for this purpose.

# S3 Bucket:
This was mainly used as the main storage solution for the .tar images made by docker to have them phisicaly stored somewhere.

# λ fucntion:
Lambda fucntions were used as a watchdog for the S3 Bucket. Kepping an constant eye on the present files this function would tirgger in the event of a new file being detected. Which in turn would trigger the SQS service.

# SQS service:
Triggered by the λ fucntion this would send the signall to the SNS subscribers boradcasting a message about what happened inside the S3 Bucket (Eg. a new file was detected).

# SNS service:
Contians the message "A new job was done in the /dockers folder of the S3 Bucket", which will be sent to the Email and phone number of the people subscribed to said service.

# Undexpected outcomes:
I managed to turn the SQS into a SPAM generator for my Email adress which got my main AWS account BANNED. Good times.
