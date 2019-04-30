import nltk
from numpy import linalg as LA
from nltk.corpus import wordnet as wn
from pywsd import disambiguate
from pywsd.similarity import max_similarity as maxsim
import numpy as np


def getsense_of_words(sen):
    sen.lower()
    token = nltk.word_tokenize(sen)
    filtered_words = list()
    m= disambiguate(sen, algorithm=maxsim, similarity_option='wup', keepLemmas=True)
    for f in m:
        if f[2]:
            filtered_words.append(prune(str(f[2])))

    return filtered_words


func = lambda s: s[:1].lower() + s[1:] if s else ''
def psim(list1,list2):
    v=list()
    for l1 in list1:
        n=list()
        a=wn.synset(l1)
        for l2 in list2:
            b= wn.synset(l2)
            sim=a.path_similarity(b)
            if(sim):
                n.append(sim)
            else:
                n.append(0.0)

        #print(n)
        a1=max(n)
        v.append(a1)
    return v
def prune(syn):
    x=[]
    for i in range(8, len(syn) - 2):
        x.append(syn[i])
    return "".join(x)

def normalise(v,size):
    if(size>len(v)):
        for i in range(len(v),size):
            v.append(float(0))
    return v


def semantic_main(sen1,sen2):

    l1 = getsense_of_words(sen1)
    l2 = getsense_of_words(sen2)
    # print("list1:\n",l1)
    #print("list2:\n", l2)
    v1 = psim(l1, l2)
    v2 = psim(l2, l1)
    if len(v1) > len(v2):
        v2 = normalise(v2, len(v1))
    else:
        v1 = normalise(v1, len(v2))
    # print("vector1:\n",v1)
    # print("vector2:\n",v2)
    s = np.dot(v1, v2)
    # print(s)
    c1 = 0
    c2 = 0
    for v in v1:
        if v > 0.8025:
            c1 += 1
    for v in v2:
        if v > 0.8025:
            c2 += 1
    # print(c1,c2)
    dow = (c1 + c2) / 1.8
    fn = dow / s
    return fn



def wos(sen1,sen2):
    v1=list()
    v2=list()

    token1=nltk.word_tokenize(sen1)
    token2=nltk.word_tokenize(sen2)
    for t in token1:
        v1.append(token1.index(t)+1)
    for t2 in token2:
        if t2 in token1:
            v2.append(token1.index(t2)+1)
        else:
            v2.append(token2.index(t2)+1)
    if len(v1) > len(v2):
        v2 = normalise(v2, len(v1))
    if len(v1)<len(v2):
        v1 = normalise(v1, len(v2))
    #print(v1,v2)
    wos=np.divide(LA.norm(np.subtract(v1, v2)), LA.norm(np.multiply(v1, v2)))
    return wos

