#!/usr/bin/env python
# -*- coding: UTF-8

# Created on 2017.07.28
#
# Author: Marino Punturieri
import sys

# Uncomment if python virtual env is not working.
# sys.path.append("./venv/lib/python2.7/site-packages/")

import datetime as dt
import datetime as dt
import logbook


LOGGER = logbook.Logger('pyUniverseClient')
LOG = logbook.FileHandler(str(dt.date.today()) + '-pyUniverseClient.log')
LOG.push_application()

time = str(dt.datetime.now().hour) + str(dt.datetime.now().minute) + str(dt.datetime.now().second)
# Main
def main():
    try:
        LOGGER.info('Starting pyUniverseClient')

    except Exception as e:
        LOGGER.error('The application has somme issue while running!')
        LOGGER.error(str(e))

if __name__ == '__main__':
    main()
