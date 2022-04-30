from pydub import AudioSegment
import os
import requests
from PIL import Image

def reqDL(link, name):
	r = requests.get(link)
	f = open(name, 'wb')
	f.write(r.content)
	f.close


reqDL("https://cdn.discordapp.com/attachments/947100010959470595/962825939958505502/silence.wav", "silence.wav")
reqDL("https://cdn.discordapp.com/attachments/947100010959470595/962825940117880912/tone.wav", "tone.wav")
reqDL("https://cdn.discordapp.com/attachments/947100010959470595/962825940478603295/delimiter.wav", "delimiter.wav")

silc = AudioSegment.from_wav("silence.wav")
tone = AudioSegment.from_wav("tone.wav")
delm = AudioSegment.from_wav("delimiter.wav")

os.remove("silence.wav")
os.remove("tone.wav")
os.remove("delimiter.wav")

reqDL("https://cdn.discordapp.com/attachments/833115587013115934/962836280020975667/qrcode.png", "image.png")

im = Image.open("image.png")
px = im.load()
wi, he = im.size

bl = [1, (0, 0, 0), (0,0,0,255)]
wh = [0, (255, 255, 255), (255,255,255,255)]

comb = AudioSegment.empty()

for _h in range(he):
	for _w in range(wi):
		if px[_w, _h] in bl: comb += tone
		elif px[_w, _h] in wh: comb += silc
		else: raise Exception('Invalid color')
	if _h != he - 1: comb += delm

comb.export("res.wav", format = "wav")

os.remove("image.png")
