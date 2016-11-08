bind = "0.0.0.0:8080"
workers = 3
daemon = False
loglevel = "debug"
proc_name = "Residency"
pidfile = "/tmp/Residency.pid"
worker_class = "gevent"
debug = True
django_settings = "Residency.settings"