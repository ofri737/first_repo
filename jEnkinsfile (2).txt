properties([pipelineTriggers([pollSCM(ignorePostCommitHooks: true, scmpoll_spec: '* * * * *')])])
pipeline {
    agent any

    stages {
        stage('1') {
            steps {
                bat 'dir'
            }
        }
    }
}