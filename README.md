# Qr Data Decoder
by David Schep

Inspired by the community project Optical Data exfiltration from Hak5
Both the payload html and js are originaly from bg-wa: https://github.com/bg-wa/QRExtractor

### Installing
```
git clone https://github.com/DavidEncrypted/qr_data_decoder
sudo apt-get install zbar-tools
sudo pip install videosequence
sudo pip install pillow
sudo apt-get install gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 python-gi python3-gi libgstreamer1.0-dev gstreamer1.0-plugins-good
```
### Usage
```
decoder.py (videofile) (outpufile.txt)
```
