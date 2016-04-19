import math
import normalize


class weighted_sentence:
    def __init__(self, weight, sentence, index):
        self.weight = weight
        self.sentence = sentence
        self.index = index
        

#Ranking input:Matrix of similarity scores between each pair of sentences, original sentences in a list
def page_rank(matrix, original_sentences):
    length = len(original_sentences)
    eigen = [1 for x in range(length)]
    for x in range (0,10):
        w = [0 for x in range(length)]
        for i in range(0,length):
            for j in range(0,length):
                w[i] = w[i] + (matrix[i][j] * eigen[j])
        
        eigen = normalize.normalizeByLength(w, length)
        
    eigenCounts = []
    
    for x in range(0,length):
        ws = weighted_sentence(eigen[x], original_sentences[x], x)
        eigenCounts.append(ws)
    
    #>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
    eigenCounts = sorted(eigenCounts, lambda x, y: int(y.weight - x.weight))
    
    return eigenCounts