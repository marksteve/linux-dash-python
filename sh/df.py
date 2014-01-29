import subprocess

from app import app
from flask import json


@app.route('/df')
def df():
  resp = []
  result = subprocess.check_output(
    'df -h | awk \'{print $1","$2","$3","$4","$5","$6}\'',
    shell=True,
  ).splitlines()
  for a in result:
    resp.append(a.decode('utf-8').split(','))
  return json.dumps(resp)
