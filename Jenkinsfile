pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'yamil'
        AWS_REGION = 'us-east-1'
        AWS_CREDENTIALS = 'LabRoleCredentials' // ID of the stored AWS credentials in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NotJeket/Cloud_Project.git'
            }
        }
        stage('Build and Test Docker Image') {
            steps {
                script {
                    // Running Docker build locally
                    sh '''
                    docker build -t ${DOCKER_IMAGE} .
                    docker run -d --name ${DOCKER_IMAGE}-test ${DOCKER_IMAGE}
                    '''
                }
            }
        }
    }
}
