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
	
if (~is_chroot):
	# Go through every file in MIME-types directory that isn't abiword
	# and replace abiword with oowriter.
	# Go through every file in MIME-types directory that isn't gnumeric
	# and replace gnumberic with oocalc.
	# Go through every file in MIME-types directory that isn't gnumeric
	# and replace gnumberic with oocalc.

	path_mime='home/'+username+'/.config/rox.sourceforge.net/MIME-types/'
	text=open(path_mime+'application_msword').read()
	text.replace()
	
	
	
	
	
	
if (~is_chroot):
	# Replace "Diet" with "Regular"
    text=open('/home/'+username+'/.conkyrc', 'r').read()
    text = text.replace("Diet", "Regular") 
    open('/home/'+username+'/.conkyrc', "w").write(text)
    
if (~is_chroot):
	# Replace "Diet" with "Regular"
    text=open('/etc/skel/.conkyrc', 'r').read()
    text = text.replace("Diet", "Regular") 
    open('/etc/skel/.conkyrc', "w").write(text)

rm /home/$USERNAME/.config/rox.sourceforge.net/MIME-types/application_msword 
	cp $DIR_CONFIG/MIME-types/application_msword /home/$USERNAME/.config/rox.sourceforge.net/MIME-types

	rm /home/$USERNAME/.config/rox.sourceforge.net/MIME-types/application_vnd.ms-excel 
	cp $DIR_CONFIG/MIME-types/application_vnd.ms-excel /home/$USERNAME/.config/rox.sourceforge.net/MIME-types

	rm /home/$USERNAME/.config/rox.sourceforge.net/MIME-types/application_vnd.oasis.opendocument.spreadsheet 
	cp $DIR_CONFIG/MIME-types/application_vnd.oasis.opendocument.spreadsheet /home/$USERNAME/.config/rox.sourceforge.net/MIME-types

	rm /home/$USERNAME/.config/rox.sourceforge.net/MIME-types/application_vnd.oasis.opendocument.text 
	cp $DIR_CONFIG/MIME-types/application_vnd.oasis.opendocument.text /home/$USERNAME/.config/rox.sourceforge.net/MIME-types

	rm /home/$USERNAME/.config/rox.sourceforge.net/MIME-types/application_vnd.ms-powerpoint
	cp $DIR_CONFIG/MIME-types/application_vnd.ms-powerpoint /home/$USERNAME/.config/rox.sourceforge.net/MIME-types

	rm /home/$USERNAME/.config/rox.sourceforge.net/MIME-types/application_vnd.oasis.opendocument.presentation
	cp $DIR_CONFIG/MIME-types/application_vnd.oasis.opendocument.presentation /home/$USERNAME/.config/rox.sourceforge.net/MIME-types
