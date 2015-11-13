##  Wzorowane na przykładzie Rona Zacharskiego

class Classifier:

    def __init__(self, filename):

        self.medianAndDeviation = []       
        # reading the data in from the file
        f = open(filename)
        lines = f.readlines()
        f.close()
        self.format = lines[0].strip().split('\t')
        self.data = []
        for line in lines[1:]:
            fields = line.strip().split('\t')
            ignore = []
            vector = []
            for i in range(len(fields)):
                if self.format[i] == 'num':
                    vector.append(int(fields[i]))
                elif self.format[i] == 'comment':
                    ignore.append(fields[i])
                elif self.format[i] == 'class':
                    classification = fields[i]
            self.data.append((classification, vector, ignore))
        self.rawData = list(self.data)
        # get length of instance vector
        self.vlen = len(self.data[0][1])
        # now normalize the data
        for i in range(self.vlen):
            self.normalizeColumn(i)
        

        

    def getMedian(self, alist):
        """TODO: zwraca medianę listy"""

        return 0
        

    def getAbsoluteStandardDeviation(self, alist, median):
        """TODO: zwraca absolutne odchylenie standardowe listy od mediany"""
        return 0

    def normalizeColumn(self, columnNumber):
        """TODO: 
        1. mając dany nr kolumny w self.data, dokonuje normalizacji wg Modified Standard Score
        2. zapisz medianę i odchylenie standardowe dla kolumny w self.medianAndDeviation"""

        pass
        
    def normalizeVector(self, v):
        """Znormalizuj podany wektor mając daną medianę i odchylenie standardowe dla każdej kolumny"""
        vector = list(v)
        # TODO: wpisz kod
        return vector

    def manhattan(self, vector1, vector2):
        """Zwraca odległość Manhattan między dwoma wektorami cech."""
        return sum(map(lambda v1, v2: abs(v1 - v2), vector1, vector2))


    def nearestNeighbor(self, itemVector):
        """return nearest neighbor to itemVector"""
        
        return ((0, ("TODO: Zwróc najbliższego sąsiada", [0], [])))
    
    def classify(self, itemVector):
        """Return class we think item Vector is in"""
        return(self.nearestNeighbor(self.normalizeVector(itemVector))[1][0])
        
        
def testMedianAndASD():
    list1 = [54, 72, 78, 49, 65, 63, 75, 67, 54]
    list2 = [54, 72, 78, 49, 65, 63, 75, 67, 54, 68]
    list3 = [69]
    list4 = [69, 72]
    classifier = Classifier('athletesTrainingSet.txt')
    m1 = classifier.getMedian(list1)
    m2 = classifier.getMedian(list2)
    m3 = classifier.getMedian(list3)
    m4 = classifier.getMedian(list4)
    asd1 = classifier.getAbsoluteStandardDeviation(list1, m1)
    asd2 = classifier.getAbsoluteStandardDeviation(list2, m2)
    asd3 = classifier.getAbsoluteStandardDeviation(list3, m3)
    asd4 = classifier.getAbsoluteStandardDeviation(list4, m4)
    assert(round(m1, 3) == 65)
    assert(round(m2, 3) == 66)
    assert(round(m3, 3) == 69)
    assert(round(m4, 3) == 70.5)
    assert(round(asd1, 3) == 8)
    assert(round(asd2, 3) == 7.5)
    assert(round(asd3, 3) == 0)
    assert(round(asd4, 3) == 1.5)
    
    print("getMedian and getAbsoluteStandardDeviation work correctly")
    
