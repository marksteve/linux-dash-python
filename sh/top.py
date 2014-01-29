import subprocess

from app import app
from flask import json


@app.route('/top')
def top():
  resp = ''
  result = subprocess.check_output(
    '/usr/bin/top -b -n1|awk \'{print $2}\'',
  ).splitlines()
  a = result[6].split(' ')
  b = [a[2], a[3], a[9], a[11], a[13], a[15], a[17], a[18], a[20], a[21], a[25], a[27]]
  resp = json.dumps(b) + '\n'
  final = []
  start_from = 7
  a = result[7].split(' ')
  if not a[2] and not a[3]:
    b = [a[4], a[5], a[11], a[14], a[15], a[16], a[17], a[18], a[21], a[23], a[26], a[27]]
    start_from = 8
    final.append(b)
  else:
    final.append([])
  for x in range(start_from, len(result)):
    a = result[x].split(' ')
    b = [a[2], a[3], a[9], a[12], a[13], a[14], a[15], a[16], a[19], a[21], a[24], a[25]]
    final.append(b)
  resp += json.dumps(final)
  return resp

