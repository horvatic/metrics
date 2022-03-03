pipeline {
    agent none
    stages {
        stage('Build') {
            agent { docker { image 'python:3' } }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install --user psutil '
                    sh 'python3 -m unittest discover -p "*_test.py"'
                }
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
