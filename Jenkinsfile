pipeline {
    agent any

    stages {
        stage('1') {
            steps {
                git branch: 'main', url: 'https://github.com/ofri737/first_repo.git'
                bat 'python "home work 1.py"'
            }
        }
    }
}