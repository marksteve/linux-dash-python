import subprocess

from app import app
from flask import json


@app.route('/mem')
def mem():
  result = subprocess.check_output(
    'free -tmo | awk \'{print $1","$2","$3","$4}\'',
    shell=True,
  ).splitlines()
  return json.dumps(result[1].decode('utf-8').split(','))
