pipeline {
  agent {
    docker { image 'node:14-alpine' }
  }
  stages {
    stage ('test') {
      steps {
        sh '''#!/bin/bash
        python3 -m venv test3
        source test3/bin/activate
        pip install pip --upgrade
        pip install maven
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
