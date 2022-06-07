from sklearn.metrics.pairwise import cosine_similarity as cs
import numpy as np
from basic_recomm.models import Font_keyword_value
import math


def cos_sim(a, b):
    d1 = 0
    d2 = 0
    dp = 0

    for i in range(0, 19):
        dp += a[i] * b[i]
        d1 += a[i] * a[i]
        d2 += b[i] * b[i]

    cosSim = dp / (math.sqrt(d1 * d2))
    return cosSim
    # return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def cos_sim2(a, b):
    d1 = 0
    d2 = 0
    dp = 0

    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa******************************************")
    print(a)
    print("******************************************")

    for i in range(0, 19):
        if b[i] == 0:
            pass
        else:
            dp += a[i] * b[i]
            d1 += a[i] * a[i]
            d2 += b[i] * b[i]

    if d1==0 or d2==0:
        return -1

    cosSim = dp / (math.sqrt(d1 * d2))
    return cosSim

def selected_one(a, b):
    for i in range(0, 19):
        if b[i] == 1:
            return a[i]


def search_most_sim(selected_key):
    db = Font_keyword_value.objects.values()
    selected_key = list(map(float, selected_key))

    selected_num = 0

    for i in range(0,19):
        if selected_key[i]==1:
            selected_num+=1

    cos_val = []
    cos_val2 = []
    for i in range(0, len(db)):
        comp = db[i]['key_value']
        comp = list(map(float, comp))
        cosSim = cos_sim(comp, selected_key)

        if selected_num==1:
            cosSim2=selected_one(comp, selected_key)
        else:
            cosSim2 = cos_sim2(comp, selected_key)

        cos_val.append([i, cosSim])

        if cosSim2 == -1:
            continue

        cos_val2.append([i, cosSim2])

    print("******************************************")
    print(cos_val)
    print("******************************************")

    cos_val.sort(key=lambda cos_val: cos_val[1], reverse=True)
    cos_val2.sort(key=lambda cos_val2: cos_val2[1], reverse=True)

    return cos_val[:3], cos_val2[:3]
