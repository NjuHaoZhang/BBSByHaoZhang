#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app


sys.path.insert(0, abspath(dirname(__file__)))
application = app.app

"""
刚刚测试了在本机Ubuntu上运行BBS，基于gunicorn运行BBS，supervisor管理gunicorn；还有bug，需要找一下
建立一个软连接
ln -s /var/www/bbs/bbs.conf /etc/supervisor/conf.d/bbs.conf

ln -s /var/www/bbs/bbs.nginx /etc/nginx/sites-enabled/bbs


➜  ~ cat /etc/supervisor/conf.d/bbs.conf

[program:bbs]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/bbs
autostart=true
autorestart=true


/usr/local/bin/gunicorn wsgi
--bind 0.0.0.0:2001
--pid /tmp/blog.pid
"""
