# DEPLOY03_TEST

<h1 align=center>Deployment 3</h1>

Welcome to deployment 3. We have been covering the fundamentals of python, now it’s time to apply your python knowledge to a python application called Add2Vals. This python application is a simple command line application that adds two arguments and outputs the value to the user. You have been tasked to first test the Add2Val application with the already made test_calc.py and produce an XML report. 

Once you have ran a test build and produced a test report. Create an additional feature or component to the Add2Vals application. Create a test that will fail when you test Add2 a second time and then get your test to pass. 

***Documentation and screenshot requirements:*** 
- [x]Fork (https://github.com/kura-labs-org/DEPLOY03_TEST)
- [x]Screenshot the first successful test build.
- [x]Document your added component or feature.
- [x]Screenshot your failed test and document why your test failed.
- [x]Screenshot your successful test build and document what you did to fix your failed test build  
- [x]Initiate a pull request to the kura_labs_org/DEPLOY_3_TESTING repo with your documentation, screenshots(add screenshots to documentation), test_calc.py with your added test, and add2vals.py with your added feature or component.   

👉Link to **some** helpful instructions: [here](https://github.com/kura-labs-org/DEPLOY03_TEST/blob/main/Deployment%203.pdf)  


<h1>Documentation</h1>

<h2>Purpose</h2>

The purpose of this deployment is to build on top of previous deployments using Jenkins. In this deployment, we will learn about pytest, which is a module used in conjunction with the building functions of Jenkins. The pytest module will be incorporated into a script written specifically to test the current program, which is add2py. The results expected will be the matched against the arguments in the test.

<h2>Steps</h2>

First build was completed using Freestyle Jenkins Pipeline option


<h3<Second Objective</h3>

For second build, objective was add a feature that would fail with a new test when built with jenkins
-Adding testing for mul2 on the test py file

-Added a mul2 function to calc.py

-Pushing to git to update on Jenkins to build

-Build has indeed failed



To fix this build. I needed to modify the add2cal file and modify the inherent functions of sys.arg of taking in two arguments
in a single command and make it so that the user will select the operation as well as adding individual arguements as input.
--changed lists from sys.arg to mod_number
--changed the add2 variable to a if statement to call either add2 or mul2(which was added in the calc2)

There are some unnecessary items in the code that were edited out instead of being deleted in-case references were needed to undo this.

<h3>Why this is important</h3>

The reason we added a testing component to the build using Jenkins has to do with test-driven development. Test-driven development is the concept that when writing code, your code should be written based off the test that you write first. These test are important to create and run post build to ensure that values that the program/script/feature anticipates for a given output or input is within the operating parameters that are acceptable for the developer and the organization's goals in the real world. For example, if a bank deploys a feature into their application that involves monetary changes to a bank account and a bug in the code allowed for the value of that number to be larger or smaller than the value that is actually supposed to be, this cound be financially catastrophic for the bank.
