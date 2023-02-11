# Semantic Similarity: starter code

import math

def norm(vec):
    '''
    Return the norm of a vector stored as a dictionary, as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    absolute_vec1 = 0
    absolute_vec2 = 0
    n = 0

    for i in vec1:
        absolute_vec1 += vec1[i]**2

    for i in vec2:
        absolute_vec2 += vec2[i]**2

    d = (absolute_vec1*absolute_vec2)**(0.5)

    if len(vec1) >= len(vec2):
        for m in vec2:
            if m in vec1:
                n += vec2[m] * vec1[m]
    else:
        for m in vec1:
            if m in vec2:
                n += vec2[m] * vec1[m]

    return n/d


def build_semantic_descriptors(sentences):
    d = {}

    sentencesets = []
    for sentence in sentences:
        sentencesets.append(set(sentence))

    for s in sentencesets:
        for w in s:
            if w not in d:
                d[w] = {}

    for s in sentencesets:
        for w in s:
            for i in s:
                if i != w:
                    if i in d[w]:
                        d[w][i] += 1
                    else:
                        d[w][i] = 1

    return d


# split function can only be used in string variables
def build_semantic_descriptors_from_files(filenames):
    files = ""

    for i in range(len(filenames)):
        f = open(filenames[i],"r",encoding="latin1")
        file = f.read().lower()
        files += file + " "

    sentences = files.replace("!",".").replace("?",".").replace(","," ").replace("-"," ").replace("--"," ").replace(":"," ").replace(";"," ").replace("\n"," ").split(".")

    s = []
    for j in sentences:
        s.append(j.split())

    return build_semantic_descriptors(s)

def most_similar_word(word, choices,semantic_descriptors, similarity_fn):

    max = -1
    indexi = 0
    for i in range(len(choices)):
        if ((word in semantic_descriptors) and (choices[i] in semantic_descriptors)):
            s = similarity_fn(semantic_descriptors[word],semantic_descriptors[choices[i]])
        else:
            s = -1
        if s > max:
            max = s
            indexi = i
    return choices[indexi]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    fi = open(filename,"r",encoding="latin1")
    filei = fi.read()
    line = filei.split("\n")
    count = 0
    for i in line:
        l = []
        l.extend(i.split(" "))
        if len(l)<2:
            continue
        w = most_similar_word(l[0],l[2:],semantic_descriptors,similarity_fn)
        if w == l[1]:
            count += 1
    return count/len(line)*100


sem_descriptors = build_semantic_descriptors_from_files(["wp.txt","sw.txt"])
res = run_similarity_test("hello.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")
