import subprocess

from app import app
from flask import json


@app.route('/ip')
def ip():
  result = subprocess.check_output(
    '/sbin/ifconfig |grep -B1 "inet addr" |awk \''
    '{ if ( $1 == "inet" ) { print $2 } else if ( $2 == "Link" ) { printf "%s:",$1 } }\' |awk'
    ' -F: \'{ print $1","$3 }\'',
    shell=True,
  ).splitlines()
  result2 = subprocess.check_output(
    'curl http://ipecho.net/plain; echo',
    shell=True,
  ).splitlines()
  resp = [['external_ip', result2[0].decode('utf-8')]]
  resp.append([a.decode('utf-8').split(',') for a in result])
  return json.dumps(resp)
