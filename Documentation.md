
# Step 1
### 1. Build an ec2 instance and add a script to the user data so that it downloads jenkins into itself.
### 2. Access jenkins through your instance's public ip using the 8080 port
### 3. Enter your credentials to get started in jenkins
# Step 2
### 1. Create a new multibranch project in jenkins  
### 2. Connect your github repository to the jenkins pipeline using you github token and link
# Step 3
### 1. Make a jenkins file in your github repository and add the script that creates a python3 environment to run pytest and uses j-unit   
![Screenshot 2021-08-28 112046](https://user-images.githubusercontent.com/60336145/131222756-00333649-5dcd-4e5d-9da4-4a940996c549.png)
### At this point your build should run successfully if not use the console logs to track down the problems (usually typos in your jenkins file)
![Screenshot 2021-08-14 164025](https://user-images.githubusercontent.com/60336145/131222814-1a612fce-7a78-4ea7-93d6-bf0d304b61e2.png)
# Step 4 
### try to change the test code so that it fails
![Screenshot 2021-08-14 164524](https://user-images.githubusercontent.com/60336145/131222850-c2477a7a-d58a-4a58-84c3-ac6ab3d4cc79.png)
### after the first fail try to fix your code so that it passes the the test (give it a new test to pass)
![Screenshot 2021-08-21 112802](https://user-images.githubusercontent.com/60336145/131222873-422f146c-00ac-43e0-b3a4-150582d6fa26.png)
![Screenshot 2021-08-21 113153](https://user-images.githubusercontent.com/60336145/131222877-1b86f405-c952-4754-98b6-349ea8f988f8.png)

