import subprocess

from app import app
from flask import json


@app.route('/ps')
def ps():
  resp = []
  result = subprocess.check_output(
    'ps aux | awk \'{print $1","$2","$3","$4","$5","$6","$7","$8","$9","$10","$11}\'',
    shell=True,
  ).splitlines()
  for a in result:
    resp.append(a.decode('utf-8').split(','))
  return json.dumps(resp)
