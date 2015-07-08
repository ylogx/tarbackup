#!/usr/bin/env python3

import sys
import tarbackup.main
try:
    sys.exit(tarbackup.main.main())
except KeyboardInterrupt:
    sys.exit(1)
