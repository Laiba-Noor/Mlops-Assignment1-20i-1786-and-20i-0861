pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Builds a Docker image from a Dockerfile in the current directory
                    docker.build('californiahousingml:latest')
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    // Logs in to Docker Hub and pushes the built image
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image('californiahousingml:latest').push()
                    }
                }
            }
        }
    }
    post {
        success {
            // Sends an email notification upon successful deployment
            mail to: 'i201786@nu.edu.pk',
                subject: "Successful Deployment",
                body: "The California Housing ML model has been successfully deployed."
        }
    }
}
