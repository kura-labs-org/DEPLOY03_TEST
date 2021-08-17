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
            emailext body: "Check console output at $BUILD_URL to view the results. \n\n ${CHANGES} \n\n -------------------------------------------------- \n${BUILD_LOG, maxLines=100, escapeHtml=false}", 
                    to: "zscyrus31@gmail.com", 
                    subject: "Build failed in Jenkins: $Deployment - #$BUILD_NUMBER"
        }
        }
      }
    }
  }
}
