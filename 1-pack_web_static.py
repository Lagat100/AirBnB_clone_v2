#!/usr/bin/python3
#  Fabric script that generates a .tgz archive from the
# contents of the web_static folder of your AirBnB Clone repo
# using the function do_pack

import os.path
from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + timestamp + ".tgz"
        local("mkdir -p versions")
        local("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None

