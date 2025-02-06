pipeline {
    agent any
    
    environment {
        // Set up the virtual environment directory
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Update package lists and install python3-pip, python3-venv
                sh '''
                    apt-get update && apt-get install -y python3-pip python3-venv
                '''
            }
        }

        stage('Build Application') {
    steps {
        // Create and activate the virtual environment
        sh '''
            python3 -m venv ${VENV_DIR}
            . ${VENV_DIR}/bin/activate
            python3 -m pip install --upgrade pip
            python3 -m pip install -r requirements.txt
        '''
    }
}

        stage('Run Tests') {
            steps {
                // Activate the virtual environment and run tests
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python3 -m pytest tests/
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build the Docker image (if needed, adjust based on your Dockerfile)
                sh '''
                    docker build -t flaskapp .
                '''
            }
        }
        
        stage('Run Application') {
            steps {
                // Run the application (if needed, adjust based on your app's requirements)
                sh '''
                    docker run -d -p 5000:5000 flaskapp
                '''
            }
        }
    }
    
    post {
        always {
            // Clean up resources if needed
            echo 'Pipeline execution completed!'
        }
    }
}
