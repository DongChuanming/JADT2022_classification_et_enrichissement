# coding: utf8
#!/usr/sfw/bin/python

import csv, glob, os, re, sys, time
from io import open

# store in the folder variable the address of the folder containing this program
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

unitex = open(os.path.join(os.path.join(folder,"data-unitex"),"Dela_fr.txt"), "r", encoding='utf-8')

inflectedForms = {}

for line in unitex:
   regex = "^([^,]+)[,]([^.]*)[.]([^:]+):.*"
   res = re.search(regex, line)
   if res:
      token = res.group(1)
      lemma = res.group(2)
      if lemma == "":
         lemma = token
      POS = res.group(3)
      if lemma in inflectedForms:
         if token not in inflectedForms[lemma]:
            inflectedForms[lemma].append(token)
      else:
         inflectedForms[lemma] = [token]

print("Nb of lemmas: " + str(len(inflectedForms)))

# Consider all input texts
for file in glob.glob(os.path.join(os.path.join(folder,"data-unitex"),"list*.txt")):
   # Display the address of the file being treated
   print("Currently enriching list from file " + file)
   inputFile = open(file, "r", encoding='utf-8')
   outputFile = open(os.path.join(os.path.join(folder,"data-unitex"), "enriched-" + os.path.basename(file)), "w", encoding='utf-8')

   for row in inputFile:
      res = re.search("^([^\r\n]+)[\r\n]*$", row)
      if res:
         lemma = res.group(1)
         if lemma in inflectedForms:
            for inflectedForm in inflectedForms[lemma]:
               outputFile.writelines(inflectedForm + "\n")
   inputFile.close()
   outputFile.close()