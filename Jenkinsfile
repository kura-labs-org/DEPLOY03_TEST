pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh ''' #!/bin/bash 
        python3 -m venv test3
        pip install pip --upgrade
        pip install pytest
        py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py
        '''
        
      }
      post{
        always {
          junit 'test-reports/results.xml'
        }
      }
    }
  }
}
