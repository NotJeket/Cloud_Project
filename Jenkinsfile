pipeline {
    agent any
    
    environment {
        S3_BUCKET = '***************'
        S3_FOLDER = '********/'
        IMAGE_NAME = '********'
        GIT_REPO = '****************************************'
        AWS_REGION = '********'  // e.g., 'us-west-2'
        EC2_EXPORT_PATH = '****************'
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
