pipeline {
  agent any
  stages {
    stage('Install Dependencies') {
      steps {
				sh `PATH=${PATH}:/usr/local/bin`
				sh `sudo easy_install pip`
        sh 'python -m pip3 install -r requirements.txt'
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
