pipeline {
    parameters {
        choice(name: 'AGENT_LABEL', choices: ['agent1', 'agent2'], description: 'Choose agent to run on')
    }

    agent { label "${params.AGENT_LABEL}" }

    stages {
        stage('Clone Repo') {
            steps {
                echo "Cloning from SCM - already handled by Jenkins if using Git project"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'model/model.pkl', fingerprint: true
            }
        }
    }
}
