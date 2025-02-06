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
                sh 'apt-get update && apt-get install -y python3-pip'  // Install pip if missing
                sh 'python3 -m venv venv'  // Create virtual environment
                sh 'source venv/bin/activate'  // Activate virtual environment
                sh 'python3 -m pip install --upgrade pip'  // Upgrade pip
                sh 'python3 -m pip install -r requirements.txt'  // Install dependencies
                sh 'python3 -m pip install pytest'  // Install pytest
            }
        }

        stage('Verify Pytest Installation') {
            steps {
                sh 'python3 -m pip show pytest || echo "Pytest is not installed properly"'
            }
        }

        stage('Verify Python and Pip Paths') {
            steps {
                sh 'which python3'
                sh 'which pip3'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/'  // Run tests using python3
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
