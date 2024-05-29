pipeline {
    agent any
    
    environment {
        S3_BUCKET = 'cutiedelaborator'
        S3_FOLDER = 'dockers/'
        IMAGE_NAME = 'hello-world-docker'
        GIT_REPO = 'https://github.com/NotJeket/Cloud_Project.git'
        AWS_REGION = 'us-east-1'  // e.g., 'us-west-2'
        AWS_CREDENTIALS_ID = 'AWS creds'  // The ID of your AWS credentials in Jenkins
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
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${env.AWS_CREDENTIALS_ID}"]]) {
                    sh """
                        aws s3 cp ${IMAGE_NAME}.tar s3://${S3_BUCKET}/${S3_FOLDER}${IMAGE_NAME}.tar --region ${AWS_REGION}
                    """
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
