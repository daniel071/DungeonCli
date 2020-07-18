pipeline {
  agent none
  stages {
    stage('Install Dependencies') {
      parallel {
        stage('Install on Linux') {
          agent {
            label 'linux'
          }
          steps {
            sh 'python3 -m venv env'
            sh 'source env/bin/activate'
            sh 'python3 -m pip install -r requirements.txt'
            sh 'python3 -m pip install nuitka'
          }
        }

        stage('Install on MacOS') {
          steps {
            echo 'test'
          }
        }

      }
    }

    stage('Compile') {
      parallel {
        stage('Compile on Linux') {
          agent {
            label 'linux'
          }
          steps {
            sh './compile.sh'
            archiveArtifacts 'DungeonCli_Linux.zip'
          }
        }

        stage('Compile on MacOS') {
          steps {
            echo 'test2'
          }
        }

      }
    }

  }
}