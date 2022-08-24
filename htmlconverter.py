#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print ("please supply a file as parameter")
    exit(1)

path = sys.argv[1]
with open(path) as rfile:
    with open(path + ".new", "w") as wfile:
        for line in rfile:
            if (line == "\n"):
                continue
            wfile.write("\"" + line[:-1].replace("\"", "\\\"") + "\",\n")
            print("\"" + line[:-1].replace("\"", "\\\"") + "\",")
        wfile.write("\"\"")
        print("\"\"")
