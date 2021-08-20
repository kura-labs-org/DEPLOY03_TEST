#!/bin/bash

pipeline {
  agent { docker { image 'python 3.7.11 } }
  stages {
    stage ('test') {
      
      steps{
        sh 'python --version' '''
       python3 -m venv test3
       source test3/bin/activate
       pip install pip --upgrade
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
