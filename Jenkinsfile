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
                    currentDate = '2021-01-05'//sh(returnStdout: true, script: 'date +%Y-%m-%d').trim()
                    currentDay = '01' //sh(returnStdout: true, script: 'date +%d').trim()
                    sh "git config --global user.email \"anna_rudkovskaia@epam.com\""
                    sh "git config --global user.name \"Anna Rudkovskaia\""
                    sh "git remote set-url origin https://$GITHUB_CRED@github.com/vintezza/ci-cd-dq.git"
                    sh "git checkout develop"
                    sh "git checkout -b releases/$currentDate"
                    sh "git merge origin/develop"

                    sh "git push --set-upstream origin releases/$currentDate"
                    if (currentDay == '01') {
                        echo "Deploying.."
                        sh "git checkout master"
                        sh "git merge origin/releases/$currentDate"
                        sh "git push"
                    }
                }
            }
        }
    }
}