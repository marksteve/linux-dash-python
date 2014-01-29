linux-dash-python
=================

Python port of [afaqurk](https://github.com/afaqurk/linux-dash).

Setup and run
-------------
```sh
$ cd sh
$ python3 -m venv ~/.virtualenvs/linux-dash
$ source ~/.virtualenvs/linux-dash/bin/activate
$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
$ pip3 install -r requirements.txt
$ gunicorn wsgi:app
```
