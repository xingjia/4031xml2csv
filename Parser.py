from xml.sax import make_parser
from Handler import Handler

f = open('partial.xml')
hd = Handler()
saxparser = make_parser()

saxparser.setContentHandler(hd)
saxparser.setDTDHandler(hd)
saxparser.parse(f)