pipeline {
  agent {
          label 'linux'
  }

	stages {
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
    stage('Compile on Linux') {
      agent {
        label 'linux'
      }
      steps {
        sh './compile.sh'
        archiveArtifacts 'DungeonCli_Linux.zip'
      }
    }
	}
}
