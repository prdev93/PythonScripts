#!/usr/bin/env python
#Program to print the name and years in which he/she will become 100 years old
import sys
name=sys.argv[1]
age=int(sys.argv[2])
diff=100-age
print 'Hello',name,'will be 100 in',diff,'years'
