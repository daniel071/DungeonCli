pipeline {
  agent any
  stages {
    stage('Install Dependencies') {
      steps {
        sh 'python -m pip install -r requirements.txt'
      }
    }

    stage('Compile') {
      steps {
        sh './compile.sh'
      }
    }

    stage('Archive artifacts') {
      steps {
        archiveArtifacts './bin.build/DungeonCli.dist'
      }
    }

  }
}