import os
import sys
path=input("enter your directory path")

if os.path.exists(path):
	list_of_files_dir=os.listdir(path)
else:
	print("enter valid path")
	sys.exit()

for each_file_or_dir in list_of_files_dir:
	f_d_p=os.path.join(path,list_of_files_dir)	
	print(f_d_p)
#if os.path.isfile(f_d_p)
	#print(f'{f_d_p}is a file')
#else 
	#print(f'{f_d_p}is a directory')