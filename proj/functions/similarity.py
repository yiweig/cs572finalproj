import  math



#Compute similarity scores between two arrays where each array contains words in a sentence
# a: [word1,word2,word3] b:[word2,word3,word1]



def tanimoto(a,b):
    c = [v for v in a if v in b]
    return float((len(c)) / len(a) +  len(b) - len(c))