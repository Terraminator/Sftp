import paramiko
import threading
from time import sleep
import sys

ssh = paramiko.SSHClient()

target = str(input("Target: "))
uname = input("Username: ")
pwd = input("Password: ")
def datatransfer(target, uname, pwd):
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(target, username=uname, password=pwd)
		
	reply = input("Command: ")

	if reply == "Get" or reply == "get":
		item = input("File: ")
		dst = item
		ftp_client=ssh.open_sftp()
		ftp_client.get(item, dst)
		ftp_client.close()
		ssh.close()
			
			
	elif reply == "Put" or reply == "put":
		item = input("File: ")
		dst = item
		ftp_client=ssh.open_sftp()
		ftp_client.put(item, dst, confirm=False, callback=None)
		ftp_client.close()
		ssh.close()
	else:
		output = ""
		stdin,stdout,stderr=ssh.exec_command(reply)
		for line in stdout:
			output=output+line
		if output!="":
			print(output)

		

while True:
	datatransfer(target, uname, pwd)
