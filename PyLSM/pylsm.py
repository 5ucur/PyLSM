import numpy
import spacy
import json
from functools import reduce

with open("postags.json") as file_:
    taglist = json.load(file_)

nlp = spacy.load("en_core_web_sm")

def abs_diff_score(n1, n2):
    return 1 - (numpy.abs(n1 - n2) / (n1 + n2 + numpy.nextafter(0,1)))

def get_pos_tags(text):
    return [word.tag_ for word in nlp(text)]

def get_counts(array):
    counter = {}
    for item in array:
        counter[item] = counter.get(item, 0) + 1
    return counter
    
def get_fword_proportion(text):
    tags = get_pos_tags(text)
    counts = get_counts(tags)
    total_count = 0
    fword_proportions = {}
    
    for key,val in counts.items():
        total_count += val
        fword_proportions[key] = counts[key] / total_count

    return fword_proportions

def compare_fword_proportions(f1, f2):
    likeness = [];
    for key in taglist:
        if f1.get(key, None) is None or f2.get(key, None) is None:
            if f1.get(key, None) is None and f2.get(key, None) is None:
                continue
            else:
                likeness.append(0)
        elif f1[key] == f2[key]:
            likeness.append(1)
        else:
            weight = numpy.abs(1 - ((f1[key] + f2[key])/2))
            diff = abs_diff_score(f1[key], f2[key])
            likeness.append(diff * weight)
    if likeness:
        summ = reduce(lambda a, b: a + b, likeness)
        avg = summ / len(likeness)
        return avg
    else:
        return 0

def compare_text_samples (t1, t2):
    result = list(map(get_fword_proportion, [t1, t2]))
    return compare_fword_proportions(result[0], result[1]);
