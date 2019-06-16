"""
All package info is here. By defaults, opens URL with the repo
"""

info = {
    "name": "copyhere",
    "version": "1.1.4",
    "description": "Module for copy or unzip a file to cwd",
    "url": "https://github.com/dongrama/copyhere",
    "author": "Andrei Gramakov",
    "author_email": "mail@agramakov.me",
    "install_requires": [line.rstrip('\n') for line in open("requirements.txt")],  # reading requirements.txt content
    "license": "MIT",

}

if __name__ == '__main__':
    import webbrowser

    webbrowser.open(info["url"])
