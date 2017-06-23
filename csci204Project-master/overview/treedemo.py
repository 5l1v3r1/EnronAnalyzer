import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz  #can be used to make a dot file
#import pydotplus


df = pd.read_csv('cardata.csv')
print("Read from CSV")
print(df)
#Need to setup maps to ordinal features
#We could do this iwht a list/dist comp, I will learn the syntax to you
eng_map = {'small': 0, 'med': 1, 'large': 2}
turbo_map = {'no': 0, 'yes': 1}
size_map = {'light': 0, 'avg': 1, 'heavy': 2}
eco_map = {'bad': 0, 'avg': 1, 'good': 2}
fast_map = {'no': 0, 'yes': 1}
df['eng'] = df['eng'].map(eng_map)
df['turbo'] = df['turbo'].map(turbo_map)
df['size'] = df['size'].map(size_map)
df['eco'] = df['eco'].map(eco_map)
df['fast'] = df['fast'].map(fast_map)
print("Converted Maps")
print(df)

#Now we can convert to numpy arrays
npv = df.as_matrix()
x = npv[:,0:4]
y = npv[:,[4]]
print("Got Numpy Arrays")


#Now attempt to make the tree
tree = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=0)
print(x)
print(y)
tree = tree.fit(x,y)
print("Built Tree")
dot_data = export_graphviz(tree, out_file='cartree.dot', feature_names=['eng', 'turbo', 'size', 'eco'])
#You can look at the dot file to see the tree that it made.  Very close to the one in the demo.
#dot_data = export_graphviz(tree, out_file=None)
#graph = pydotplus.graph_from_dot_data(dot_data)
#graph.write_pdf("cartree.pdf")

