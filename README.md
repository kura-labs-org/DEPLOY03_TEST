# Deployment 3 Jenkins with Pytest

## Steps

1. Created an EC2 instance hosting a Jenkins pipeline. 
    - Make sure git and jenkins is installed.
2. Create a Jenkinsfile in the root of your Github repository which Jenkins will be accessing. 
```
pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh ''' #!/bin/bash 
        python3 -m venv test3
        source test3/bin/activate
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
```

3. Create a new multi-branch pipeline in Jenkins hooked to the Github repo with your credentials. 
4. Click build now on your Jenkins dashboard to see your first successful build. 
   ![First Test Build](first_success.png)

5. 

