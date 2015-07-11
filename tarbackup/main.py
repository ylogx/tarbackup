#!/usr/bin/env python3
#
#  tarbackup - zips the folder passed as first argument in a unique tar file
#
#  Copyright (c) 2014-2015 Shubham Chaudhary <me@shubhamchaudhary.in>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
import time

from tarbackup.archiver import create_unique_backup

def main(argv=sys.argv):
    folder_in = os.path.curdir
    folder_in = os.path.abspath(folder_in)
    folder_in = os.path.basename(folder_in)
    if len(argv) >= 2:
        folder_in = argv[1:]
    create_unique_backup(folder_in)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
