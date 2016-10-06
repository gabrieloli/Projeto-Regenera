import nltk

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_words_in_samples(samples):
    all_words = []
    for (words, sentiment) in samples:
      all_words.extend(words)
    return all_words

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def train(labeled_featuresets, estimator="ELEProbDist"):

    # Create the P(label) distribution
    label_probdist = estimator(label_freqdist)

    # Create the P(fval|label, fname) distribution
    feature_probdist = {}

    return NaiveBayesClassifier(label_probdist, feature_probdist)

pos_samples = [('Hello', 'positive'),
	      ('Hi', 'positive'),
	      ('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]

neg_samples = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
	      ('I hate you','negative')]

love_samples = [('I love you', 'love'),
		('I like you', 'love'),
		('I am in love', 'love'),
		('I look at you and see the rest of my life in front of my eyes', 'love'),
		("I'm much more me when I'm with you", 'love'),
		("I swear I couldn't love you more than I do right now, and yet I know I will tomorrow.", 'love')]

anger_samples = [('I hate this place', 'anger'),
		 ('You look terrible', 'anger'),
		 ('I am angry', 'anger'),
		 ('I blame you', 'anger'),
		 ('I shame you', 'anger'),
		 ('I hate you', 'anger')]

def new_classifier(name, input_samples):
	samples = []
	for (words, sentiment) in input_samples :
		words_filtered = [e.lower() for e in words.split() if len(e) >=3]
		samples.append((words_filtered, sentiment))
	word_features = get_word_features(get_words_in_samples(samples))
	training_set = nltk.classify.apply_features(extract_features, samples)
	name = nltk.NaiveBayesClassifier.train(training_set)
	return eval(name+' = nltk.NaiveBayesClassifier.train(training_set)')	

samples = []
for (words, sentiment) in pos_samples + neg_samples + anger_samples + love_samples :
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    samples.append((words_filtered, sentiment))
print(samples)
word_features = get_word_features(get_words_in_samples(samples))

training_set = nltk.classify.apply_features(extract_features, samples)
#classifier = nltk.NaiveBayesClassifier.train(training_set)

def analyse(string,classifier):
	return(eval(classifier+'.classify(extract_features(string.split()))'))

new_classifier('anger', anger_samples)


#print(classifier.classify(extract_features(analyse.split())))
