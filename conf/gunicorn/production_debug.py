bind = "unix:/tmp/gunicorn.Residency.production.sock"

# http://gunicorn.org/design.html#how-many-workers
workers = 5

# Supervisor needs a non-daemonized process
daemon = False

pidfile = "/tmp/gunicorn.Residency.production.pid"
loglevel = "debug"
proc_name = "Residency-debug"
worker_class = "gevent"
debug = True

django_settings = "Residency.settings"

