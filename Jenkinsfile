pipeline {
    agent none
    stages {
        stage('Build') {
            agent { docker { image 'python:3.10.1-alpine' } }
            steps {
                sh 'python --version'
            }
        }
        stage('Deploy') {
            agent { docker { image 'alpine/k8s:1.19.15' } }
            environment {
                K8PROFILE = credentials('K8PROFILE')
            }
            steps {
                sh '''
                    export KUBECONFIG=.kube/config
                
                    mkdir -p .kube

                    echo $K8PROFILE | base64 -d > .kube/config

                    kubectl get no
                '''
            }
        }
    }
}
