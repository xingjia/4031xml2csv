from xml.sax.handler import ContentHandler, DTDHandler

class Handler(ContentHandler,DTDHandler):
	"""
	A handler to deal with elements in XML
	"""

	def __init__(self):
		self.tempData = dict()
		self.entry = ''
		self.currentNode = ''
		self.pubId = 0
		self.authorId = 0
		self.publication = ['article','inproceedings','proceedings','book','incollection','www']
		self.fieldType = ['author','editor','title','booktitle','pages','year','address','journal','volume','number','month','url','ee','cdrom','cite','publisher','note','crossref','isbn','series','school','chapter']
		self.authors = {}
		self.newAuthor = False
		# self.output = open('nodes.csv','a')


	def startElement(self,name,attrs):
		self.currentNode = name
		if name in self.publication:
			self.tempData.update({'pubId':self.pubId})
			self.tempData.update({'pubKey':'\"'+attrs.getValueByQName('key')+'\"'})

	def characters(self,characters):
		if len(characters) > 1:
			if self.currentNode == 'author':
				print self.pubId, characters
				if(self.authors.get(characters,-1) == -1):
					self.authors[characters] = self.authorId
					f = open('author.csv','a')
					f.write(str(self.authorId)+','+characters+'\n')
					f.close()
					self.authorId+=1

				f = open('authored.csv','a')
				f.write(str(self.authors.get(characters))+','+str(self.pubId)+'\n')
				f.close()
			self.tempData[self.currentNode] = '\"'+characters+'\"'

	def endElement(self,name):	
		self.currentNode = ''
		if name in self.publication:
			self.entry =  str(self.tempData.get('pubId',''))+','+self.tempData.get('pubKey','')+','+self.tempData.get('title','')+','+self.tempData.get('year','')+','+self.tempData.get('name','')+'\n'
			f = open('publication.csv','a')
			f.write(self.entry.encode('utf-8'))
			f.close()
			if name == 'article':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('journal','')+','+self.tempData.get('number','')+','+self.tempData.get('volumn','')+','+self.tempData('month','')+'\n'
				f = open('article.csv','a')
				f.write(self.entry.encode('utf-8'))
				f.close()
			elif name == 'inproceedings':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('booktitle','')+','+self.tempData.get('editor','')+'\n'
				f = open('inproceedings.csv','a')
				f.write(self.entry.encode('utf-8'))
			elif name == 'proceedings':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('booktitle','')+','+self.tempData.get('editor','')+'\n'
				f = open('proceedings.csv','a')
				f.write(self.entry.encode('utf-8'))
			elif name == 'book':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('isbn','')+','+self.tempData.get('publisher','')+'\n'
				f = open('book.csv','a')
				f.write(self.entry.encode('utf-8'))
			elif name == 'incollection':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('isbn','')+','+self.tempData.get('booktitle','')+','+self.tempData.get('publisher','')+'\n'
				f = open('incollection.csv','a')
				f.write(self.entry.encode('utf-8'))
			elif name == 'www':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('url','')+','+self.tempData.get('editor','')+'\n'
				f = open('www.csv','a')
				f.write(self.entry.encode('utf-8'))
				f.close()

			self.tempData = {}
			self.pubId += 1


