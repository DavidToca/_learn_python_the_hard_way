#A real warrior must have arguments to defend himself
from sys import argv

print "Wellcome, This is ", argv[0]

if len(argv) <= 1:
  print "YOU SIR HAVE NO ARGUMENTS!"
else:
  print "I do not agree with what you have to say, but I'll defend to the death your right to say it."

