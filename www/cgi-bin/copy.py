#!C:\Python27\python.exe

"""
A simple form to upload a file with allowed extensions
"txt,htm,html,png,gif,jpg,ico,zip,rar,avi,mpg,rm,ram,wma,mp3,wav,pdf,doc,ppt"
to directory "../upload" (see ***SCRIPT PARAMETERS***)
Copyright (C) Georgy Pruss 2003,2004
Tested on Windows XP Home/Apache 2.0.43/Python 2.3
"""

# The upload form
# 1st parameter - (this) script name
# 2nd parameter - file field name
the_form = """
<FORM METHOD="POST" ACTION="%s" enctype="multipart/form-data">
<INPUT TYPE=FILE NAME="%s" size=50>
<INPUT TYPE="SUBMIT" VALUE="Upload">
</FORM>
"""


try:
  import msvcrt,os
  msvcrt.setmode( 0, os.O_BINARY ) # stdin  = 0
  msvcrt.setmode( 1, os.O_BINARY ) # stdout = 1
except ImportError:
  pass


print "Content type: text/html"
print

import sys, os, traceback, re
import cgi
import cgitb; cgitb.enable()


def strip_path( fpname ):
  """strip off leading path and drive stuff from dos/unix/mac file full name
  takes care of '/' ':' '\' '%2f' '%5c' '%3a'
  """
  fname = re.sub( r"(%(2f|2F|5c|5C|3a|3A))|/|\\|:", '/', fpname )
  delim = fname.rfind( '/' ) # -1 for not found, will return full fname
  return fname[delim+1:]


def check_ext( file_name, ext_set ):
  ext = file_name.rfind('.')
  if ext < 0:
    return False
  ext = file_name[ext+1:].lower()
  # was re.match( '^(gif)|(jpg)|(zip)$', ext, re.I )
  exts = ext_set.lower().split(',')
  for good_ext in exts:
    if ext == good_ext:
      return True
  return False


class UploadException:
  def __init__(self,rsn): self.reason = rsn

NO_FILE_FIELD = -1
NO_FILENAME   = -2
BAD_EXTENTION = -3
NO_FILE       = -4


def process_fileitem( file_item_name, local_file_path = './', allowed_file_types = 'jpg' ):
  """Gets file from form field file_item_name and saves it with the original
  file name to local_file_path. Returns (file_length,file_name) if success.
  Otherwise raise UploadException( NO_FILE_FIELD|NO_FILENAME|BAD_EXTENTION|NO_FILE )
  """

  form = cgi.FieldStorage()
  if not form.has_key( file_item_name ):
    raise UploadException( NO_FILE_FIELD )

  file_item = form[ file_item_name ]

  if not file_item.filename:
    raise UploadException( NO_FILENAME )

  remote_file_name = file_item.filename
  file_name = strip_path( remote_file_name )

  if not check_ext( file_name, allowed_file_types ):
    raise UploadException( BAD_EXTENTION )
  print "file name "+file_name
  local_file_name = os.path.join( local_file_path, file_name )
  print "local file name " + local_file_name
  if not file_item.file:
    raise UploadException( NO_FILE )

  data = file_item.file.read( 5*1024*1024 ) # max 5 megabyte
  # or data = fileitem.value
  # or data = form.getvalue( file_item_name, "" )
  fstrm = open( local_file_name, "wb" )
  fstrm.write( data )
  fstrm.close()

  return (len(data), file_name)


print "<html><head><title>Upload form</title></head><body>"

try:

  # ***SCRIPT PARAMETERS***
  file_field_name = "filename"
  loc_path = "E:\Ampps\www\pics\memberphotos"
  file_types = "jpg,png,jpeg,gif"

  try:

    flen, fname = process_fileitem( file_field_name, loc_path, file_types )
    print '%d bytes received to <a href="%s/%s">%s</a>' % \
          (flen, loc_path, fname, fname)

  except UploadException, ex:

    if ex.reason == NO_FILE_FIELD or ex.reason == NO_FILENAME:
      print "<p>Browse for file to upload.</p>"
    elif ex.reason == BAD_EXTENTION:
      print "<p>Illegal file, only %s allowed.</p>" % file_types
    else: # NO_FILE
      print "<p>No file received. Please repeat.</p>"
    print the_form % (strip_path( __file__ ), file_field_name)

except:

  print "<pre style='color:red; background:white;'>"
  sys.stderr = sys.stdout
  traceback.print_exc()
  print "</pre>"

print "</body></html>"


# EOF
