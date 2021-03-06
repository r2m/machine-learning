from Reader import Reader
from FeaturesUtilityFunctions import wordCounter, countUniqueChars, countNumberOfChars, countUniqueWords, checkForRepetition, extractDataAsNumPyArray, extractLabelAsNumPyArray
import random 
from sklearn import svm
from sklearn.metrics import f1_score


def getFeature(example, label):
	"Construct feature vector" 
	feature = []
	# Calculate a number of features and put them into an array.
	# What features are relevant?
	# Are there any missing features?
	chars = countNumberOfChars(example)
	uniqueChars = countUniqueChars(example)
	weightedUniqueChars = uniqueChars/chars

	# Calculate some features based on the words 
	counterForWords = wordCounter(example)
	uniqueWords = countUniqueWords(counterForWords)
	hasRepetition = checkForRepetition(counterForWords)

	feature.append(uniqueWords)
	feature.append(hasRepetition)

	# Finally add the label
	feature.append(label)

	return feature

if __name__ == '__main__':
	reader = Reader()
	# Read the data from out example files
	badExamples = reader.read('bad.txt', '|')
	goodExamples = reader.read('good.txt', '|')

	# Aggregate the data into one array
	examples = badExamples + goodExamples

	# Label the data 0 for bad 1 for good examples.
	# 'labels' should be an array with the same length as 'examples' 
	# populated with 0, one for each entry in 'badExamples'
	# and 1 one for each entry in  'goodExamples' with 1. 
	# TODO Create a vector with labels according to the instruction above.
	labels = ...

	# Lets create the features we will use for analysis.
	featureVector = []
	for i in range(len(examples)):
		feature = getFeature(examples[i], labels[i])
		featureVector.append(feature)


	# Lets create two sets of data! One for training and
	# one for testing to see how good our algorithm was.
	# But first shuffle the list so that every run will be unique
	# TODO remove the shuffle... What is the result and why?
	random.shuffle(featureVector)

	# Split in half, maybe test to change this limit!
	cut = int(len(featureVector)/2)
	trainingSet = featureVector[:cut]
	evaluationSet = featureVector[cut:]

	# Extract the training data into numpy arrays so that we can use them for the machine learning algorithms.
	trainingData = extractDataAsNumPyArray(trainingSet)
	trainingLable = extractLabelAsNumPyArray(trainingSet)

	# Check http://scikit-learn.org/stable/modules/svm.html#svm-kernels for more kernels or write your own!
	#
	# The C parameter tells the SVM optimization how much you want to avoid misclassifying each training
	# example.
	#
	# For large values of C, the optimization will choose a smaller-margin hyperplane if that hyperplane
	# does a better job of getting all the training points classified correctly.
	#
	# Conversely, a very small value of C will cause the optimizer to look for a larger-margin separating 
	# hyperplane, even if that hyperplane misclassifies more points. 
	#
	# For very tiny values of C, you should get misclassified examples, 
	# often even if your training data is linearly separable.

	#TODO - try different values for C see what happens
	#TODO - try a differnet kernel and see if the results are different. Check out the link above
	C = 1.0
	svc = svm.SVC(kernel='linear', C=C, verbose=False).fit(trainingData, trainingLable)
	print 'Type of the support vector used: \n', type(svc)
	print 'Support Vector Classification: \n', svc

	# Extract the evaluation data into numpy arrays so that we can use them for the machine learning algorithms.
	evaluationData = extractDataAsNumPyArray(evaluationSet)
	evaluationLable = extractLabelAsNumPyArray(trainingSet)

	# Get the predicition
	predictedLable = svc.predict(evaluationData)

	# Let us evaluate the solution!
	score = 0
	for i in range(len(predictedLable)):
		if predictedLable[i] == evaluationLable[i]:
			score += 1

	percentage =  (float(score) / len(predictedLable)) * 100

	# Print results
	print 'Got %s out of %s that is roughly %.2f %% correct.' %(score, len(predictedLable), percentage)

	# The F1 score can be interpreted as a weighted average of the prediction and the actual data.
	# F1 score reaches its best value at 1 and worst score at 0.
	f1 = f1_score(evaluationLable, predictedLable, average='binary') 
	print f1










