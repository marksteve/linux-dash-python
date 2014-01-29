import subprocess

from app import app
from flask import json


@app.route('/whereis')
def whereis():
  result = subprocess.check_output(
    'whereis php mysql vim python ruby java apache2 nginx openssl vsftpd make'
    '|awk \'{ split($1, a, ":");if (length($2)==0) print a[1]",Not Installed"; else print a[1]","$2;}\'',
    shell=True,
  ).splitlines()
  return json.dumps([a.decode('utf-8').split(',') for a in result])
