from __future__ import division
import csv
import nltk
tweets = []
category = []
occurence_list = dict()
category_1= [] # initialized by zee 
category_0 = [] # initialized by zee
hits = 0

dict_list = []
dict_list.append(dict())
dict_list.append(dict())
with open('dataset_v2.csv') as f:
	read = csv.reader(f)
	i=0
	for row in read:
		if(row[1]=="1"):
			category_1.append(row[0])
		else:
			category_0.append(row[0])
		tweets.append(row[0])
		category.append(row[1])
		i+=1
	print "Lengths ", len(category_0), len(category_1)			

def build_occurrence_list():
	for i in range(len(tweets)):
		words = nltk.word_tokenize(tweets[i])
		for blub in words:
			#print "In one"
			if (not(occurence_list.__contains__(blub))):
				occurence_list[blub]=1
			else:
				occurence_list[blub]+=1
	print (sum(occurence_list.values()))			
	'''for i in occurence_list.keys():
		print i'''

#def init_counts(words, tweet_list):
	

#def build_dictionary():
for tweet in category_0:
	for w in nltk.word_tokenize(tweet): 
		if (dict_list[0].__contains__(w)):
			dict_list[0][w]+=1
		else:
			dict_list[0][w]=1
for tweet in category_1:
	for w in nltk.word_tokenize(tweet): 
		if (dict_list[1].__contains__(w)):
			dict_list[1][w]+=1
		else:
			dict_list[1][w]=1
print sum(dict_list[0].values())+ sum(dict_list[1].values())
print sum(dict_list[1].values())
for word in occurence_list.keys():
	if (dict_list[0].__contains__(word)):
		dict_list[0][word]/=sum(dict_list[0].values())
	if (dict_list[1].__contains__(word)):
		dict_list[1][word]/=sum(dict_list[1].values())
#return	


def lookup(dict_list , tweet ,expected_value):
	global hits
	#set_words_tweet = set(tweet.split())

	set_words_tweet= nltk.word_tokenize(tweet)
	#print set_words_tweet

	#Given a dictionary, lookup the probabilities

	#probablities of each word being in category 1
	cat0_prob=[]
	for i in set_words_tweet:
		if (dict_list[0].__contains__(i)):
			cat0_prob.append(dict_list[0][i])
	cat0_prob.append((len(category_0)/((len(category_0) + len(category_1)))))
	#probabilties of each word being in caegory 2
	cat1_prob=[]
	for j in set_words_tweet:
		if (dict_list[1].__contains__(j)):
			cat1_prob.append(dict_list[1][j])
	cat1_prob.append((len(category_1)/((len(category_0) + len(category_1)))))
	#print cat0_prob
	#print cat1_prob

	cat0_p = reduce(lambda x,y: x*y , cat0_prob)
	cat1_p = reduce(lambda x,y: x*y , cat1_prob)

	if cat0_p > cat1_p:
		#return '0' 
		if (expected_value != '0'):
			# debug stuff
			print cat0_p, cat1_p
			print cat0_prob
			print cat1_prob
		else:
			hits+=1
	else:
		if (expected_value != '1'):
			# debug stuff
			print cat0_p, cat1_p
			print cat0_prob
			print cat1_prob
		#return '1' 
		else:
			hits+=1

print len(tweets)
for i in range(0,len(tweets)):
	#if (lookup(dict_list, tweets[i],category[i])== category[i]):
	#	hits+=1
	lookup(dict_list, tweets[i], category[i])
print hits		
