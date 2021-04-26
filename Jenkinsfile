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
            script {
                withCredentials([usernameColonPassword(credentialsId: 'github_creds', variable: 'GITHUB_CRED')]) {
                    currentDate = sh(returnStdout: true, script: 'date +%Y-%m-%d').trim()
                    echo(currentDate)
                    echo(a)
                    sh "git checkout -b origin/releases/$currentDate"
                    sh 'git status'
                }
            }
        }
    }
}