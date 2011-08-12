#!/bin/bash
# Proper header for a Bash script.

# Check for root user login
if [ ! $( id -u ) -eq 0 ]; then
	echo "You must be root to run this script."
	echo "Please enter su before running this script again."
	exit 2
fi

IS_CHROOT=0 # changed to 1 if and only if in chroot mode
USERNAME=""
DIR_DEVELOP=""

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /srv directory only exists in chroot mode
if [ -d "/srv" ]; then
	IS_CHROOT=1 # in chroot mode
	DIR_DEVELOP=/usr/local/bin/develop 
else
	USERNAME=$(logname) # not in chroot mode
	DIR_DEVELOP=/home/$USERNAME/develop 
fi

# From Diet Swift Linux to Regular Swift Linux
echo "*****************************************************************"
echo "TRANSFORMING DIET SWIFT LINUX INTO REGULAR SWIFT LINUX"
# Add OpenOffice
sh $DIR_DEVELOP/openoffice/main.sh

# Add forensic packages
sh $DIR_DEVELOP/forensic/main.sh

# Change Conky
python $DIR_DEVELOP/regular/conky.py

# Change MIME-types to OpenOffice formats
python $DIR_DEVELOP/regular/mime.py

# Change ROX
# Change pb_antiX-ice files to show OpenOffice icons
python $DIR_DEVELOP/regular/rox.py


echo "FINISHED TRANSFORMING DIET SWIFT LINUX INTO REGULAR SWIFT LINUX"
echo "*****************************************************************"

exit 0
