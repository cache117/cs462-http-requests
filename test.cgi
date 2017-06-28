#!/usr/bin/env python

import os
import sys

def redirect_on_query_strings():
    query_param = os.environ.get("QUERY_STRING", "No Query String in url")

    if query_param == "repo":
        print("Location:http://github.com")
        print # to end the CGI response headers.


    if query_param == "search":
        print("Location:http://google.com")
        print # to end the CGI response headers.


    if query_param == "face":
        print("Location:http://facebook.com")
        print # to end the CGI response headers.
        
def print_html_body():
    print "Content-Type: text/html"
    print "Cache-Control: no-cache"
    print

    print "<html><body>"

    print "<h1>Headers</h1>"

    for headername, headervalue in os.environ.iteritems():
        if headername.startswith("HTTP_"):
            print "<p>{0} = {1}</p>".format(headername, headervalue)

    print "<h1>Query String</h1>"

    print os.environ.get("QUERY_STRING", "No Query String in url")

    print "<h1>POST Body</h1>"
    print sys.stdin.read()

    print "</html></body>"
    

redirect_on_query_strings()
print_html_body()
