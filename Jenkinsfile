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
                    sh "git config --global user.email \"anna_rudkovskaia@epam.com\""
                    sh "git config --global user.name \"Anna Rudkovskaia\""
                    sh "git remote set-url origin https://$GITHUB_CRED@github.com/vintezza/ci-cd-dq.git"

                    sh "git checkout -b origin/releases/$currentDate"
                    sh "git merge origin/develop"

                    //sh "git commit -m new_release_$currentDate"
                    sh "git push --set-upstream origin refs/heads/releases/$currentDate"
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