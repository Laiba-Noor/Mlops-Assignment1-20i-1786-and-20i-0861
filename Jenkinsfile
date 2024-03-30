pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'laibanoor/Mlops-Assignment1-20i-1786-and-20i-0861:final'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE_NAME ."
                }
            }
        }

        stage('Login Dockerhub abd Push Docker Image') {
            environment {
                DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials')
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'laibanoor', passwordVariable: 'laiba123456')]) {
                        sh "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin"

                        sh "docker push $DOCKER_IMAGE_NAME"
                    }
                }
            }
        }
    }
}
