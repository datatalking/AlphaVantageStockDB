# SOURCE
import subprocess


def main():
	run_shell_create_daily()
	run_shell_create_intraday()



def run_shell_create_daily():
	"""
	
	:return:
	"""

	# This is our shell command, executed by Popen.
	# create_daily.sh and create_intraday.sh
	p = subprocess.Popen("create_daily.sh")
	
	print(p.communicate())


def run_shell_create_intraday():
	"""
	
	:return:
	"""
	# TODO create_daily.sh
	# This is our shell command, executed by Popen.
	# TODO and create_intraday.sh
	p = subprocess.Popen("create_intraday.sh")
	
	print(p.communicate())


if __name__=="__main__":
	
	main()
