pipeline {
  agent any
  stages {
    stage ('test') {
      steps{
        sh '''
       python3 -m venv test 
       source test/bin/activate
       pip install pytest
       py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py
       '''
           }
      
    stage ('Build') {
      steps{
        sh '''
        py.test --verbose --junit-xml test-reports/results.xml sources/add2vals.py
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
}


