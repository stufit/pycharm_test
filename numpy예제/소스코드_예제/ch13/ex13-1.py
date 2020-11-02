#!/usr/bin/env python
# coding: utf-8

# # 13.1 NetworkX

# In[1]:


#p193
get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx
G = nx.Graph()


# ## 노드/엣지의 삽입

# In[2]:


G.add_node(1)
print(G.nodes())


# In[3]:


G.add_node('P')
G.add_node('H')
print(G.nodes())


# In[4]:


G.add_nodes_from([2, 3])
print(G.nodes())


# In[5]:


#p195
nx.draw(G, with_labels=True, node_color='lightblue')


# In[6]:


G.add_edge(1, 2)
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='grey')


# In[7]:


print(G.edges())


# In[8]:


#p196
G.add_edges_from([(1,2), (1,3), (1,4), (1,5)])
print(G.edges())


# In[9]:


#p197
import networkx as nx
G = nx.path_graph(4)
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='grey')


# In[10]:


import networkx as nx
G = nx.Graph()
G.add_path([0,1,2,3])
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='grey')


# In[11]:


#p198
print(G.degree(0))
print(G.degree([0, 1]))
print(G.degree())


# ## 노드/엣지의 삭제

# In[12]:


G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (1,4), (1,5), (1,'P'), (1,'Hi'), (4,5)])
print(G.edges())
G.remove_edge(1, 3)
print(G.edges())


# In[13]:


G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (1,4), (1,5), (1,'P'), (1,'Hi'), (4,5)])
print(G.edges())
G.remove_edges_from([(1, 2), (1, 3)])
print(G.edges())


# In[14]:


G = nx.Graph()
G.add_nodes_from([1, 'P', 'Hi', 2, 3, 4, 5])
print(G.nodes())
G.remove_node(3)
print(G.nodes())


# In[15]:


#p199
G = nx.Graph()
G.add_nodes_from([1, 'P', 'Hi', 2, 3, 4, 5])
print(G.nodes())
G.remove_nodes_from([3, 4, 5])
print(G.nodes())


# ## 노드/엣지의 개수

# In[16]:


import networkx as nx
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1,2), (1,3), (1,4), (1,5), (4,5)])
print('No. nodes:', G.number_of_nodes())
print('No. edges:', G.number_of_edges())


# In[17]:


G.remove_edge(1, 3)
print('No. nodes:', G.number_of_nodes())
print('No. edges:', G.number_of_edges())


# In[18]:


#p200
import networkx as nx
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1,2), (1,3), (1,4), (1,5), (4,5)])
G.remove_node(3)
print('No. nodes:', G.number_of_nodes())
print('No. edges:', G.number_of_edges())


# ## 특정 확률 분포의 그래프 생성기

# In[19]:


#p202
import networkx as nx
import matplotlib.pyplot as plt
G = nx.erdos_renyi_graph(25, 0.2)
nx.draw(G)


# In[20]:


G = nx.watts_strogatz_graph(30, 3, 0.1)
nx.draw(G)


# In[21]:


G = nx.barabasi_albert_graph(25, 5)
nx.draw(G)


# In[22]:


#p203
G = nx.random_lobster(25, 0.9, 0.9)
nx.draw(G)


# In[23]:


from scipy.stats import bernoulli
for i in range(6):
    print(bernoulli.rvs(p=0.33))


# In[24]:


#p204
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
def erdosGraph(N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    listG = list(G.nodes())
    for i, node1 in enumerate(listG):
        for node2 in listG[i+1:]:
            if (bernoulli.rvs(p=p)):
                G.add_edge(node1, node2)
    return G
G1 = erdosGraph(80, 0.3)
plt.hist(list([d for n, d in G1.degree()]), histtype='step')


# In[25]:


#p205
def pltGraph(G):
    plt.hist(list([d for n, d in G.degree()]), histtype='step')
G1 = erdosGraph(80, 0.3)
pltGraph(G1)
G2 = erdosGraph(80, 0.3)
pltGraph(G2)
G3 = erdosGraph(80, 0.3)
pltGraph(G3)


# ## 엑셀 파일로 그래프 생성

# In[26]:


#p207
import numpy as np
import networkx as nx
K = np.loadtxt("test.csv", delimiter=",")
G = nx.to_networkx_graph(K)
nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')


# ## Networkx의 샘플 데이터 세트 1

# In[27]:


#p209
import networkx as nx
G = nx.karate_club_graph()
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='yellow')


# In[28]:


#p210
G.degree()


# In[29]:


print(G.degree())


# In[30]:


G.degree(16)


# In[31]:


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
G = nx.karate_club_graph()
print('노드의 개수: %d' % G.number_of_nodes())
print('엣지의 개수: %d' % G.number_of_edges())
print('평균 차수: %.1f' % np.mean([d for n, d in G.degree()]))


# ### node_size

# In[32]:


#p212
import networkx as nx
G = nx.karate_club_graph()
degree = [d for n, d in G.degree()]
nx.draw(G, with_labels=True, node_size=100, node_color='yellow', edge_color='red')


# In[33]:


#p213
import networkx as nx
G = nx.karate_club_graph()
degree = [d for n, d in G.degree()]
nx.draw(G, with_labels=True, node_size=[n*100 for n in degree], node_color='yellow', edge_color='red')


# ## Networkx의 샘플 데이터 세트 2
# ### 풋볼 팀의 대전 빈도

# In[34]:


#p214
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import zipfile
zf = zipfile.ZipFile('football.zip')
txt = zf.read('football.txt').decode()
gml = zf.read('football.gml').decode()
G = nx.parse_gml(gml)
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='grey')
plt.savefig('football.pdf')


# ### 소셜 네트워크

# In[35]:


#p215
import numpy as np
import networkx as nx
K = np.loadtxt("social.csv", delimiter=",")
G = nx.to_networkx_graph(K)
nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')


# #### 부분그래프

# In[36]:


#p216
ksub = nx.connected_component_subgraphs(G)
klist = list(ksub)
print(len(klist))


# In[37]:


#p217
nx.draw(klist[0], with_labels=True, node_color='yellow', edge_color='red')


# #### 가장 노드 수가 많은 부분그래프

# In[38]:


#p218
maxG = max(nx.connected_component_subgraphs(G), key=len)
nx.draw(maxG, with_labels=True, node_color='yellow', edge_color='red')


# In[ ]:




