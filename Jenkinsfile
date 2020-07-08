pipeline {
  agent none

	triggers {
        cron('H 0 * * *')
  }
  stages {
    stage('Install Dependencies') {
			agent any
      steps {
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
				archiveArtifacts 'DungeonCli.zip'
      }
    }

		stage('Compile on MacOS') {
			agent {
				label 'macos'
			}
			steps {
				sh './compile.sh'
				archiveArtifacts 'DungeonCli.zip'
			}
		}
  }
}
