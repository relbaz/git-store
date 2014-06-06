#!/bin/python

import codecs
import fileinput

print "sed -r '"
for line in fileinput.input():
    s = line.strip().split("\t")
    newlabel = s[0]
    if len(s) > 1:
        oldlabels = "|".join(s[1:])
        print "s/^(%s)(\W+)/%s\\2/" % (oldlabels, newlabel)
        print "t skip"
        print ""
    else:
        print "s/^(\w+)(\W+)/%s\\2/" % newlabel
        print ":skip"

print "'"

