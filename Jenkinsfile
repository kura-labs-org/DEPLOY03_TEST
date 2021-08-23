pipeline { 
    agent any 
    stages {
        stage('test') { 
            steps { 
                sh '''#! /bin/bash
                python3 -m venv test3
                source test3/bin/activate
                pip3 install pip --upgrade
                pip3 install pytest
                py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py
                '''
             }
             post {
               always {
                 junit 'test-reports/results.xml'
               }
            }
        }
    }
}
