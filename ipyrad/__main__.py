#!/usr/bin/env python2
""" the main CLI for calling ipyrad """

from __future__ import print_function, division  # Requires Python 2.7+ 
import argparse
import pkg_resources




def parse_params():
    """ parse the CLI arguments """
    ## create a default Assembly object
    params = open(paramsfile).readlines()

    xpoint = 3
    print(xpoint, "CLI not ready yet")


def parse_command_line():
	""" Parse CLI. Only three options now. """
	## -p  choose params file
	## -s  subselect steps
	## -n  create new params file
	print("not yet")


if __name__ == "__main__": 
    
    ## parse params file input
    parse_params()

    ## 
