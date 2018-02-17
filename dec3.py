#from pyzbar.pyzbar import decode, ZBarSymbol

#import zbar

from PIL import Image
from contextlib import closing
from videosequence import VideoSequence
import progressbar
from PIL import ImageEnhance
#import numpy
numlist = []
import subprocess

print "Start decoding\n"
print "----------------------"

dataset = set()

with closing(VideoSequence("slow18-150.mp4")) as frames:
	print "Decoding: ", len(frames), " frames\n\n"
	curframe = 0
	bar = progressbar.ProgressBar(maxval=len(frames), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	bar.start()
	while curframe < len(frames):
		#frame = ImageEnhance.Sharpness(frame)
		#frame = frame.enhance(4.0)
		#frame = ImageEnhance.Contrast(frame)
		#frame = frame.enhance(2.0)
		frame = frames[curframe]
		frame.save("curframe.jpg")
		#print curframe
		try:
			result = subprocess.check_output(["zbarimg","curframe.jpg"], stderr=subprocess.STDOUT)
		except:
			curframe += 1
			continue;
		parts = result.split("QR-Code:")
		for part in parts:
			subparts = part.split('\n')
			for subpart in subparts:
				if ',' in subpart:
					num, data = subpart.split(',',1)
					if num not in numlist:
						numlist.append(int(num))
						dataset.add((int(num),data))
				
		bar.update(curframe)
		curframe += 1
print "\n\n--------------"
print "DONE!"
print "--------------"

numlist.sort()
numset = set(numlist)

perc = 100.0 - float(len(numset)) / (float(numlist[-1] + 1)) * 100.0

print "Perc missing: ", perc

dataset = sorted(dataset, key=lambda tup: tup[0])
#print dataset
with open("output2.txt", 'w') as f:
	for num, data in dataset:
		f.write(data)
#		print data