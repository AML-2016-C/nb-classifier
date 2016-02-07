from __future__ import division
from nltk.corpus import stopwords
import csv
import nltk
import random


# Function which reads csv file. Converts category of tweets from string to int for future use.
def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i][1]=int(dataset[i][1])
	global stop_words
	stop_words=stopwords.words("english")
	#print stop_words			
	return dataset

#gets list of words and it's count of occurences in each category. Puts them into a table called freq_table
def getWords(data):
	freq_table=[]
	for i in range(N):
		freq_table.append(dict())
	for tweet,category in data:
		words=nltk.word_tokenize(tweet)
		list_words=filter(lambda x: x.lower() not in stop_words,words)
		#print list_words
		for w in list_words:
			w=w.lower()
			if(freq_table[category].__contains__(w)):
				freq_table[category][w]+=1
			else:
				freq_table[category][w]=1;	
	return freq_table			

#Splitting dataset randomly for training and testing purposes.
def getSets(trainSize):
	trainSet=[]
	testSet = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(testSet))
		trainSet.append(testSet.pop(index))
	return [trainSet, testSet]		

#Supposed to divide occurence of each word in a category with total number of words in that category. 
#If i don't divide, accuracy around 97%. If i divide, accuracy around 20%. Why? Idk
def updateFreqTable(freq_table):
		num_words=[]
		for i in range(N):
			num_words.append(sum(freq_table[i].values()))
		#print len(freq_table[0])
		#print len(freq_table[1])	
		for i in range(N):
			for j in freq_table[i]:
				freq_table[i][j]/=len(freq_table[i])
		return freq_table		

#Predicting category using frequency table. 
def predict(testSet,freq_table,cat_prob):
	hits=0;
	print "Initial = ",cat_prob	
	for tweet,category in testSet:
		words=nltk.word_tokenize(tweet)
		list_words=filter(lambda x: x not in stop_words,words)
		probability=[]
		for i in range(N):
			probability.append(1)
		for w in list_words:
			w=w.lower()
			for c in range(N):
				if(freq_table[c].__contains__(w)):
					probability[c]*=freq_table[c][w]
				else:
					probability[c]*=1/len(freq_table[c])	
		for i in range(N):
			probability[i]*=cat_prob[i] # Multiply with P[category]
		#print probability	
		if(category==probability.index(max(probability))):
			hits+=1
	return hits/len(testSet)						

def initProb(dataset):
	probs=[]
	for i in range(N):
		probs.append(0)
	for i in range(len(dataset)):
		probs[dataset[i][1]]+=1
	for i in range(N):
		probs[i]/=num_train	
	return probs
		
if(__name__=="__main__"):	
	dataset=loadCsv("dataset_v3.csv")
	N=3 #Number of classes
	num_train=1300;
	trainingSet,testSet=getSets(num_train)
	#print len(dataset),len(testSet),len(trainingSet)
	freq_table=getWords(trainingSet)
	#print len(freq_table[0]),len(freq_table[1])
	freq_table=updateFreqTable(freq_table)
	#print freq_table
	'''for i in freq_table:
		print "Class ",freq_table.index(i)
		for pair in i.keys():
			print pair," = ",i[pair]'''
	cat_prob=initProb(trainingSet)
	accuracy=predict(testSet,freq_table,cat_prob)
	print accuracy*100
