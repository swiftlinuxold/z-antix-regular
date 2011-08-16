#! /usr/bin/env python

import os # allows interaction with the operating system
import getpass # allows the username to be obtained
import os.path # allows you to determine if a directory exists
import sys, commands # Allows checking for root

whoami = commands.getoutput( "whoami" )
if whoami != 'root':
	sys.exit( 'You must be root to run this script.' )

is_chroot = os.path.exists('/srv')
dir_develop=''

if (is_chroot):
	dir_develop='/usr/local/bin/develop'	
else:
	username=commands.getoutput("logname")
	dir_develop='/home/'+username+'/develop'

print 'Conky display: Diet -> Regular'
if (not(is_chroot)):
    text=open('/home/'+username+'/.conkyrc', 'r').read()
    text = text.replace("Diet", "Regular") 
    open('/home/'+username+'/.conkyrc', "w").write(text)

text=open('/etc/skel/.conkyrc', 'r').read()
text = text.replace("Diet", "Regular") 
open('/etc/skel/.conkyrc', "w").write(text)
	
