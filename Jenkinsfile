pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh ''' #!/bin/bash 
        #Creating a virtual environment called test3 to run our python application and tests.
        python3 -m venv test3
        source test3/bin/activate
        pip install pip --upgrade
        #Installing pytest for our virtual environment in order to run our tests.
        pip install pytest
        #Export pytest results in junit-xml format to the test-reports folders
        py.test --verbose --junit-xml test-reports/results.xml
        '''
        
      }
      post{
        always {
          junit 'test-reports/results.xml'
        }
        failure {
          def jobName = currentBuild.fullDisplayName
          emailext body: '''${SCRIPT, template="text"}''',
            subject: "[Jenkins] ${jobName}",
            to: "zscyrus31@gmail.com"
        }
      }
    }
  }
}
