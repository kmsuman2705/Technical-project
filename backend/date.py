#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

import subprocess as s
out=s.getoutput("date")
print("<pre>")
print(out)
print("</pre>")

print()
print()
print("<form action= HTTP://'your_ip'/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")
