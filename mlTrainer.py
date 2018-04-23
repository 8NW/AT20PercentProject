import sklearn
import pickle
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from htmlparser import mlSamplers

def load_mlDatadict():
		file = open('mlData_dict.pkl', 'rb')
		mlData = pickle.load(file)
		return mlData


def genDataSet(samplers):
	dataSet = []
	labelSet = []

	for t in samplers:
		data, label = t.sampleToList()

		dataSet.append(data)
		labelSet.append(label)

	return dataSet, labelSet
	




dataDict = load_mlDatadict()
dataSetList, labelSetList = genDataSet(dataDict)

print(labelSetList)

dataTrain, dataTest, labelTrain, labelTest = train_test_split(dataSetList, labelSetList, test_size = .20)

print(len(dataSetList))
print(len(labelSetList))

#-----------------------------------------------
learner = SVC(kernel = 'linear')
learner.fit(dataTrain, labelTrain)
accuracy = learner.score(dataTest, labelTest)
for i in range(len(labelTest)):
	print(labelTest[i] , ", " , learner.predict([dataTrain[i]]))
#-----------------------------------------------

print(str(accuracy*100) + "%")

pkl_file = open('trained.pkl', 'wb')
pickle.dump(learner, pkl_file)




