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
    }
}