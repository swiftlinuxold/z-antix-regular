#! /usr/bin/env python

import os # allows interaction with the operating system
import getpass # allows the username to be obtained
import os.path # allows you to determine if a directory exists

is_chroot = os.path.exists('/srv')
username=''
dir_develop=''

if (is_chroot):
	dir_develop='/usr/local/bin/develop'
else:
	username=os.environ['XAUTHORITY']
	username=username[6:-12]
	dir_develop='/home/'+username+'/develop'
	
print 'Changing MIME-types so files open in OpenOffice instead of Abiword or Gnumeric'

# 1.  defaults.list in ~/.local/share/applications and 
# /etc/skel/.local/share/applications: abiword -> oowriter

# Changing files in ~/.config/rox.sourceforge.net/MIME-types
# and /etc/skel/.config/rox.sourceforge.net/MIME-types
# 2. application_msword: abiword -> oowriter
# 3. application_vnd.ms-excel: gnumeric -> oocalc
# 4. application_vnd.oasis.opendocument.spreadsheet: gnumeric -> oocalc
# 5. application_vnd.oasis.opendocument.text: abiword -> oowriter

# Adding files in ~/.config/rox.sourceforge.net/MIME-types
# and /etc/skel/.config/rox.sourceforge.net/MIME-types
# 6. application_vnd.ms-powerpoint: ooimpress
# 7. application_vnd.oasis.opendocument.presentation: ooimpress

# CHANGING ~/.local/share/applications, /etc/skel/.local/share/applications
#ADD
#application/vnd.oasis.opendocument.text=ooo-writer.desktop
#application/vnd.ms-excel=ooo-calc.desktop
#CHANGE:
#application/msword: abiword.desktop -> ooo-writer.desktop

def change_text (pathdir, filename, text_old, text_new):
	if (not(is_chroot)):
		file_mime='/home/'+username+'/'+pathdir+'/'+filename
		text=open(file_mime, 'r').read()
		text=text.replace(text_old, text_new)
		open (file_mime, 'w').write(text)
	
	file_mime='/etc/skel/'+pathdir+'/'+filename
	text=open(file_mime, 'r').read()
	text = text.replace(text_old, text_new) 
	open(file_mime, "w").write(text)

print 'Changing MIME types for Thunar'	
dl_old='application/msword=abiword.desktop'
dl_new='application/msword=ooo-writer.desktop\n'
dl_new=dl_new+'application/vnd.oasis.opendocument.text=ooo-writer.desktop\n'
dl_new=dl_new+'application/vnd.ms-excel=ooo-calc.desktop\n'
change_text ('.local/share/applications', 'defaults.list', dl_old, dl_new)

print 'Changing MIME types for ROX-Filer'
path_mime_types='.config/rox.sourceforge.net/MIME-types'
change_text (path_mime_types, 'application_msword', 'abiword', 'oowriter')
change_text (path_mime_types, 'application_vnd.ms-excel', 'gnumeric', 'oocalc')
change_text (path_mime_types, 'application_vnd.oasis.opendocument.spreadsheet', 'gnumeric', 'oocalc')
change_text (path_mime_types, 'application_vnd.oasis.opendocument.text', 'abiword', 'oowriter')

def add_files(pathdir, filename, text):
	if (not(is_chroot)):
		file_mime='/home/'+username+'/'+pathdir+'/'+filename
		f = open (file_mime, 'w')
		f.write('#! /bin/sh\n'+text)
	
	file_mime='/etc/skel/'+pathdir+'/'+filename
	f = open (file_mime, 'w')
	f.write('#! /bin/sh\n'+text)
	
path_mime_types='.config/rox.sourceforge.net/MIME-types'
add_files(path_mime_types, 'application_vnd.ms-powerpoint', 'exec ooimpress "$@"')
add_files(path_mime_types, 'application_vnd.oasis.opendocument.presentation', 'exec ooimpress "$@"')
