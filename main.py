from Transfer import *
from FirstOrderLogic import *


if __name__ == '__main__':
    UpdateKB()
    UpdateQueries()
    inputQueries_ = getQueries("./Data/transferQueries.txt")
    inputSentences_ = getKB("./Data/transferSentences.txt")
    knowledgeBase = KB(inputSentences_)
    knowledgeBase.prepareKB()
    results_ = knowledgeBase.askQueries(inputQueries_)
    printOutput("output.txt", results_)