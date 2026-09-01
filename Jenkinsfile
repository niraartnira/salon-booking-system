pipeline {
    agent any
    
    environment {
        COMPOSE_PROJECT_NAME = 'salon-booking-system'
    }


    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker --version'
                sh 'docker compose version'
            }
        }

        stage('Build Application') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Verify Containers') {
            steps {
                sh 'docker ps'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 10'
                sh 'curl --fail http://localhost:8000'
            }
        }
    }

    post {
        success {
            echo 'Salon Booking application deployed successfully'
        }

        failure {
            echo 'Deployment failed. Check Jenkins console logs.'
        }
    }
}
