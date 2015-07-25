import sys
from subprocess import call
try:
   import xml.etree.cElementTree as ET
except:
   import xml.etree.ElementTree as ET

if len(sys.argv) == 1:
   print ("Don't forget to enter the name of the desired thread")
   exit(0)

#-----------------------------------------------#

tree = ET.ElementTree(file='threads.xml')
threads = {}
root = tree.getroot()
for child in root:
   threads[child.attrib["name"]] = child.text.strip()


compInt = int( threads[sys.argv[1]] )

#-----------------------------------------------#

def say(name, msg, count):
   voice = ""

   if name == "Minnal Kunnan":
      voice = "Daniel"
   elif name == "Russell Wong":
      voice = "Oliver"
   elif name == "Alex Kost":
      voice = "Lee"
   elif name == "Ryan Eakins":
      voice = "Tom"

   elif name == "ADMIN":
      voice = "Samantha"

   elif name == "Andrew James Hollister":
      voice = "Daniel"
   elif name == "Robert Wery":
      voice = "Oliver"
   elif name == "Brian Ruhele":
      voice = "Lee"
   elif name == "Sam Worth":
      voice = "Tom"

   elif name == "Andrew Pimentel":
      voice = "Daniel"
   elif name == "Nicholas Ross":
      voice = "Oliver"

   call (["say", "-v", voice, "-o", str(count)+".aiff", msg])


inFile = open('out.txt', 'r')

i = 0

for line in inFile:
   try:
      if int(line) == compInt:
         name = inFile.readline().replace("\n", "")
         message = inFile.readline().replace("\n", "")

         if message.startswith("http"):
            message = "LINK"
            name = "ADMIN"

         say(name, message, i)
         i = i + 1
         
   except ValueError:
      blah = 1

inFile.close()

if i == 0:
   print ("No files to convert to audio")
else:
   # Concatenate each audio file into a single file (using sox)
   command = ["sox"]
   for c in range(0, i):
      command.append(str(c) + ".aiff")
   command.append("out.aiff")
   call (command)

