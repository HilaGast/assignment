# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 10:47:54 2018

@author: hila
"""

def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    
    result=False
    for i in range(len(word)-5):
        if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            result = True
            return(result)
    return(result)

if __name__ == '__main__':
    print('Answers to question 1:')
#negative ex.:
    word='llkkbmm'
    result=trifeca(word)
    print(word,result)
    word='bbcCdd'
    result=trifeca(word)
    print(word,result)
    word=''
    result=trifeca(word)
    print(word,result)

#positive ex.:
    word='aabbcc'
    result=trifeca(word)
    print(word,result)
    word='abccddee0123'
    result=trifeca(word)
    print(word,result)
    word='aaaazz'
    result=trifeca(word)
    print(word,result)