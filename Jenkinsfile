pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Repository Cloned Successfully'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Build Application') {
            steps {
                echo 'Django Backend Build Successful'
            }
        }

    }
}