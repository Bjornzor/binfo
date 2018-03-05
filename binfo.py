import sys
import platform
import getpass
from uuid import getnode as get_mac
import psutil,datetime


error = ""
		

if len(sys.argv) == 2:

	i = sys.argv[1]

	if sys.argv[1] not in ['0','1','2','3','4']:
		errorMsg = "***ERROR NOTIFICATION: Pick a number from the options list***"
		error = 1

	if sys.argv[1].isalpha():
		errorMsg = "***ERROR NOTIFICATION: You entered a string***"
		error = 1


else:
	errorMsg = ""
	error = 1


def usage():



	print("""


	 _     _        __      
	| |   (_)      / _|     
	| |__  _ _ __ | |_ ___  
	| '_ \| | '_ \|  _/ _ \ 
	| |_) | | | | | || (_) |
	|_.__/|_|_| |_|_| \___/ 
	                        
	                        
	               	
   	Author: Björn Welboren

   	Decription: 

   	This tool is created for the purpose of improving my Python skills

	Options:

	0 = Print pc info
	1 = Print mac address 
	2 = (Mounted) Disk partitions
	3 = Print uptime since boot
	4 = Show processes running by user and pid

		"""
			)
	print("\n\t"+errorMsg)



def shows(a):


	
	if a == '0':
		print("\nCommand executed with Python {a} at {b} showing{c}\n ".format(a=platform.python_version(), b=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), c = ": Machine information"))
		print("[*]NAME:	{}".format(getpass.getuser()))
		print("[*]SYSTYPE:	{}".format(platform.machine()))
		print("[*]PC-NAME:	{}".format(platform.node()))
		print("[*]OS+SP:	{}".format(platform.platform(aliased=0,terse=0)))
		print("[*]CPU:		{}".format(platform.processor()))

	if a == '1':
		print("\nCommand executed with Python {a} at {b} showing{c}\n ".format(a=platform.python_version(), b=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), c = ": Mac Address"))
		x = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))
		print("[*]MAC-ADDRESS:		{}".format(x))

	
	if a == '2':
		print("\nCommand executed with Python {a} at {b} showing{c}\n ".format(a=platform.python_version(), b=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), c = ": Mounted partitions"))
		print("[*]Mounted disk partitions: {}".format(psutil.disk_partitions(all=False)))

	if a == '3':
		print("\nCommand executed with Python {a} at {b} showing{c}\n ".format(a=platform.python_version(), b=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), c = ": Boottime"))
		print("[*]Up since: {}".format(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")))

	if a == '4':
		print("\nCommand executed with Python {a} at {b} showing{c}\n ".format(a=platform.python_version(), b=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), c = ": Processlist"))
		for proc in psutil.process_iter():
			try:
				pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
			except psutil.NoSuchProcess:
				print("No process")
			else:
				print(pinfo)
	



if error != 1:
	shows(i)

else:
	usage()
	

