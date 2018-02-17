from PIL import Image
from contextlib import closing
from videosequence import VideoSequence
import progressbar
import argparse
from PIL import ImageEnhance
numlist = []
import subprocess


parser = argparse.ArgumentParser(description="QR Code data reconstructor - made by David Schep, Encrypted. Inspired by prodicode and bg-wa");
parser.add_argument("video", help="Video file containing QR codes",
                    type=str);
parser.add_argument("output", help="The file to output the data to. (output is in base64)",
                    type=str)
args = parser.parse_args();


print("""\


   ____  _____  _____  ______ _____ ____  _____  ______ _____  
  / __ \|  __ \|  __ \|  ____/ ____/ __ \|  __ \|  ____|  __ \ 
 | |  | | |__) | |  | | |__ | |   | |  | | |  | | |__  | |__) |
 | |  | |  _  /| |  | |  __|| |   | |  | | |  | |  __| |  _  / 
 | |__| | | \ \| |__| | |___| |___| |__| | |__| | |____| | \ \ 
  \___\_\_|  \_\_____/|______\_____\____/|_____/|______|_|  \_\
                                                               
                                                                      
        by David Schep ;)
        https://github.com/DavidEncrypted

""");



print "Decoding Started!\n"

dataset = set()

with closing(VideoSequence("hak5qr.mp4")) as frames:
	print "Decoding: ", len(frames), " frames\n\n"
	curframe = 0
	bar = progressbar.ProgressBar(maxval=len(frames), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	bar.start()
	while curframe < len(frames):
		frame = frames[curframe]
		frame.save("curframe.jpg")
		
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
with open("output2.txt", 'w') as f:
	for num, data in dataset:
		f.write(data)
