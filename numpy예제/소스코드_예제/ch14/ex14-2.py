#!/usr/bin/env python
# coding: utf-8

# # 14.2 트리 분류자의 시각화

# In[5]:


#p247
import graphviz
from sklearn import tree
features = [[270, 0], [250, 0], [220, 1], [240, 1]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render()
dot_data = tree.export_graphviz(clf, out_file=None, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph


# In[7]:


#p249
from sklearn import tree
features = [[270, 0], [250, 0], [260, 0], [220, 1], [240, 1], [230, 1]]
labels = [0, 0, 0, 1, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render()
dot_data = tree.export_graphviz(clf, out_file=None, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph


# In[ ]:




