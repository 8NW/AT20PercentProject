import sklearn
import pickle
import requests
# import urllib2
import urllib3
#from googletrans import Translator
from os import system
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from htmlparser import mlSamplers
from HTMLParser import HTMLParser


class MyHTMLSummarizer(HTMLParser):
	summarized = []
	collected = []
	tags = []
	maxDIVS = 40
	mlData = []
	# translator = Translator()

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
		req = http.request('GET', url)
		# response = urllib2.urlopen(req)
		# the_page = response.read()

		# req = requests.get(url)
		# # print(req.text)
		# the_page = req.text

		self.feed(r)



	def handle_data(self, data):
		numTags = []
		moddedTags = self.tags
		
		for t in moddedTags:
			try:
				numTags.append(self.htmltags[t])
			except(KeyError): # adds a  new number to the tag dict if it encounters an unknown tag
				self.htmltags[t] = len(self.htmltags)
				numTags.append(self.htmltags[t])


		convertedData = data.replace('\r', '')
		convertedData = convertedData.replace('\n', '')

		sample = mlSamplers(numTags, convertedData)
		dataList, labelList = sample.sampleToList()
		label = self.trained.predict([dataList])[0]
		sample.label = label

		if sample.label != 0 and sample.label!=10:
			self.collected.append(sample)

		# print(sample.label)


# -----------------------------------------------
	def summarize_site(self, website):
		index = 0

		for i in self.collected:

			if index == 0:
				if i.label == 1:
					if i.data != '':
						self.summarized.append([i])
						self.summarized.append([])
						index+=1

					elif i.data == '':
						self.summarized.append([website])
						self.summarized.append([])
						index+=1
				else:
					self.summarized.append([website])
					self.summarized.append([])
					index+=1


			elif i.label == 7:
				self.summarized[1].append(i)

			else:
				if i.label == 9 or i.label == 13 or i.label == 4:
					index +=1
					self.summarized.append([])
					self.summarized[index].append(i)
				else: 
					self.summarized[index].append(i)

	def summarize_top_level(self):
		
		print("Welcome to " + self.summarized[0])

		if len(self.summarized) >= 2:
			print("This website contains " + (len(self.summarized)-1) + "bodies. ")
			for i in len(self.summarized):
				if i == 0:
					pass
				elif i == (len(self.summarized) -1):
					print(" and " + (i+1) + " " + str(self.summarized[i][0]) + ".")
				else: print(""+ (i+1) + " " +  str(self.summarized[i][0]) + ", ")
			print("If you would like to hear again hit enter without a number. Otherwise please type the number associated with the body and hit enter.")
			userIndex = input()
			if userIndex == "":
				summarize_top_level()
			else:
				if (int(userIndex)+1) < len(self.summarized):
					indexedInput = (int(userIndex)+1)
					summarize_body_level(indexedInput)

				else:
					print("Sorry. That was not a valid input.")
					summarize_top_level()
			


	def summarize_body_level(self, inputIndex):
		for i in self.summarized[inputIndex]:
			strOfI = str(i)



 
#-----------------------------------------------	
	# def summarize_top_level(self):
	# 	system('say' + (translator.translate("Welcome to ", dest=translator.detect(self.summarized[0])) + self.summarized[0]))
	# 	if len(self.summarized) >= 2:
	# 		system('say' + (translator.translate("You have " + str(len(self.summarized)) + "bodies.", dest=translator.detect(self.summarized[0])) + self.summarized[0]))
	# 		for i in len(self.summarized):
	# 			system('say' + self.summarized[i][0].oData )




	# def summarize_body_level(self, inputIndex):



	# def summarize_top_level(self):
	# 	for i in self.summarized:
	# 		strOfI = str(i[0])
	# 		# encodedI = strOfI.encode('utf-8')
	# 		print(strOfI)
			# for x in i:
			# 	print(str(x))s
			# 	system('say ' + str(x))
			
		

# -----------------------------------------------


if __name__ == '__main__':
	summarizer =  MyHTMLSummarizer()
	summarizer.load_tagdict('tags_dict.pkl')
	summarizer.load_labelsdict()
	summarizer.load_mlDatadict()
	summarizer.load_trained()

	#print(parser.htmltags)
	website = 'https://www.google.com/search?q=godaklsjf&oq=godaklsjf&aqs=chrome..69i57.1204j0j1&sourceid=chrome&ie=UTF-8'
	summarizer.handle_page(website)

	summarizer.summarize_site(website)
	# summarizer.summarize_top_level();

	for i in summarizer.collected:
		print(i.convert(summarizer.labelDict))
		# system('say ' + i.oData)

		














