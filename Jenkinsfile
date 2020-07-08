pipeline {
  agent { label 'macos' }
	triggers {
        cron('H 0 * * *')
  }
  stages {
    stage('Install Dependencies') {
      steps {
        sh 'python3 -m pip install -r requirements.txt'
        sh 'python3 -m pip install nuitka'
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
