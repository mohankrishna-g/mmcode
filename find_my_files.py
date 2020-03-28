import os

p_s_d="ABCDEFGHIJKLMNOPQRSTUVXYZ"
my_os_drives_li=[]
for each_drive in p_s_d:
	drive_name=each_drive+":\\"
	if os.path.exists(drive_name):
		my_os_drives_li.append(drive_name)
print("all drives on your system os are:",my_os_drives_li)

"""
for each_drive in my_os_drives_li:
	for r,d,f in os.walk(each_drive):
		for each_f in f:
			if os.path.join(r,each_f).endwith(".py")
				print(os.path.join(r,each_f))
				"""