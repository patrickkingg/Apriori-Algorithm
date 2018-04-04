#written by Patrick Wang
from collections import defaultdict

def getFreqSingle(allTransactions, support, results):
    counter = defaultdict(int)
    result = defaultdict(int)
    for transaction in allTransactions:
        data=sorted(transaction)
        _2itemSet=[]
        i=1
        for each in transaction:
            counter[each] += 1
        for x in data:
            for y in data[i:]:
                _2itemSet.append(frozenset([x,y]))
            i+=1


        for item in _2itemSet:
            result[item] += 1

    for k in counter:
        if counter[k] >= support:
            results[frozenset([k])] = counter[k]
    return result



def getCand(currCand, k):
    result = set()
    for x in currCand:
        for y in currCand:
            z = x | y
            if  x != y and len(z)==k:
                for each in z:
                    subset=z-frozenset([each])
                    if subset in currCand:
                        result.add(z)
    return result

def apriori(allTransactions, minSupp):
    results = {}
    candidates = getFreqSingle(allTransactions, minSupp, results)

    supportCand = {}
    if candidates:
        for item in candidates:
            if candidates[item] >= minSupp:
                supportCand.update({item: candidates[item]})
    results.update(supportCand)
    candidates = supportCand
    k = 3
    while candidates:

        candidates = getCand(candidates.keys(), k)
        if candidates:
            counted = defaultdict(int)
            for transaction in allTransactions:
                bucket = [candidate for candidate in candidates if candidate <= transaction]
                for each in bucket:
                    counted[each] += 1
            suppCand = {}
            for item in counted:
                if counted[item] >= minSupp:
                    suppCand.update({item: counted[item]})

            results.update(suppCand)
            candidates = suppCand
            k += 1
        else:
            break
    return results