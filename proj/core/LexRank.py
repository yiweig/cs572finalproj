import numpy as np

from sumy.nlp.stemmers import Stemmer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import math

#Implementation of LexRank using sumy tokenizers and parsers

Language = "english"



def tokenizeToSentences(text):
    tokenizer = Tokenizer(Language)
    return tokenizer.to_sentences(text)
    
def tokenizeToWords(text):
    tokenizer = Tokenizer(Language)
    return tokenizer.to_words(text)

def tanimoto(a,b):
    c = [v for v in a if v in b]
    return float((len(c)) / len(a) +  len(b) - len(c))
    
def normalizeByLength(array, length):
    dist = 0
    for x in range(0,length):
        dist +=  array[x] * array[x]
    
    dist = math.sqrt(dist)
    
    for x in range(0,length):
        array[x] = array[x] / dist
    
    return array
	
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
    pass


def summarizeFromFile(file_path, sentence_threshold, similarityFunct, normalizeFunct, rankingMethod):
    l = ' '
    with open(file_path) as f:
        l = l.join(line.strip() for line in f)
    summarizeFromString(l,sentence_threshold, similarityFunct, normalizeFunct, rankingMethod)
    








summarizeFromFile('test.txt',10, tanimoto, normalizeByLength)

