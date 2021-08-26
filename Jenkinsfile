
pipeline {
  agent any
  stage {
    stage ('test') {
      steps {
      sh '''#!/bin/bash
      python3 -m venv test3
      source test/bin/active
      pip intsall pip --upgrade
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
