import sklearn
from htmlparser.py import mlSamplers

def load_mlDatadict(self):
		file = open('mlData_dict.pkl', 'rb')
		self.mlData = pickle.load(file)


load_mlDatadict()