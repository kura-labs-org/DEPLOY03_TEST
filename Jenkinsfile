#!/bin/bash

pipeline {
  agent any
  stages {
    stage ('test') {
      
      steps{
        sh '''
       python3 -m venv test3
       source3 test3/bin/activate
       pip install pip --upgrade, pytest
       
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
