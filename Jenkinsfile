pipeline {
    agent any

    environment {
        ECR_REPOSITORY_URI = '905418214725.dkr.ecr.us-east-1.amazonaws.com/cloud-project-test'
        AWS_REGION = 'us-east-1'
        DOCKER_IMAGE = 'yamil'
        ECS_CLUSTER = 'test-cluster'
        ECS_SERVICE = 'test'
        AWS_CREDENTIALS = 'LabRoleCredentials' // ID of the stored AWS credentials in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NotJeket/Cloud_Project.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        stage('Login to ECR') {
            steps {
                withAWS(credentials: "${AWS_CREDENTIALS}", region: "${AWS_REGION}") {
                    script {
                        sh 'aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPOSITORY_URI}'
                    }
                }
            }
        }
        stage('Tag and Push Docker Image') {
            steps {
                script {
                    sh 'docker tag ${DOCKER_IMAGE}:latest ${ECR_REPOSITORY_URI}:latest'
                    sh 'docker push ${ECR_REPOSITORY_URI}:latest'
                }
            }
        }
        stage('Deploy to ECS') {
            steps {
                withAWS(credentials: "${AWS_CREDENTIALS}", region: "${AWS_REGION}") {
                    script {
                        sh '''
                            aws ecs update-service --cluster ${ECS_CLUSTER} --service ${ECS_SERVICE} --force-new-deployment
                        '''
                    }
                }
            }
        }
    }
}
