from xml.sax.handler import ContentHandler, DTDHandler

class Handler(ContentHandler,DTDHandler):
	"""
	A handler to deal with elements in XML
	"""

	def __init__(self):
		self.inWWW = 0
		self.inArticle = 0
		self.inInproceedings = 0
		self.inProceedings = 0
		self.inBook = 0
		self.inIncollection = 0
		self.inPhdthesis = 0
		self.inMasterthesis = 0
		self.inWww = 0
		self.tempData = dict()
		self.entry = ''
		self.currentNode = ''
		self.publication = ['article','inproceedings','proceedings','book','incollection','www']
		self.fieldTYpe = ['author','editor','title','booktitle','pages','year','address','journal','volume','number','month','url','ee','cdrom','cite','publisher','note','crossref','isbn','series','school','chapter']
		# self.output = open('nodes.csv','a')


	def startElement(self,name,attrs):
		self.currentNode = name
		if name in self.publication:
			self.tempData.update({'pubKey':'\"'+attrs.getValueByQName('key')+'\"'})
		if name == 'article':self.inArticle = 1
		elif name == 'inproceedings':self.inInproceedings = 1
		elif name == 'proceedings': self.inProceedings = 1
		elif name == 'book':self.inBook = 1
		elif name == 'incollection':self.inIncollection = 1
		# elif name == 'phdthesis':self.inPhdthesis = 1
		# elif name == 'mastertheses':self.inMasterthesis = 1
		elif name == 'www':self.inWww = 1

	def characters(self,characters):
		if len(characters) > 1:
			self.tempData[self.currentNode] = '\"'+characters+'\"'

	def endElement(self,name):	
		self.currentNode = ''
		if name in self.publication:
			self.entry = self.tempData.get('pubKey','')+','+self.tempData.get('title','')+','+self.tempData.get('year','')+','
			if name == 'article':
				self.inArticle = 0
				f = open('article.csv','a')
				f.write(self.entry.encode('utf-8'))
			elif name == 'inproceedings':
				self.inInproceedings = 0
				f = open('inproceedings.csv','a')
				f.write(self.entry.encode('utf-8'))
			elif name == 'proceedings':
				self.inProceedings = 0
				f = open('proceedings.csv','a')
				f.write(self.entry.encode('utf-8'))
			elif name == 'book':
				self.inBook = 0
				f = open('book.csv','a')
				f.write(self.entry.encode('utf-8'))
			elif name == 'incollection':
				self.inIncollection = 0
				f = open('incollection.csv','a')
				f.write(self.entry.encode('utf-8'))
			# elif name == 'phdthesis':self.inPhdthesis = 0
			# elif name == 'mastertheses':self.inMasterthesis = 0
			elif name == 'www':
				self.inWww = 0
				self.entry += self.tempData.get('url','')+','+self.tempData.get('editor','')+'\n'

				f = open('www.csv','a')
				f.write(self.entry.encode('utf-8'))

			self.entry = ''
			self.tempData = {}


