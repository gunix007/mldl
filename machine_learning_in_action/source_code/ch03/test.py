>>> from imp import reload
>>> import trees
>>> import treePlotter
>>> myDat, labels = trees.createDataSet()
>>> myTree = treePlotter.retrieveTree(0)
>>> trees.storeTree(myTree, 'classifierStorage.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/gunix/workspace/src/github/mldl/machine_learning_in_action/source_code/ch03/trees.py", line 116, in storeTree
    pickle.dump(inputTree, fw)
TypeError: write() argument must be str, not bytes
>>> reload(trees)
<module 'trees' from '/home/gunix/workspace/src/github/mldl/machine_learning_in_action/source_code/ch03/trees.py'>
>>> 
>>> 
>>> trees.storeTree(myTree, 'classifierStorage.txt')
>>> trees.storeTree(myTree, 'classifierStorage.txt')
>>> trees.grabTree('classifierStorage.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/gunix/workspace/src/github/mldl/machine_learning_in_action/source_code/ch03/trees.py", line 120, in grabTree
    return pickle.load(fr)
  File "/home/gunix/anaconda3/lib/python3.6/codecs.py", line 321, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
>>> 
>>> reload(trees)
<module 'trees' from '/home/gunix/workspace/src/github/mldl/machine_learning_in_action/source_code/ch03/trees.py'>
>>> trees.grabTree('classifierStorage.txt')
{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
>>> 
>>> 
>>> 
>>> trees.grabTree('classifierStorage.txt')
{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
>>> 
>>> 
>>> 
>>> trees.storeTree(myTree, 'classifierStorage.txt')
>>> 
>>> 
>>> myTree
{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
>>> 
>>> trees.grabTree('classifierStorage.txt')         
{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
>>> 
>>> fr = open('lenses.txt')
>>> lenses = [inst.strip().split('\t') for inst in fr.readLines()]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: '_io.TextIOWrapper' object has no attribute 'readLines'
>>> lenses = [inst.strip().split('\t') for inst in fr.readlines()]
>>> lenses
[['young', 'myope', 'no', 'reduced', 'no lenses'], ['young', 'myope', 'no', 'normal', 'soft'], ['young', 'myope', 'yes', 'reduced', 'no lenses'], ['young', 'myope', 'yes', 'normal', 'hard'], ['young', 'hyper', 'no', 'reduced', 'no lenses'], ['young', 'hyper', 'no', 'normal', 'soft'], ['young', 'hyper', 'yes', 'reduced', 'no lenses'], ['young', 'hyper', 'yes', 'normal', 'hard'], ['pre', 'myope', 'no', 'reduced', 'no lenses'], ['pre', 'myope', 'no', 'normal', 'soft'], ['pre', 'myope', 'yes', 'reduced', 'no lenses'], ['pre', 'myope', 'yes', 'normal', 'hard'], ['pre', 'hyper', 'no', 'reduced', 'no lenses'], ['pre', 'hyper', 'no', 'normal', 'soft'], ['pre', 'hyper', 'yes', 'reduced', 'no lenses'], ['pre', 'hyper', 'yes', 'normal', 'no lenses'], ['presbyopic', 'myope', 'no', 'reduced', 'no lenses'], ['presbyopic', 'myope', 'no', 'normal', 'no lenses'], ['presbyopic', 'myope', 'yes', 'reduced', 'no lenses'], ['presbyopic', 'myope', 'yes', 'normal', 'hard'], ['presbyopic', 'hyper', 'no', 'reduced', 'no lenses'], ['presbyopic', 'hyper', 'no', 'normal', 'soft'], ['presbyopic', 'hyper', 'yes', 'reduced', 'no lenses'], ['presbyopic', 'hyper', 'yes', 'normal', 'no lenses']]
>>> 
>>> lensesLabels = ['age', 'prescript', 'astigmatic' 'tearRate']
>>> lensesLabels
['age', 'prescript', 'astigmatictearRate']
>>> 
>>> 
>>> lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
>>> 
>>> 
>>> lensesLabels
['age', 'prescript', 'astigmatic', 'tearRate']
>>> 
>>> lensesTree = trees.createTree(lenses, lensesLabels)
>>> lensesTree
{'tearRate': {'normal': {'astigmatic': {'yes': {'prescript': {'myope': 'hard', 'hyper': {'age': {'pre': 'no lenses', 'presbyopic': 'no lenses', 'young': 'hard'}}}}, 'no': {'age': {'pre': 'soft', 'presbyopic': {'prescript': {'myope': 'no lenses', 'hyper': 'soft'}}, 'young': 'soft'}}}}, 'reduced': 'no lenses'}}
>>> 
>>> 
>>> 
>>> treePlotter.createPlot(lensesTree)
QXcbConnection: Could not connect to display 
Aborted
