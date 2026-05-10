pipeline {

    agent any

    environment {
        IMAGE_NAME = "deployment-platform"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Repository Cloned Successfully'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t deployment-platform .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Check Kubernetes Pods') {
            steps {
                sh 'kubectl get pods'
            }
        }

        stage('Check Services') {
            steps {
                sh 'kubectl get services'
            }
        }

    }

    post {

        success {
            echo 'CI/CD Pipeline Executed Successfully'
        }

        failure {
            echo 'Pipeline Failed'
        }
    }
}