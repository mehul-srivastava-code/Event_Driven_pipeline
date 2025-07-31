
pipeline {
    agent any

    environment {
        PYTHON_CMD = 'python'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/mehul-srivastava-code/event-pipeline.git'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                bat "${env.PYTHON_CMD} -m pip install --upgrade pip"
                bat "${env.PYTHON_CMD} -m pip install pandas matplotlib"
            }
        }

        stage('Ingest Data') {
            steps {
                bat "${env.PYTHON_CMD} scripts\\ingest.py"
            }
        }

        stage('Process Data') {
            steps {
                bat "${env.PYTHON_CMD} scripts\\process.py"
            }
        }

        stage('Generate Report') {
            steps {
                bat "${env.PYTHON_CMD} scripts\\report.py"
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'processed\\*.csv, processed\\*.png', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Build Finished'
        }
    }
}
