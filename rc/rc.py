#!/usr/bin/python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from bottle import post, route, request, template, static_file, run
import os, subprocess

@route('/')
@route('/', method='POST')
def remote_control():
    st_home = os.statvfs("/home")
    free_home = "%.2f" % float((st_home.f_bavail * st_home.f_frsize)/1.073741824e9)
    
    if (request.POST.get("cardbackup")):
        process = subprocess.Popen("sudo /home/pi/little-backup-box/scripts/card-backup.sh", shell=True)
        return template('exit.tpl')
    if (request.POST.get("camerabackup")):
        process = subprocess.Popen("sudo /home/pi/little-backup-box/scripts/camera-backup.sh", shell=True)
        return template('exit.tpl')
    if (request.POST.get("devicebackup")):
        process = subprocess.Popen("sudo /home/pi/little-backup-box/scripts/device-backup.sh", shell=True)
        return template('exit.tpl')
    if (request.POST.get("shutdown")):
        process = subprocess.Popen("sudo shutdown -h now", shell=True)
        return template('exit.tpl')
    return template('rc.tpl', freespace_home=free_home)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0", port=8080, debug=True, reloader=True)
