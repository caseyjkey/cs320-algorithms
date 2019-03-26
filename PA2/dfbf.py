import sys

#global variable, keeping track in dfs whether a cycle was found
cyclic = False 

# Don't change helper functions
#   read, dump, white, dfsInit

def read(fnm):
  """  
  read file fnm containing a graph into a dictionary and return the dictionary
  each line has a nodeName followed by its adjacent nodeNames
  """
  f = open(fnm)
  gr = {} #graph represented by dictionary
  for line in f:
    l =line.strip().split(" ")
    # ignore empty lines
    if l==['']:continue
    # dictionary: key: nodeName  value: (color, adjacency List of names)
    gr[l[0]]= ('white',l[1:]) 
  return gr

def dump(gr):
  print("Input graph: nodeName (color, [adj list]) dictionary ")
  for e in gr:
    print(e, gr[e])

def white(gr) :
  """
   paint all gr nodes white
  """
  for e in gr :
    gr[e] = ('white',gr[e][1])

def dfsInit(gr,root):
   """
   dfs keeps track of cycles in global cyclic
   call dfs with appropriate initial parameters
   """ 
   global cyclic
   cyclic = False
   visited = dfs(gr,root,[])
   return (visited,cyclic)

# Work on bfs, dfs 

def bfs(gr,q):
  """
  q is an array representing a queue of (node,distance) pairs
  initially queue q contains 1 (node,distance) pair: (root,0)
  (see the call to bfs in main)
  breadth first search gr from the root, keep track of distance
  from root
  return the queue of all (node,distance) pairs visited
  """
  bfs = []
  bfs.append(q[0])
  while q:
      u = q.pop() # current
      for v in gr[u[0]][1]:
          if gr[v[0]][0] == 'white':
              gr[v[0]] = ('gray', gr[v[0]][1])
              child = (v, u[1] + 1)
              bfs.append(child)
              q.append(child)
      gr[u[0]] = ('black', gr[u[0]][1])
      #bfs.append(child)
      
      
  
  return bfs

      
def dfs(gr,r,visited):
   """  
   depth first search gr from root r for cycles,
   when a cycle is detected, set global cyclic to True
   return array of nodes visited, i.e. append node to visited
   when encountering it for the first time (i.e. when it is white)
   """
   global cyclic
   if r not in visited:
        visited.append(r)
   #print(str(gr))
        for v in gr[r][1]:
                #print(v, str(visited))
            dfs(gr, v, visited)
   else:
        cyclic = True
        return visited      
       
   return visited



if __name__ == "__main__":
  print(sys.argv[0])      # program name
  gr = read(sys.argv[1])  # graph file name
  root = sys.argv[2]      # root node
  print("BFS")
  dump(gr)
  print("Root node:", root)
  # don't need grey for bfs
  gr[root] = ('black',gr[root][1])
  q = bfs(gr,[(root,0)])
  print("BFS queue: (node name, distance) pairs")
  print(q)
  print("END BFS")
  print()
  white(gr);
  print("DFS")
  dump(gr)
  print("Root node", root)
  vis,cyc = dfsInit(gr,root)
  print("DFS from root visited:")
  print(vis)
  if cyc:
    print("graph with root",root,"is cyclic")
  else:
    print("graph with root",root,"is not cyclic")
  print("END DFS")


