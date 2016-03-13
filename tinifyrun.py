""" IMPLEMENTING TINYPNG API TO OPTIMIZE PNG AND JPEG IMAGES ON THEIR SERVERS """
#do some imports
import os
import sys

#import the package and the assign the API-KEY
import tinify
tinify.key = ""


#store the list of files in a list

path_to_dir = os.getcwd()
print(path_to_dir)


files = os.listdir(path_to_dir)
for file in files:
	if file == "tinifyrun.py":
		files.remove(file)
	else:
		file = sys.path[0] + '\\' + file

#work on each file?
print('Working...')
for file in files:
	try:
		source = tinify.from_file(file)
		source.to_file(file)
		print(str(file) + ' DONE!')
	except:
		print(str(file) + ' not found...')



		