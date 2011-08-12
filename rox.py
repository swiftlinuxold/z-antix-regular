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
	
# Change pb_antiX-ice files to show OpenOffice icons:
# /home/$USERNAME/.config/rox.sourceforge.net/ROX-Filer/pb_antiX-ice
# /etc/skel/.config/rox.sourceforge.net/ROX-Filer/pb_antiX-ice
# /usr/share/antiX-install/icewm/pb_antiX-ice

print 'Adding OpenOffice icons to the ROX pinboard desktop'

def change_text (pathdir):
	file_pb=pathdir+'/pb_antiX-ice'
	text=open(file_pb, 'r').read()
	text_old='</pinboard>'
	t1='<icon x="40" y="470" label="OO-Write">/usr/share/applications/ooo-writer.desktop</icon>\n'
	t2='<icon x="110" y="470" label="OO-Calc">/usr/share/applications/ooo-calc.desktop</icon>\n'
	t3='<icon x="180" y="470" label="OO-Impress">/usr/share/applications/ooo-impress.desktop</icon>\n'
	t4=text_old
	text_new=t1+t2+t3+t4
	text=text.replace(text_old, text_new)
	open (file_pb, 'w').write(text)

if (~is_chroot):
	change_text('/home/'+username+'/.config/rox.sourceforge.net/ROX-Filer')
change_text('/etc/skel/.config/rox.sourceforge.net/ROX-Filer')
if (is_chroot):
	change_text('/usr/share/antiX-install/icewm')
