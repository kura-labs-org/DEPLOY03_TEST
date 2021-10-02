pipeline {
  agent {
    docker { image 'ubuntu' }
  }
  stages {
    stage ('test') {
      steps {
        sh '''#!/bin/bash
        apt update -y
        apt install maven
        apt install python3
        apt install python3-venv
        python3 -m venv test3
        source test3/bin/activate
        pip install pip --upgrade
        pip install pytest
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

