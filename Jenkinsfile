pipeline {
    agent any

    stages {
        stage ("Checkout SCM"){
            steps {
                checkout scm
            }
        }

        stage ("Install Requirements"){
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage ("Build Docker Image"){
            steps {
                bat 'docker build -t exam-demo .'
            }
        }

        stage ("Run Docker Image"){
            steps {
                bat 'docker run -d -p 5002:5002 exam-demo'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}