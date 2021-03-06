pipeline {
    agent any

    stages {
        stage('presettings') {
          steps {
            sh 'python36 --version'
          }
        }

        stage('checkout') {
          steps {
            git branch: 'develop', poll: true, url: 'git@github.com:FyodorovAleksej/OpenAirPollutionMonitor.git'
          }
        }

        stage('build') {
          steps {
            dir ('./src/docker') {
              sh 'docker-compose up -d'
            }
          }
        }

        stage('clean up') {
          steps {
            dir ('./src/docker') {
              sh 'docker-compose stop'
            }
          }
        }

        stage('make report') {
          steps {
            dir ('./docs/tex/docker-xelatex-fonts/') {
              sh 'chmod +x *.sh'
              sh './make.sh make cleanall'
              sh './make.sh make all'
            }
            sh 'git add docs/tex/docker-xelatex-fonts/'
            sh "git config --global user.name Jenkins-Agent"
            sh "git config --global user.email Fyodorov.aleksej@gmail.com"

            sh "git commit -m \"[JENKINS_PIPELINE] - update report - BUILD #${BUILD_NUMBER}\""
            sh "git push origin develop"
          }
        }
    }
}
