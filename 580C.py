class Node:
  def __init__(self,value,parent=None):
    self.neighbors = set()
    self.value = value
    self.cat = 0
    self.parent = parent
    self.isVisited = False

  def add_neighbor(self,node):
    self.neighbors.add(node)

  def __repr__(self):
    return f"Node{self.value}"


class Graph:
  def __init__(self,n):
    self.nodes = { x:Node(x) for x in range(1,n+1) }
    self.isVisited = {i:False for i in range(1,n+1)}
    self.root = self.nodes[1]
    
  def get_node(self,value):
    if value in self.nodes:
      return self.nodes[value]
    else:
      return Node(value)

  def add_edge(self,src,dst):
    src = self.get_node(src)
    dst = self.get_node(dst)

    src.add_neighbor(dst)
    dst.add_neighbor(src)

  def hasCat(self,node):
    self.nodes[node].cat = 1

  def visit_node(self,node):
    self.isVisited[node.value] = True

  def get_neighbors(self,node):
    return [i for i in node.neighbors if not self.isVisited[i.value]]  

    
def make_graph():
  v, limit = (map(int,input().split()))
  cats = list(map(int,input().split()))
  graph = Graph(v)
  for i in range(v-1):
    src,dst = list(map(int,input().split()))
    graph.add_edge(src,dst)
  for i in range(v):
    if cats[i]:
      graph.hasCat(i+1)
  return graph, limit

def custom_dfs(graph, limit):
  stack = [(graph.root,0)]
  restaurants = 0
  while stack:
    node, catstreak = stack.pop()
    graph.visit_node(node)
    if ((catstreak + node.cat) > limit):
      continue

    if not node.cat :
      catstreak = 0
    else:
      catstreak +=1
    neighbors = graph.get_neighbors(node) 
    if len(neighbors) == 0:
      restaurants +=1
    else:
      stack.extend([(i,catstreak) for i in neighbors])   
  return restaurants
  

if __name__ == "__main__":
  graph, limit = make_graph()
  print(custom_dfs(graph, limit))
  