pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat '''
                python3 -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests using pytest...'
                bat '''
                call venv\\Scripts\\activate
                pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Python Selenium Tests Passed Successfully!'
        }
        failure {
            echo '❌ Tests Failed. Check Console Output for Details.'
        }
    }
}
