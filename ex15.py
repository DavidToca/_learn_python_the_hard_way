from sys import argv

if len(argv) <=1:
    print "To run this file, use a filename as parameter."
    exit(1)

script, filename = argv

file = open(filename)

print "Here's your file %r:" % filename
print file.read()

print "Type the filename again:"
file_name = raw_input("> ")

file = open(file_name)

print file.read()