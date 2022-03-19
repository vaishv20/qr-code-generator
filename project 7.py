import pyqrcode
import png
from pyqrcode import QRCode
s = "www.google.com"
url = pyqrcode.create(s)
url.png('sun.png', scale = 6)