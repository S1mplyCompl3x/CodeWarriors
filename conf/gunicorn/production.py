bind = "unix:/tmp/gunicorn.Residency.production.sock"

# http://gunicorn.org/design.html#how-many-workers
workers = 5

# Supervisor needs a non-daemonized process
daemon = False

pidfile = "/tmp/gunicorn.Residency.production.pid"
loglevel = "warning"
proc_name = "Residency-production"
worker_class = "gevent"
debug = False

django_settings = "Residency.settings"
