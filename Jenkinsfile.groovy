pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
    ansiColor('xterm') // Enable colors in terminal
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Build') { // Checkout (git clone ...) the projects repository
      agent {
        docker { image 'python:3' }
      }
      steps {
        sh """
          pip install pylint
          """
      }
    }
  }
}