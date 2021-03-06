from flask import Flask

import os
import subprocess
import time

# import markisol
# import atexit
#
# I don't know why calling the funcs from the file
# doesn't work when called from a Flask handler,


dir_path = os.path.dirname(os.path.realpath(__file__))


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    # markisol.init()
    # atexit.register(markisol.cleanup)

    @app.route('/up')
    def shadeUp():
        # markisol.send('up')
        subprocess.call(['%s/markisol.py' % dir_path, 'up'])
        return "OK"

    @app.route('/down')
    def shadeDown():
        # markisol.send('down')
        subprocess.call(['%s/markisol.py' % dir_path, 'down'])
        return "OK down"

    @app.route('/stop')
    def shadeStop():
        # markisol.send('stop')
        subprocess.call(['%s/markisol.py' % dir_path, 'stop'])
        return "OK"
      
    return app
