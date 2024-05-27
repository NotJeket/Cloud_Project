pipeline {
    agent any
    
    environment {
        S3_BUCKET = 'cardboardbox'
        S3_FOLDER = 'dockers/'
        IMAGE_NAME = 'hello-world-docker'
        GIT_REPO = 'https://github.com/NotJeket/Cloud_Project.git'
        AWS_REGION = 'us-east-1'  // e.g., 'us-west-2'
        AWS_CREDENTIALS_ID = 'LabRoleCredentials'  // The ID of your AWS credentials in Jenkins
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${env.GIT_REPO}"
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.IMAGE_NAME}")
                }
            }
        }
        stage('Save Docker Image') {
            steps {
                sh 'docker save ${IMAGE_NAME} -o ${IMAGE_NAME}.tar'
            }
        }
        stage('Upload to S3') {
            steps {
                withAWS(region: "${env.AWS_REGION}", credentials: "${env.AWS_CREDENTIALS_ID}") {
                    s3Upload(file: "${IMAGE_NAME}.tar", bucket: "${env.S3_BUCKET}", path: "${env.S3_FOLDER}${IMAGE_NAME}.tar")
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
