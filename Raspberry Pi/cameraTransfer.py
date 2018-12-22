# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.  If not, see 
# <http://www.gnu.org/licenses/>.
#
# This script is part of the Intervalometerator project, a time-lapse camera controller for DSLRs:
# https://github.com/greiginsydney/Intervalometerator
# https://greiginsydney.com/Intervalometerator
# https://intvlm8r.com


# Thank you https://docs.python.org/2/howto/urllib2.html
#
# This script is executed every time the Pi boots, causing it to trigger a sync with the camera.
# A pre-req task is that the Arduino has woken the camera, which we assume has taken place by the time the script runs.

from urllib2 import urlopen, URLError
import logging
import os
from datetime import datetime

LOGFILE_PATH = os.path.expanduser('/home/pi')
LOGFILE_NAME = os.path.join(LOGFILE_PATH, 'cameraTransfer.log')

htmltext = ''


def main():
    logging.basicConfig(filename=LOGFILE_NAME, filemode='w', format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG)
    try:
        response = urlopen('http://localhost/transfer?copyNow=1')
        log('Response code = ' + str(response.getcode()))
        htmltext = response.read()
        if 'Unable to connect to the camera' in htmltext:
            log('Unable to connect to the camera')
        log('=========================')    
        log(str(htmltext))
    except URLError as e:
        if hasattr(e, 'reason'):
            log(str(e.reason))
        elif hasattr(e, 'code'):
            log(str(e.code))
    except Exception as e:
        log('Unhandled error: ' + str(e))


def log(message):
    try:
        logging.info(message)
    except Exception as e:
        #print 'error:' + str(e)
        pass


if __name__ == '__main__':
    main()