#Graph code 1

from igraph import * importing igraph library 

g= Graph (3) #3 nodes

g.add_edge(0,1)
g.add_edge(1,2)
for i in range (0,g .vcount()):
	print (g. degree(i))

summary (g)

plot (g, "codel.pdf")