#! /usr/bin/env python

from os.path import dirname, realpath, abspath, join
from os import chdir, getcwd
from glob import glob
from re import compile, DOTALL
from subprocess import check_output

ROOT_PATH = abspath(join(dirname(realpath(__file__)), '../..'))
SLIDES_PATH = join(ROOT_PATH, 'slidedeck')
SRC_PATH = join(SLIDES_PATH, 'src')
CODE_PATH = abspath(join(ROOT_PATH, 'code'))

LISTING_RE = compile(r'\$LIST\((.+)\)')
EXEC_RE = compile(r'\$EXEC\((.+)\)')
TILDE_RE = compile(r'(~)(.+?)(~)', DOTALL)
TILDE_SUB = r'<span id="chighlight">\2</span>'
LT_RE = compile(r'<')
LT_SUB = r'&lt;'

def copy(infn):
  print 'copying ' + infn
  with open(infn) as infile:
    outfile.write('<!-- {} -->\n'.format(infn.split('/')[-1]))
    inlines = infile.readlines()
    outfile.writelines([do_macro(line) for line in inlines])
    outfile.write('\n')

def do_macro(line):

  m = LISTING_RE.search(line)
  if m:
    return do_list(m.groups()[0])

  m = EXEC_RE.search(line)
  if m:
    return do_exec(m.groups()[0])

  return line

def get_div(precode):
  cssclass = 'terminal' if precode.count('\n') < 31 else 'terminal-scroll'
  return '''
      <div class="{}">
        <pre><code>{}</code></pre>
      </div>
  '''.format(
      cssclass,
      precode
      )


def do_list(arg):
  fn = join(CODE_PATH, arg)
  print 'inserting listing of {}'.format(fn)
  with open(fn) as listing:
    return '<!-- listing of {} -->\n {}'.format(
        arg,
        get_div(
          TILDE_RE.sub(
            TILDE_SUB,
            LT_RE.sub(
              LT_SUB,
              listing.read()
            )
          )
        )
    )

def do_exec(arg):

  path, cmd = arg.split(',')
  cmd = cmd.strip()

  chdir(join(ROOT_PATH, path))

  print 'inserting results of "{}" executed in {}'.format(
      cmd,
      getcwd()
      )

  cmdargs = cmd.split(' ')

  return '<!-- execution of {} -->\n{}'.format(
      arg,
      get_div('{}/ > {}\n\n{}'.format(
        path,
        cmd,
        check_output(cmdargs)
  )))

def fncmp(a, b):
  """
  cmp-return-compatible function that behaves such that
  'slide-1.html < <slide-2.html' < 'slide-10.html' < 'slide-10-1.html' etc.
  """

  def listify(fn):
    """
    given fn='slide-1-3-5.html', returns [1, 3, 5]
    """
    l = fn.split('-')
    if not l[-1].endswith('.html'): raise ValueError
    # strip 'slide-' and '.html'
    l[-1] = l[-1][:-5]
    return [int(i) for i in l[1:]]

  # builtin cmp does what we want with lists of ints
  return cmp(listify(a),
             listify(b))

def allslides():
  return sorted(glob(join(SRC_PATH, "slide*.html")), fncmp)

if __name__ == '__main__':
  with open(join(SLIDES_PATH, 'index.html'), 'w') as outfile:

    copy(join(SRC_PATH, 'head.html'))

    for slidefile in allslides():
      copy(slidefile)

    copy(join(SRC_PATH, 'tail.html'))

