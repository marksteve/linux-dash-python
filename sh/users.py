import subprocess

from app import app
from flask import json


@app.route('/users')
def users():
  result = subprocess.check_output(
    'awk -F: \'{ if ($3<=499) print "system,"$1","$6; else print "user,"$1","$6; }\' < /etc/passwd',
    shell=True,
  ).splitlines()
  return json.dumps([a.decode('utf-8').split(',') for a in result])
