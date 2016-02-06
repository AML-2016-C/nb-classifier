from __future__ import division
import csv

tweets = []
category = []

with open('dataset_v2.csv') as f:
	read = csv.reader(f)
	i=0
	for row in read:
		tweets.append(row[0])
		category.append(row[1])
		i+=1

tweets_0=[]
tweets_1=[]
for count in range(len(tweets)):
	#print type(category[count])
	if category[count]=='1':
		tweets_0.append(tweets[count])
	else:
		category[count]='2'
		tweets_1.append(tweets[count])

#print category[35]

words_cat0 = []
words_cat1 = []

for count in tweets_0:
	temp = count.split()
	for i in temp:
		words_cat0.append(i)
for count in tweets_1:
	temp = count.split()
	for i in temp:
		words_cat1.append(i)

#print tweets_0
no_words_cat0 = len(words_cat0)

no_words_cat1 = len(words_cat1)

def lookup(tweet):

	global words_cat0, words_cat1, no_words_cat1, no_words_cat0
	#print no_words_cat0
	#print no_words_cat1
	set_words_tweet = set(tweet.split())
	#print set_words_tweet

	#Given a dictionary, lookup the probabilities

	#probablities of each word being in category 0
	cat0_prob=[]
	for i in set_words_tweet:
		p = words_cat0.count(i)/no_words_cat0
		if p!=0:
			cat0_prob.append(p)
		else:
			cat0_prob.append(1.0/no_words_cat0)
	cat0_prob.append(no_words_cat0/(no_words_cat0+no_words_cat1))

	#probabilties of each word being in caegory 1
	cat1_prob=[]
	for j in set_words_tweet:
		p = words_cat1.count(j)/no_words_cat1
		if p!=0:
			cat1_prob.append(p)
		else:
			cat1_prob.append(1.0/no_words_cat1)
	cat1_prob.append(no_words_cat1/(no_words_cat0+no_words_cat1))


	#print cat0_prob
	#print cat1_prob
	try:
		cat0_p = reduce(lambda x,y: x*y , cat0_prob)
		cat1_p = reduce(lambda x,y: x*y , cat1_prob)
		#print cat0_p
		#print cat1_p

		if cat0_p > cat1_p:
			#print "1"
			return "1"
		else:
			#print "2"
			return "2"
	except:
		pass

hits=0

#print category
for i in range(len(tweets)):
	guess = lookup(tweets[i])
	if guess == category[i]:
		hits+=1

print len(tweets)
print hits
#lookup(tweets[35])
