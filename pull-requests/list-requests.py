#
# List open pull requests with some additional data
#
import sys
import os
from github import *
sys.path.append(os.path.relpath(".."))
import gitlogin
g = gitlogin.login()
o =g.get_organization("dealii")
r = g.get_repo("dealii/dealii")
for p in r.get_pulls():
  print p.title
  print "    ", p.created_at
  print "    ", p.head.label, "->", p.base.label
  print "    ", p.html_url
  if (p.milestone):
    print "    ", p.milestone.title

    
