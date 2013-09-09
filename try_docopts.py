#!/usr/bin/env python

'''
Docopts is wondrous.
'''

import sys
import docopt

opts = docopt.docopt("""\
Usage:
  PROG tcp <host> <port>
  PROG serial <port> [--baud=N]
""".replace('PROG', sys.argv[0]))

if opts['tcp']:
    print 'hack network stuff'
    print 'host:', opts['<host>']
    print 'port:', opts['<port>']
elif opts['serial']:
    print 'hack serial stuff'
    print 'port:', opts['<port>']
    if opts['--baud']:
        print 'baud:', opts['--baud']