def testNormalization():
    classifier = Classifier('athletesTrainingSet.txt')
    #
    #  test median and absolute standard deviation methods
    list1 = [54, 72, 78, 49, 65, 63, 75, 67, 54, 76, 68,
             61, 58, 70, 70, 70, 63, 65, 66, 61]
    list2 = [66, 162, 204, 90, 99, 106, 175, 123, 68,
             200, 163, 95, 77, 108, 155, 155, 108, 106, 97, 76]
    m1 = classifier.getMedian(list1)
    assert(round(m1, 3) == 65.5)
    m2 = classifier.getMedian(list2)
    assert(round(m2, 3) == 107)
    assert(round(classifier.getAbsoluteStandardDeviation(list1, m1),3) == 5.95)
    assert(round(classifier.getAbsoluteStandardDeviation(list2, m2),3) == 33.65)
    print("getMedian and getAbsoluteStandardDeviation are OK")

    # test normalizeColumn
    list1 = [[-1.9328, -1.2184], [1.0924, 1.6345], [2.1008, 2.8826],
             [-2.7731, -0.5052], [-0.084, -0.2377], [-0.4202, -0.0297],
             [1.5966, 2.0208], [0.2521, 0.4755], [-1.9328, -1.159],
             [1.7647, 2.7637], [0.4202, 1.6642], [-0.7563, -0.3566],
             [-1.2605, -0.8915], [0.7563, 0.0297], [0.7563, 1.4264],
             [0.7563, 1.4264], [-0.4202, 0.0297], [-0.084, -0.0297],
             [0.084, -0.2972], [-0.7563, -0.9212]]
    

    for i in range(len(list1)):
        assert(round(classifier.data[i][1][0],4) == list1[i][0])
        assert(round(classifier.data[i][1][1],4) == list1[i][1])
    print("normalizeColumn is OK")
    
def testClassifier():
    classifier = Classifier('athletesTrainingSet.txt')
    br = ('Basketball', [72, 162], ['Brittainey Raven'])
    nl = ('Gymnastics', [61, 76], ['Viktoria Komova'])
    cl = ("Basketball", [74, 190], ['Crystal Langhorne'])
    # first check normalize function
    brNorm = classifier.normalizeVector(br[1])
    nlNorm = classifier.normalizeVector(nl[1])
    clNorm = classifier.normalizeVector(cl[1])
    assert(brNorm == classifier.data[1][1])
    assert(nlNorm == classifier.data[-1][1])
    print('normalizeVector fn OK')
    # check distance
    assert (round(classifier.manhattan(clNorm, classifier.data[1][1]), 5) == 1.16823)
    assert(classifier.manhattan(brNorm, classifier.data[1][1]) == 0)
    assert(classifier.manhattan(nlNorm, classifier.data[-1][1]) == 0)
    print('Manhattan distance fn OK')
    # Brittainey Raven's nearest neighbor should be herself
    result = classifier.nearestNeighbor(brNorm)
    assert(result[1][2]== br[2])
    # Nastia Liukin's nearest neighbor should be herself
    result = classifier.nearestNeighbor(nlNorm)
    assert(result[1][2]== nl[2])
    # Crystal Langhorne's nearest neighbor is Jennifer Lacy"
    assert(classifier.nearestNeighbor(clNorm)[1][2][0] == "Jennifer Lacy")
    print("Nearest Neighbor fn OK")
    # Check if classify correctly identifies sports
    assert(classifier.classify(br[1]) == 'Basketball')
    assert(classifier.classify(cl[1]) == 'Basketball')
    assert(classifier.classify(nl[1]) == 'Gymnastics')
    print('Classify fn OK')
    
    
def test(training_filename, test_filename):
    """Test the classifier on a test set of data"""
    classifier = Classifier(training_filename)
    f = open(test_filename)
    lines = f.readlines()
    f.close()
    numCorrect = 0.0
    for line in lines:
        data = line.strip().split('\t')
        vector = []
        classInColumn = -1
        for i in range(len(classifier.format)):
              if classifier.format[i] == 'num':
                  vector.append(float(data[i]))
              elif classifier.format[i] == 'class':
                  classInColumn = i
        theClass= classifier.classify(vector)
        prefix = '-'
        if theClass == data[classInColumn]:
            # it is correct
            numCorrect += 1
            prefix = '+'
        print("%s  %12s  %s" % (prefix, theClass, line))
    print("%4.2f%% correct" % (numCorrect * 100/ len(lines)))
        

##
##  Przykłady użycia
#  test('athletesTrainingSet.txt', 'athletesTestSet.txt')
#  test("irisTrainingSet.data", "irisTestSet.data")
#  test("mpgTrainingSet.txt", "mpgTestSet.txt")

testMedianAndASD()
# testNormalization()
# testClassifier()

