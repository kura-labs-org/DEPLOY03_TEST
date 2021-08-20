#!/bin/bash

pipeline {
  agent none
  stages {
    stage ('test') {
      agent { docker 'maven:3.8.1-adoptopenjdk-11'}
      steps{
        sh'''
       python3 -m venv test3
       source test3/bin/activate
       pip install pip --upgrade
       pip install pytest
       py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py
       '''
      }
      }
      
      post {
        always {
          junit 'test-reports/results.xml'
        }
      }
    }
  }
}
