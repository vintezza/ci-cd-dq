pipeline {
    agent any
    triggers {
        cron('H 18 1,15 * *')
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
                    currentDay = sh(returnStdout: true, script: 'date +%d').trim()
                    sh "git checkout -b origin/releases/$currentDate"
                    sh "git merge origin/develop"
                    sh "git push"
                    if (currentDay == '01') {
                        sh "git checkout master"
                        sh "git merge origin/releases/$currentDate"
                        sh "git push"
                    }
                }
            }
        }
    }
}