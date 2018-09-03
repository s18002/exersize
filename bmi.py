#!/usr/bin/env python3

import cgi

print("Content-Type: text/html")
print("")

form = cgi.FieldStorage()

print("BMI")

if (not 'v1' in form) or (not 'v2' in form):
    print("""
        <form>
        tai: <input type="text" name="v1">kg  /
        sin: <input type="text" name="v2">m
        <input type="submit" value="BMI">
        </form>
    """)
else:
    v1 = form.getvalue("v1", "0")
    v2 = form.getvalue("v2", "0")
    try:
        ans = int(v1) / (int(v2) * int(v2))
    except:
        ans = 0
    print("<h1>", ans, "</h1>")
