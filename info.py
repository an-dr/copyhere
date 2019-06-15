"""
All package info is here. By defaults, opens URL with the repo
"""

info = {
    "name": "copyhere",
    "version": "1.1.2",
    "description": "Module for copy or unzip a file to cwd",
    "url": "https://github.com/dongrama/copyhere",
    "author": "Andrei Gramakov",
    "author_email": "mail@agramakov.me",
    "license": "MIT",

}

if __name__ == '__main__':
    import webbrowser

    webbrowser.open(info["url"])
