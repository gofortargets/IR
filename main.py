from __future__ import division, unicode_literals
import string
import os
from scipy.spatial import distance
from scipy import spatial
import numpy
from textblob import TextBlob as tb
def remove_punct(s):
    s = s.translate(string.maketrans("",""), string.punctuation)
    return s

def normalize(s):
    s = s.lower()
    s = remove_punct(s)
    return s

