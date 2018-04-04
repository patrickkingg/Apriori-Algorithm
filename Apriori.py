#written by Patrick Wang
from sys import argv
import time
from AprioriCalculation import apriori

def main():

    inputData = argv[1]
    lines = []
    with open(inputData, 'r') as f:
        for line in f.readlines():
            line = frozenset([int(i) for i in line.split()])
            lines.append(line)
    inputData = lines
    minSupp = int(argv[2])
    outputFile = argv[3]
    startTime = time.time()
    results = apriori(inputData, minSupp)
    endTime =time.time()
    print("execution time is %f seconds" % (endTime - startTime))
    print (len(results))
    with open(outputFile, 'w') as out:
        for item, count in results.items():
            item = sorted(item)
            nextString = ' '.join(str(i) for i in item)
            string = '%s (%d)\n' % (nextString, count)
            out.write(string)

    result = []
    with open(outputFile,'r') as f:
        for line in f.readlines():

            result.append(line)
    result = sorted(result,key=lambda x:(float(x.split()[0]),float(x.replace("(","").replace(")","").split()[1]) ))
    #result = sorted(result, key=lambda x: float(x.replace("(","").replace(")","").split()[1]))
    with open(outputFile, 'w') as out:
        for each in result:
            out.write(each)


if __name__ == "__main__": main()