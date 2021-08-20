#!/bin/bash

pipeline {
  agent any
  stages {
    stage ('test') {
      
      steps{
        sh '''
       
       source python3 -m venv/bin/activate
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
