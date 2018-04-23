import urllib3
import pickle
from HTMLParser import HTMLParser


class mlSamplers():
	def __init__(self, numTags, nData):
		self.numTags = numTags
		self.data = nData
		self.label = None

	def convert(self, labelDict):
		return "LABEL: ", labelDict[self.label], ", DATA: ", self.data

	def __str__(self):
		return self.data.encode('utf-8')

	def howManyOf(self, stringType):

		dataStringType = 0
		dataStringTypeNum = (self.data).count(stringType)

		if dataStringTypeNum > 0:
			dataStringType = dataStringTypeNum


		return dataStringType

	def sampleToList(self):
		maxDIVS = 40

		moddedTags = self.numTags

		#---Adds a -2 onto the array to create a uniform modded tags array length
		if(len(self.numTags)>maxDIVS):
			moddedTags = self.numTags[-maxDIVS:]

		moddedTags = [-2]*(maxDIVS-len(moddedTags)) + moddedTags


		label = self.label
		data = []

		#---Creates a length identifier for data
		dataLength = 0
		dataLengthNum = len(self.data)

		if dataLengthNum > 0:
			dataLength = dataLengthNum

		data.append(dataLength)

		#---Checks for the number of upper case letters
		dataUpperCase = 0
		dataUpperCaseNum = sum(1 for c in (self.data) if c.isupper())

		if dataUpperCase > 0:
			dataUpperCase = 0

		data.append(dataUpperCase)

		#---Checks for the number of lower case letters
		dataLowerCase = 0
		dataLowerCaseNum = sum(1 for c in (self.data) if c.islower())

		if dataLowerCase > 0:
			dataLowerCase = 0

		data.append(dataLowerCase)

		#---Checks for the number of certain symbols
		keyboardBasics = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890;/\{\}().?<>:'\"\\!@#$%^&*_+-=|`~ ")
		for key in keyboardBasics:
			if dataLength > 0:
				data.append( ( ( self.howManyOf(key) ) *1.0) / (dataLength*1.0))
				
			else:
				data.append(0)

			data.append((self.howManyOf(key)))

		


		#---Adds the data array to the modded tags array so that there is one machine learning readable array
		moddedTags+=data
		return moddedTags, label



class MyHTMLParser(HTMLParser):
	tags = []
	maxDIVS = 40
	mlData = []
	#translator = Translator()

	def load_tagdict(self, file_name):
		file = open(file_name, 'rb')
		self.htmltags = pickle.load(file)

	def load_labelsdict(self):
		file = open('labels_dict.pkl', 'rb')
		self.labelDict = pickle.load(file)

	def load_trained(self):
		file = open('trained.pkl', 'rb')
		self.trained = pickle.load(file)

	def load_mlDatadict(self):
		try: 
			file = open('mlData_dict.pkl', 'rb')
		 	self.mlData = pickle.load(file)
		except IOError: 
			self.mlData = ""


	def handle_starttag(self, tag, attrs):
		self.tags.append(tag)

	def handle_endtag(self, tag):
		 self.tags = self.tags[:-1]

	def handle_page(self, url): 
		http = urllib3.PoolManager()
		r = http.request('GET', url)

		self.feed(r.data)



	def handle_data(self, data):

		print()
		print()
		print()
		print("-------------------------------------------------")
		print()
		print("Encountered tags:", self.tags)
		print("-------------------------------------------------")
		print("Encountered some data  :", data)
		print("-------------------------------------------------")


		numTags = []
		moddedTags = self.tags

		for t in moddedTags:
			try:
				numTags.append(self.htmltags[t])
			except(KeyError):
				self.htmltags[t] = len(self.htmltags)
				numTags.append(self.htmltags[t])




		sample = mlSamplers(numTags, data)
		dataList, labelList = sample.sampleToList()
		print(self.trained.predict([dataList]))



		print(self.labelDict)
		label = raw_input()
		if  len(label) == 0:
			label = "0"

		label = int(label)


		if label not in self.labelDict.keys():
			self.labelDict[label] = raw_input()


		sample.label = label
		self.mlData.append(sample)



	def endPage(self):

		pkl_file = open('mlData_dict.pkl', 'wb')
		pickle.dump(self.mlData, pkl_file)

		pkl_file = open('labels_dict.pkl', 'wb')
		pickle.dump(self.labelDict, pkl_file)



if __name__ == '__main__':
	parser = MyHTMLParser()
	parser.load_tagdict('tags_dict.pkl')
	parser.load_labelsdict()
	parser.load_mlDatadict()
	parser.load_trained()

	#print(parser.htmltags)
	parser.handle_page('https://www.reddit.com/')
	parser.endPage()
