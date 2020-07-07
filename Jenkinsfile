pipeline {
  agent any
  stages {
    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pip install nuitka'
      }
    }

    stage('Compile') {
      steps {
        sh './compile.sh'
      }
    }

    stage('Archive artifacts') {
      steps {
        archiveArtifacts 'DungeonCli.zip'
      }
    }

  }
}