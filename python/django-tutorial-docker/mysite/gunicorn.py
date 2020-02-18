#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
bind = '0.0.0.0:8000'

daemon = False
pidfile = '/var/run/gunicorn/django.pid'

errorlog = '/var/log/gunicorn/error.log'
accesslog = '/var/log/gunicorn/access.log'
logfile = '/var/log/gunicorn/django.log'
loglevel = 'debug'
