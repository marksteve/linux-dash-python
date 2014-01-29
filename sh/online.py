import subprocess

from app import app
from flask import json


@app.route('/online')
def online():
  users = subprocess.check_output(
    'w -h | awk \'{print " "$1","$3","$4","$5}\'',
    shell=True,
  ).splitlines()
  result = []
  for user in users:
    result.append(user.decode('utf-8').split(','))
  return json.dumps(result)

