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
        withCredentials([string(credentialsId: 'discord-webhook', variable: 'SECRET')]) { //set SECRET with the credential content
          discordSend description: "Jenkins Pipeline Build", footer: "DungeonCli",
          link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME,
          thumbnail: "https://raw.githubusercontent.com/daniel071/DungeonCli/master/Images/Logos/nightlyTerminal.png",
          webhookURL: ${SECRET}
        }
      }
    }
	}
}
