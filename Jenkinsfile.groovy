pipeline {
  environment {
    PROJECT_NAME = 'serrano-sdk'
  }
  options {
    buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
    ansiColor('xterm') // Enable colors in terminal
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  agent {
    kubernetes {
      cloud 'kubernetes'
      defaultContainer 'jnlp'
      yamlFile 'build.yaml'
    }
  }
  stages {
    stage('Install requirements') {
      steps {
        container('python') {
          sh '/usr/local/bin/python -m pip install --upgrade pip'
          sh 'pip install -r requirements.txt'
          sh 'pip install --no-input cyclonedx-bom'
        }
      }
    }
    stage('Unit tests') {
      steps {
        container('python') {
          sh 'python -m unittest discover'
        }
      }
    }
    stage('Sonarqube') {
      environment {
        scannerHome = tool 'SonarQubeScanner'
      }
      steps {
        container('java') {
          withSonarQubeEnv('sonarqube') {
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=${PROJECT_NAME}"
          }
          timeout(time: 10, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true
          }
        }
      }
    }
    stage('Generate BOM') {
      steps {
        container('python') {
          sh 'cyclonedx-bom -e -F -o ./bom.xml'
        }
      }
    }
    stage('Dependency Track') {
      steps {
        container('python') {
          dependencyTrackPublisher artifact: 'bom.xml', projectId: '282b5d5e-547b-449b-a04b-ff8b049f07ee', synchronous: true
        }
      }
    }
  }
}