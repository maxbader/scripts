#!/usr/bin/env python3

import sys
import os
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime
import subprocess

def main():
	if (len(sys.argv) - 1) != 1:
		print('usage: %s filename' % sys.argv[0] )
		return 
	filename_in = sys.argv[1]
	path, fname = os.path.split(filename_in)
	print('path: %s --> fname: %s' % (path, fname))
	filename_in_base = os.path.splitext(os.path.basename(filename_in))[0]
	file_number = int(filename_in_base.lstrip(filename_in_base[0]))
	print('filename_in_base: %s --> file_number: %i' % (filename_in_base, file_number))
	files = []
	files.append("p" + str(file_number) + ".jpg")
	for i in range(1, 10):
		files.append("p" + str(file_number-i) + ".jpg")
		files.append("p" + str(file_number+i) + ".jpg")
	file_canditate = ""
	for file in files:
		if os.path.exists(file):
			file_canditate = file
			break
	print(f"file_canditate {file_canditate}")
	if not file_canditate:
		print(f"no candiate found")
		return
		
	with open(file_canditate, 'rb') as image_file:
		image = Image(image_file)
	datetime_original = datetime.strptime(image['datetime_original'], DATETIME_STR_FORMAT)
	exif_date = datetime_original.strftime("%Y:%m:%d %H:%M:%S.%f")
	print(exif_date)
    #datetime_original.year
	command = "exiftool -AllDates=\"" + exif_date + "\" " + filename_in
	print(command)

	# Run the command and capture the output
	result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
			
if __name__ == "__main__":
    main()
