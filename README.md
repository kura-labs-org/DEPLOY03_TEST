# Deployment 3 Jenkins with Pytest

## Steps to build:

### Building A Pipeline that can run tests

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
        py.test --verbose --junit-xml test-reports/results.xml
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

5. Now to follow the spirit of Test Driven Development we are going to write the test cases for our new feature of multiplying by 2.

### Multiplying By 2 Feature 
6. Create a new python file titled test_multiply2vals.py and enter the following lines
```
# test_multiply2vals.py
import pytest
import calc

def test_multiplication():
        """
        Test that multiplication between an integer/float and another integer/float
        will return the correct value

        """

        result = calc.multiply(3,3)
        assert result == 3 * 3

def test_float_multiplication():
        """
        Test that multiplication between an integer/float and another integer/float
        will return the correct value

        """

        result = calc.multiply('3.6', '5.4')
        assert result == (3.6*5.4)


def test_string_multiplication():
        """
        Test that a user can't multiply strings.
        """

        result = calc.multiply('3', 'A string')
        
        assert result == 'Error: Arguments must be an integer or float'

```
> The above script imports the calc library from sources folder and tests to see if the function returns the correct value. If not the tests will fail. And it will fail at the moment since the multiply method hasn't been implemented yet.

 ![Failed Test Build](failure_after_test.png)

7. Now to actually pass these failing tests we have to build the features that will pass our test cases.
8. Next add a new function called multiply to the calc library. 
```
def multiply(arg1, arg2):
    # Ensure both arguments are ints or float
    arg1 = conv(arg1)
    arg2 = conv(arg2)

if (isinstance(arg1,(int,float)) and isinstance(arg2,(int,float))):
    print(arg1,arg2)
    return arg1 * arg2
        

else:
    return 'Error: Arguments must be an integer or float'

```
9. Since the multiply function has been added to the calc library, it our tests should now pass when Jenkins runs them. 