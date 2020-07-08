pipeline {
  agent {
    label 'macos'
  }
  stages {
    stage('Install Dependencies') {
      steps {
        sh 'python3 -m pip install -r requirements.txt'
        sh 'python3 -m pip install nuitka'
      }
    }

    stage('Compile') {
      parallel {
        stage('Compile Linux') {
          steps {
            sh './compile.sh'
          }
        }

        stage('Compile MacOS') {
          steps {
            sh './compile.sh'
          }
        }

      }
    }

    stage('Archive artifacts') {
      steps {
        archiveArtifacts 'DungeonCli.zip'
      }
    }

  }
  triggers {
    cron('H 0 * * *')
  }
}