import os
import sys

path = "C:/Users/Gebruiker/Documents/GitHub/misc/python"

for filename in os.listdir(path):
	filenamer = filename.replace(" ", "_")
	os.rename(path + "/" + filename, path + "/" + filenamer)