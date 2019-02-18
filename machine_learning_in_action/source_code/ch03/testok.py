from imp import reload
import trees
import treePlotter
myDat, labels = trees.createDataSet()
myTree = treePlotter.retrieveTree(0)
trees.storeTree(myTree, 'classifierStorage.txt')
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLabels)
treePlotter.createPlot(lensesTree)
