from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
from contextlib import closing
from videosequence import VideoSequence
import progressbar
from PIL import ImageEnhance

numlist = []


print "Start decoding\n"
print "----------------------"

with closing(VideoSequence("bigbig.mp4")) as frames:
	print "Decoding: ", len(frames), " frames\n\n"
	curframe = 0
	bar = progressbar.ProgressBar(maxval=len(frames), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	bar.start()
	while curframe < len(frames):
		frame = frames[curframe]
		#frame = ImageEnhance.Sharpness(frame)
		#frame = frame.enhance(4.0)
		#frame = ImageEnhance.Contrast(frame)
		#frame = frame.enhance(2.0)

		data = decode(frame , symbols=[ZBarSymbol.QRCODE])
		for i in range(0,len(data)):
			if len(data[i][0]) > 4:
				#print data[i][0]
				num, data = data[i][0].split(',',1)
				if num not in numlist:
					
					numlist.append(int(num))
		bar.update(curframe)
		curframe += 1
print "\n\n--------------"
print "DONE!"
print "--------------"

numlist.sort()
numset = set(numlist)
#misset = set(range(0,numlist[-1]+1)) - numset
#misset = sorted(misset)
for i in numset:
	print i
#print "MISSING: "
#for j in misset:
	#print j

perc = 100.0 - float(len(numset)) / float(numlist[-1]) * 100.0

print "Perc missing: ", perc