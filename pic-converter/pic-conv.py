#FINAL BUILD
import fnmatch
import os
import shutil
import glob
import time
# also requires Linux's Imagemagick suite

# First copy files from read-only source to temp directory
srcDir = '/path/to/source/pics/'
def copyFiles():
 for root, dirs, files in os.walk(srcDir):
     newdest = root.replace('/sourcePath/','/destPath/')
     if '2012-' in root: # hard coded directory
       print "Creating Target Directory:",newdest
       os.mkdir(newdest)
       for file in files:
        if file[-4:].upper() == '.JPG':
		print "Copying",file,"to",os.path.join(newdest, file)
                shutil.copy(os.path.join(root, file), os.path.join(newdest, file))

#Now create directories for orig path, used for backup of original files
paths = []
for item in [x[0] for x in os.walk("/destination/path/root/dir/")]:
   if item != ".":
     paths.append(item)
#Create the orig targets
for sdir in paths:
   os.chdir(sdir)
   print "making:",sdir + "/orig"
   try:
     os.mkdir("orig")
   except Exception as error:
     print error

#Finally convert files
for item in paths:
  if item !='/sourcePath/' or item[-5:] != '/orig':
     print "Converting in directory:",item
     os.chdir(item)
     os.system("for file in `ls *.JPG`;do convert $file -resize 50% `echo $file|sed 's/\.JPG//'`-conv.JPG && echo $file && mv $file orig/;done")