#!/user/bin/env python

import os

if __name__ == "__main__":
    os.environ.setdefault("FLASK_APP", "hello.py")
    os.system("flask run --host=0.0.0.0 --port=8080")