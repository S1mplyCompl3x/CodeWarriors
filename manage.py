#!/usr/bin/env python
import os
import sys

import dotenv

if __name__ == "__main__":
    dotenv.read_dotenv()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Residency.settings")
    # test if environment variable is properly set
    # print(os.environ.get('DJANGO_SETTINGS_MODULE'))

    from django.core.management import execute_from_command_line

    # dirspot = os.getcwd()
    # print(dirspot + 'hello')

    execute_from_command_line(sys.argv)

    if 'livereload' in sys.argv:
        from django.core.wsgi import get_wsgi_application
        from livereload import Server
        application = get_wsgi_application()
        server = Server(application)

        # Add your watch
        # server.watch('path/to/file', 'your command')
        server.serve()
    else:
        execute_from_command_line(sys.argv)
