from nltk.cluster.util import cosine_distance

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize, sent_tokenize

import numpy as np

import networkx as nx

import re

from rouge import Rouge

def sentence_similarity(sent1, sent2, stopwords=None):    

     if stopwords is None:        

       stopwords = []     

     sent1 = [w.lower() for w in sent1]    

     sent2 = [w.lower() for w in sent2]     

     all_words = list(set(sent1 + sent2))    

     vector1 = [0] * len(all_words)    

     vector2 = [0] * len(all_words)        

     for w in sent1:

         if w in stopwords:

             continue

         vector1[all_words.index(w)] += 1

     for w in sent2:

         if w in stopwords:

             continue        

         vector2[all_words.index(w)] += 1     

     return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):

    # Create an empty similarity matrix

    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):

        for idx2 in range(len(sentences)):

            if idx1 == idx2: #ignore if both are same sentences

                continue

            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def nltk_summarizer(raw_text):

    raw_text=  re.sub(r'[^a-zA-z0-9.,!?/:;\"\'\s]', '', raw_text)

    stop_words = stopwords.words('english')

    summarize_text = []

    # Step 1 - Read text and tokenize

    sentences = sent_tokenize(raw_text)

    # Step 2 - Generate Similary Martix across sentences

    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix

    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)

    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences

    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    

    print("Indexes of top ranked_sentence order are ", ranked_sentence)

    print(len(raw_text))

    top_n=3

    for i in range(top_n):

        summarize_text.append("".join(ranked_sentence[i][1]))

    # Step 5 -output the summarize text

    a=(" ".join(summarize_text))

    print(len(a))

    x=Rouge()

    y=x.get_scores(a,raw_text)

    print(y)

    return a



