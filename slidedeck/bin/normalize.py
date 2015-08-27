#!/usr/bin/python

from os.path import join
from subprocess import check_call

from assemble import allslides, SRC_PATH

slidelist = list(reversed(list(enumerate(allslides()))))

for index, slide in slidelist:
  newfile = join(SRC_PATH, 'slide-{}.html'.format(index + 1000))
  print 'Moving {} to {}'.format(
      slide, 
      newfile)
  check_call([
    'git',
    'mv',
    slide,
    newfile
    ])
