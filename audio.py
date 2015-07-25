from subprocess import call

# College
shitOnAndrew = 1133225216703161
doItForTheStickers = 1471967949715240

# LO
actuallyInTown = 976367965717672

# SET THIS TO CHANGE WHICH GROUP TO FOLLOW
compInt = actuallyInTown

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


# Concatenate each audio file into a single file (using sox)
command = ["sox"]
for c in range(0, i):
   command.append(str(c) + ".aiff")
command.append("out.aiff")
call (command)

