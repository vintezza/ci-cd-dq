pipeline {
    agent any
    triggers {
        cron('0 18 1,15 * *')
    }
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
                    sh "git checkout -b origin/releases/$currentDate"
                    sh "git merge develop"
                }
            }
        }
    }
}