import subprocess

from app import app


@app.route('/test')
def test():
  milli = subprocess.check_output('awk \'{print $1*1000}\' /proc/uptime')
  return int(milli) / 1000 * 60 * 60

