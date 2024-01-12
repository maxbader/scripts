#!/usr/bin/env python3

import sys
import os
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime

def main():
	if (len(sys.argv) - 1) != 2:
		print('usage: %s filename year' % sys.argv[0] )
		return 
	filename_in = sys.argv[1]
	new_year = int(sys.argv[2])
	path, fname = os.path.split(filename_in)
	filename_out = os.path.join(path, "modified_" + fname)
	with open(filename_in, 'rb') as image_file:
		image = Image(image_file)
	datetime_original = datetime.strptime(image['datetime_original'], DATETIME_STR_FORMAT)
	if(datetime_original.year != new_year):
	    print('Year is set on %i, at file %s' % (datetime_original.year, filename_in))


if __name__ == "__main__":
    main()
