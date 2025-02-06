pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/mohitjaiin/devops-workflow.git'
        BRANCH = 'main'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Build Application') {
            steps {
                // Install necessary packages including python3-venv
                sh 'apt-get update && apt-get install -y python3-pip python3-venv'
                // Create the virtual environment
                sh 'python3 -m venv venv'
                // Activate the virtual environment using . instead of source
                sh '. venv/bin/activate && python3 -m pip install --upgrade pip'
                // Install dependencies from requirements.txt
                sh '. venv/bin/activate && python3 -m pip install -r requirements.txt'
                // Install pytest inside the virtual environment
                sh '. venv/bin/activate && python3 -m pip install pytest'
            }
        }

        stage('Verify Pytest Installation') {
            steps {
                // Check if pytest is correctly installed in the virtual environment
                sh '. venv/bin/activate && python3 -m pytest --version || echo "Pytest is not installed properly"'
            }
        }

        stage('Verify Python and Pip Paths') {
            steps {
                sh '. venv/bin/activate && which python3'
                sh '. venv/bin/activate && which pip3'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the tests using pytest in the virtual environment
                sh '. venv/bin/activate && python3 -m pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed!'
        }
    }
}
