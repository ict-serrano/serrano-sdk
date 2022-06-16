pipeline {
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
  }
}