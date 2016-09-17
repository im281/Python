# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 16:15:28 2015

@author: iman.mohtashemi
"""

#
# from testing import foo,add
# print(foo(5,2))
# print(add(10,2))
#
from numpy import *
from pylab import *
links = {}
fnames = ['angelinajolie.html', 'bradpitt.html',
'jenniferaniston.html', 'jonvoight.html',
'martinscorcese.html', 'robertdeniro.html']

for file in fnames:
     links[file] = []
     f = open(file)
     for line in f.readlines():
        while True:
            p = line.partition('<a href="http://')[2]
            if p=='':
                 break
            url, _, line = p.partition('\">')
            links[file].append(url)
     f.close()

import networkx as nx
DG = nx.DiGraph()
DG.add_nodes_from(fnames)
edges = []
for key, values in links.items():
    eweight = {}
    for v in values:
        if v in eweight:
            eweight[v] += 1
        else:
            eweight[v] = 1
    for succ, weight in eweight.items():
        edges.append([key, succ, {'weight':weight}])

DG.add_edges_from(edges)


#import cPickle as pickle
#pickle.dump(DG, open('DG.pkl','w'))

import matplotlib.pyplot as plt
plt.figure(figsize=(9,9))
pos=nx.spring_layout(DG,iterations=10)
nx.draw(DG,pos,node_size=0,alpha=0.4,edge_color='r',
font_size=16)
plt.savefig("link_graph.png")
plt.show()

from numpy import zeros
NX = len(fnames)
T = matrix(zeros((NX, NX)))


f2i = dict((fn, i) for i, fn in enumerate(fnames))



print(f2i)

for predecessor, successors in DG.adj.items():
    for s, edata in successors.items():
        T[f2i[predecessor], f2i[s]] = edata['weight']
print(T)

from numpy.random import random
from numpy import sum, ones,dot
epsilon = .01
E = ones(T.shape)/NX
L = T + epsilon * E
G = matrix(zeros(L.shape))
for i in range(NX):
     G[i,:] = L[i,:] / sum(L[i,:])

PI = random(NX)
PI /= sum(PI)
R = PI
for _ in range(100):
    R = dot(R, G)


from numpy import linalg
#array = linalg.eigvals(G**1000)
#print(array)

revind = {}
for fname in fnames:
    for line in open(fname).readlines():
        for token in line.split():
            if token in revind:
                if fname in revind[token]:
                    revind[token][fname] += 1
                else:
                    revind[token][fname] = 1
            else:
                revind[token] = {fname: 1}

result = revind['films'].keys()


def getPageRank(fname):
    return R[0,f2i[fname]]

print(sorted(result,key=getPageRank,reverse = True))



# import networkx as nx
# G=nx.Graph()
# G.add_node("spam")
# G.add_edge(1,2)
# print(G.nodes())
# print(G.edges())

a = 5
# b = 3
# c = a + b
# print(c)
# print(b)
