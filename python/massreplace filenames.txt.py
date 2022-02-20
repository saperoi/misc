import os
import sys

path = "C:/Users/Gebruiker/Documents/GitHub/misc/python/redddit"

for filename in os.listdir(path):
	filenamer = filename.replace("Prolangs ", "")
	filenamer = filename.replace(".png.png", ".png")
	os.rename(path + "/" + filename, path + "/" + filenamer)