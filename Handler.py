from xml.sax.handler import ContentHandler, DTDHandler

class Handler(ContentHandler,DTDHandler):
	"""
	A handler to deal with elements in XML
	"""

	def __init__(self):
		self.tempData = {}
		self.entry = ''
		self.currentNode = ''
		self.pubId = 0
		self.authorId = 0
		self.publisherId = 0
		self.publication = ['article','inproceedings','proceedings','book','incollection','www']
		self.fieldType = ['author','editor','title','booktitle','pages','year','address','journal','volume','number','month','url','ee','cdrom','cite','publisher','note','crossref','isbn','series','school','chapter']
		self.authors = {}
		self.publishers = {}

		self.authorFile = open('author.csv','a')
		self.authoredFile = open('authored.csv','a')
		self.publisherFile = open('publisher.csv','a')
		self.publishedFile = open('published.csv','a')
		self.articleFile = open('article.csv','a')
		self.proceedingsFile = open('proceedings.csv','a')
		self.inproceedingsFile = open('inproceedings.csv','a')
		self.bookFile = open('book.csv','a')
		self.incollectionFile = open('incollection.csv','a')
		self.wwwFile = open('www.csv','a')
		self.publicationFile = open('publication.csv','a')


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
					self.authorFile.write(str(self.authorId)+','+characters+'\n')
					self.authorId+=1

				self.authoredFile.write(str(self.authors.get(characters))+','+str(self.pubId)+'\n')

			if self.currentNode == 'publisher':
				print self.pubId, characters
				if(self.publishers.get(characters,-1) == -1):
					self.publishers[characters] = self.publisherId
					self.publisherFile.write(str(self.publisherId)+','+characters+'\n')

					self.publisherId+=1

				self.publishedFile.write(str(self.publishers.get(characters))+','+str(self.publisherId)+'\n')

			self.tempData[self.currentNode] = '\"'+characters+'\"'

	def endElement(self,name):	
		self.currentNode = ''
		if name in self.publication:
			self.entry =  str(self.tempData.get('pubId',''))+','+self.tempData.get('pubKey','')+','+self.tempData.get('title','')+','+self.tempData.get('year','')+','+self.tempData.get('name','')+'\n'
			self.publicationFile.write(self.entry.encode('utf-8')

			if name == 'article':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('journal','')+','+self.tempData.get('number','')+','+self.tempData.get('volumn','')+','+self.tempData('month','')+'\n'
				self.articleFile.write(self.entry.encode('utf-8'))
			elif name == 'inproceedings':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('booktitle','')+','+self.tempData.get('editor','')+'\n'
				self.inproceedingsFile.write(self.entry.encode('utf-8'))
			elif name == 'proceedings':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('booktitle','')+','+self.tempData.get('editor','')+'\n'
				self.proceedingsFile.write(self.entry.encode('utf-8'))
			elif name == 'book':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('isbn','')+','+self.tempData.get('publisher','')+'\n'
				self.bookFile.write(self.entry.encode('utf-8'))
			elif name == 'incollection':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('isbn','')+','+self.tempData.get('booktitle','')+','+self.tempData.get('publisher','')+'\n'
				self.incollectionFile.write(self.entry.encode('utf-8'))
			elif name == 'www':
				self.entry = str(self.tempData.get('pubId',''))+','+self.tempData.get('url','')+','+self.tempData.get('editor','')+'\n'

			self.tempData = {}
			self.pubId += 1


