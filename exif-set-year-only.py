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
	print('reading: %s --> writing: %s' % (filename_in, filename_out))
	with open(filename_in, 'rb') as image_file:
		image = Image(image_file)
	datetime_original = datetime.strptime(image['datetime_original'], DATETIME_STR_FORMAT)
	new_datetime = datetime_original.replace(year=new_year)
	print('  changing: %s -->  %s'  % (datetime_original.strftime("%m/%d/%Y, %H:%M:%S.%f"), new_datetime.strftime("%m/%d/%Y, %H:%M:%S.%f")))
	image.datetime_original = new_datetime.strftime(DATETIME_STR_FORMAT)
	image.datetime_digitized = new_datetime.strftime(DATETIME_STR_FORMAT)
	image.datetime = new_datetime.strftime(DATETIME_STR_FORMAT)
	with open(filename_out, 'wb') as new_image_file:
		new_image_file.write(image.get_file())


if __name__ == "__main__":
    main()
