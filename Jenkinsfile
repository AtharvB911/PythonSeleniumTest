pipeline {
    agent any

    tools {
        "jenkins.plugins.shiningpanda.tools.PythonInstallation" "python"
    }

    environment {
        PATH = "C:\\Users\\Biswajit\\AppData\\Local\\Programs\\Python\\Python313;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Checking out repository...'
                checkout scm
            }
        }

        stage('Set Up Environment') {
            steps {
                echo '⚙️ Setting up Python environment...'
                bat '''
                python --version
                pip --version
                pip install --upgrade pip
                if exist venv rmdir /s /q venv
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🧪 Running Selenium test cases...'
                bat '''
                call venv\\Scripts\\activate
                pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }
    }

    post {
        success {
            echo '✅ All tests passed successfully!'
        }
        failure {
            echo '❌ Tests failed. Check console output for details.'
        }
    }
}
