import numpy as np

from sumy.nlp.stemmers import Stemmer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


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
	
def buildMatrix(sentences):
    matrix = [[0 for x in range(len(sentences))] for y in range(len(sentences))] 
    
    for x in range (0,len(sentences)):
        for y in range(0,len(sentences)):
            score = tanimoto(sentences[x],sentences[y])
            #print score
            #Suppose to check if undefined score then set to 0 
            matrix[x][y] = score
    return matrix

def summarizeFromString(text, sentence_threshold):
    sentences = tokenizeToSentences(text)
    tokenized_sentences = [tokenizeToWords(x) for x in sentences]
    
    matrix = buildMatrix(sentences)
    print matrix
    pass


def summarizeFromFile(file_path, sentence_threshold):
    l = ' '
    with open(file_path) as f:
        l = l.join(line.strip() for line in f)
    summarizeFromString(l,sentence_threshold)
    








summarizeFromFile('test.txt',10)

