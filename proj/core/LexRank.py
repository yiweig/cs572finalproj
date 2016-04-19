import numpy as np

from sumy.nlp.stemmers import Stemmer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import math
import sys
sys.path.insert(0,'../functions/')

import normalize,rank,similarity

#Implementation of LexRank using sumy tokenizers and parsers

Language = "english"



def tokenizeToSentences(text):
    tokenizer = Tokenizer(Language)
    return tokenizer.to_sentences(text)
    
def tokenizeToWords(text):
    tokenizer = Tokenizer(Language)
    return tokenizer.to_words(text)

    
	
def buildMatrix(sentences, similarityFunct, normalizeFunct):
    matrix = [[0 for x in range(len(sentences))] for y in range(len(sentences))] 
    length = len(sentences)
    for x in range (0, length):
        for y in range(0,length):
            score = similarityFunct(sentences[x],sentences[y])
            # val = 0 if not exist?
            matrix[x][y] = score
        matrix[x] = normalizeFunct(matrix[x], length)
      
    return matrix
    
    
    

def summarizeFromString(text, sentence_threshold, similarityFunct, normalizeFunct, rankingMethod):
    sentences = tokenizeToSentences(text)
    tokenized_sentences = [tokenizeToWords(x) for x in sentences]
    
    matrix = buildMatrix(sentences, similarityFunct, normalizeFunct)
    ranked_sentences = rankingMethod(matrix, sentences)
    
    top_sentences = []
    
    
    for x in range(0,min(sentence_threshold,len(ranked_sentences))):
        top_sentences.append(ranked_sentences[x])

    top_sentences = sorted(top_sentences, lambda x, y: int(x.index - y.index))
    
    summary = ' '
    for x in range(0,len(top_sentences)):
        summary += top_sentences[x].sentence + ' '
        
    return summary


def summarizeFromFile(file_path, sentence_threshold, similarityFunct, normalizeFunct, rankingMethod):
    l = ' '
    with open(file_path) as f:
        l = l.join(line.strip() for line in f)
    return  summarizeFromString(l,sentence_threshold, similarityFunct, normalizeFunct, rankingMethod)
    





l = summarizeFromFile('test.txt',5, similarity.tanimoto, normalize.normalizeByLength, rank.page_rank)
print l
