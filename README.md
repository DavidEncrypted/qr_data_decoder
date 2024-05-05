# Qr Data Decoder
by David Schep

Exfiltrate data from an airgapped machine by displaying the data as base64 encoded qrcodes. QRcodes will be flashed on the display, film the display with any camera. Extract the data later.

Inspired by the community project Optical Data exfiltration from Hak5
Both the payload html and js are originaly from bg-wa: https://github.com/bg-wa/QRExtractor

### Installing
```
git clone https://github.com/DavidEncrypted/qr_data_decoder
sudo apt-get install zbar-tools
sudo pip install videosequence pillow progressbar
sudo apt-get install gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 python-gi python3-gi libgstreamer1.0-dev gstreamer1.0-plugins-good
```
### Usage
```
decoder.py (videofile) (outputfile.txt)
```
Usage of QR generator:
```
Open Payload/index.html in any browser
Select file to encode
bg-wa's javascript will generate the qr codes
Use the playback function to play the qr codes back
```
The generator script was edited slightly:
1. The playback now plays more than 1 qr at a time
2. All QRs have a number in front of the encoded data, this is very helpfull for the decoding

How many QRs should be played back at a time and how fast can be adjusted in main.js
Recommended parameters:
```
var qr_string_size = 169; //This value makes sure all qr codes use as all their data. More data per QR = Less QR's total
var qr_image_size = 200;
var playback_delay = 150; //150 has had the best results
var playback_amount = 10; //10 has had the best results
```
150 ms between QRs was the must reliable but still very fast. Remember to be able to decode the original file, 0% of QR codes can be missing. So if the recording was of a bad quality the decoder wont be able to find all QRs.

Tips:

1. Try to record the QRs in such a way that they fill the entire vieuwfinder.
2. The higher quality the recording had the more succesful the decoding will be
3. A higher refreshrate might increase succes. But personally experimenting with this has not been very succesfull
4. If you are capable of recording in very high resolution, it might be posible to record more that 10 QRs at a time. maybe a grid of 3 x 8 to fill the entire screen.

