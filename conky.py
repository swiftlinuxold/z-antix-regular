#! /usr/bin/env python

import os # allows interaction with the operating system
import getpass # allows the username to be obtained
import os.path # allows you to determine if a directory exists

is_chroot = os.path.exists("/srv")
username=''
dir_develop=''

if (is_chroot):
	dir_develop='/usr/local/bin/develop'
else:
	username=os.environ['XAUTHORITY']
	username=username[6:-12]
	dir_develop='/home/'+username+'/develop'

print 'Conky display: Diet -> Regular'
if (~is_chroot):
    text=open('/home/'+username+'/.conkyrc', 'r').read()
    text = text.replace("Diet", "Regular") 
    open('/home/'+username+'/.conkyrc', "w").write(text)

text=open('/etc/skel/.conkyrc', 'r').read()
text = text.replace("Diet", "Regular") 
open('/etc/skel/.conkyrc', "w").write(text)
	
