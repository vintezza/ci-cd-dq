pipeline {
    agent any
    stages {
        stage('Run tests') {
            steps {
                sh 'python3 tests.py'
            }
        }
    }
    post {
        success {
            withCredentials(usernameColonPassword(credentialsId: 'github_creds', variable: 'GITHUB_CRED')) {
                currentDate = sh(returnStdout: true, script: 'date +%Y-%m-%d').trim()
                sh '''
                git checkout -b releases/${currentDate}
                git status
                '''
            }
        }
    }
}