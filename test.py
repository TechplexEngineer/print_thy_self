#!/usr/bin/python

import sys
import os

with open(os.path.basename(sys.argv[0])) as f:
	for line in f:
		print line,