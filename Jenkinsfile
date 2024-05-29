pipeline {
    agent any
    
    environment {
        S3_BUCKET = 'cutiedelaborator'
        S3_FOLDER = 'dockers/'
        IMAGE_NAME = 'hello-world-docker'
        GIT_REPO = 'https://github.com/NotJeket/Cloud_Project.git'
        AWS_REGION = 'us-east-1'  // e.g., 'us-west-2'
        EC2_EXPORT_PATH = '/home/admin/dockerimg'
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
                sh 'docker save ${IMAGE_NAME} -o ${EC2_EXPORT_PATH}/${IMAGE_NAME}.tar'
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
