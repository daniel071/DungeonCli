pipeline {
  agent none

	triggers {
        cron('20 0 * * *')
  }
  stages {
    stage('Install Dependencies') {
			agent any
      steps {
        sh 'python3 -m venv env'
        sh 'source env/bin/activate'
        sh 'python3 -m pip install -r requirements.txt --user'
        sh 'python3 -m pip install nuitka --user'
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

		stage('Compile on MacOS') {
			agent {
				label 'macos'
			}
			steps {
				sh './compile.sh'
				archiveArtifacts 'DungeonCli_MacOS.zip'
			}
		}
  }
}
