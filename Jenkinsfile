pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Repository Cloned'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building Application'
            }
        }
    }
}