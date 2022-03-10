pipeline {
    agent none
    stages {
        stage('Test') {
            agent { docker { image 'python:3' } }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 -m unittest discover -p "*_test.py"'
                }
            }
        }
		stage('Build') {
            agent { 
                docker { 
                    image 'docker' 
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                } 
            }
        	environment {
                SHORT_COMMIT = "${GIT_COMMIT[0..7]}"
            }
			steps {
                sh '''
				    docker build -t horvatic/metrics:$SHORT_COMMIT .
                    docker push horvatic/metrics:$SHORT_COMMIT
                '''
			}
		}
        stage('Deploy Dev') {
            agent { docker { image 'alpine/k8s:1.19.15' } }
            environment {
                K8PROFILE = credentials('K8PROFILE')
                SHORT_COMMIT = "${GIT_COMMIT[0..7]}"
            }
            steps {
                sh '''
                    export TAG="$SHORT_COMMIT"
                    export KUBECONFIG=.kube/config
                
                    mkdir -p .kube
                    echo $K8PROFILE | base64 -d > .kube/config
                    
                    envsubst < deploy/base/deployment.yaml > tempbase
                    cat tempbase > deploy/base/deployment.yaml
                    rm tempbase

                    kubectl apply -k "deploy/dev" -n dev

                    sleep 10

                    kubectl wait --for=condition=ready pod -l app=met -n dev --timeout=10m
                '''
            }
        }
        stage('Smoke Test') {
            agent { docker { image 'curlimages/curl:latest' } }
            steps {
                sh '''
                    curl --fail "${MetricsHealthEndpoint}"
                '''
            }
        }
    }
}