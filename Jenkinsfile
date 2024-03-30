pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('californiahousingml:latest')
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image('bostonhousingml:latest').push()
                    }
                }
            }
        }
    }
    post {
        success {
            mail to: 'i201786@nu.edu.pk',
                subject: "Successful Deployment",
                body: "The Boston Housing ML model has been successfully deployed."
        }
    }
}
