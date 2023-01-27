# 🔥 Batch Meet
Batch Meet is an online Community Chat Application mainly used for meeting and remote file access.

# 💎 Features
- User can create Chat Rooms.
- User can Communicate on a Group call.
- Group Call User Controls.
- Server can handle more than 50 users/ call.
- Live Video and Audio Interaction.
- Unique room name for chat room.

# ⚙️ Prerequisites

- You need to have python installed. You can install it from microsoft store or follow this [guide](https://www.geeksforgeeks.org/how-to-install-python-on-windows/).
- Django
- Redis
- Agora.io Account

# Setting up a Virtual Enviroment

It’s a common practice to have your Python apps and their instances running in virtual environments. Virtual environments allow different package sets and configurations to run simultaneously, and avoid conflicts due to incompatible package versions. 

Create a Virtual Enviroment in python by executing following command.
```bash
$ python3 -m venv env
```
activate the virtual environment.
```bash
# On Unix or MacOS (bash shell): 
/path/to/venv/bin/activate

# On Unix or MacOS (csh shell):
/path/to/venv/bin/activate.csh

# On Unix or MacOS (fish shell):
/path/to/venv/bin/activate.fish

# On Windows (command prompt):
\path\to\venv\Scripts\activate.bat

# On Windows (PowerShell):
\path\to\venv\Scripts\Activate.ps1
```

# Installation:
now install all the dependiencies
```bash
 $ pip install requirements.txt
```
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. 

# Working:
Thats it! You are ready to go. </br>
This project uses Redis channel as a channel Layer.
```bash
$ docker run -p 6379:6379 -d redis:5
```

run the Project by executing this.

```bash
$ python manage.py runserver
```

Project will be available on
``http://127.0.0.1:8000``

# Troubleshooting
If you are facing any problems, feel free to open an issue or contact me on `rimmelasghar4@gmail.com` 


[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
<br>
Code by Rimmel with ❤
