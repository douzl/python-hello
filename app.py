#!/user/bin/env python

import os

if __name__ == "__main__":
    os.environ.setdefault("FLASK_APP", "hello.py")
    os.system("flask run")