class Node:
  def __init__(self,value,parent=None):
    self.childrens = []
    self.value = value
    self.cat = 0
    self.parent = parent
    self.isVisited = False

  def add_child(self,child):
    # child = Node(child,parent=self.value)
    self.childrens.append(child)

  def set_parent(self, parent):
    self.parent = parent
  
  def __repr__(self):
    return f"{self.value} has {self.cat} cats, {len(self.childrens)} children"

class Graph:
  def __init__(self):
    self.nodes = {}
    self.root = Node(1)
    self.nodes[1] = self.root

  def add_edge(self,src,dst):
    # src,dst = sorted((src,dst))
    if not src in self.nodes:
      self.nodes[src] = Node(src)
    src = self.nodes[src]

    if not dst in self.nodes:
      self.nodes[dst] = Node(dst)
    dst = self.nodes[dst]

    src.add_child(dst)
    dst.set_parent(src)

    # dst.add_child(src)
    # src.set_parent(dst)



  def hasCat(self,node):
    self.nodes[node].cat = 1
    
def make_graph():
  v, limit = (map(int,input().split()))
  cats = list(map(int,input().split()))
  graph = Graph()
  for i in range(v-1):
    src,dst = list(map(int,input().split()))
    graph.add_edge(src,dst)
  for i in range(v):
    if cats[i]:
      graph.hasCat(i+1)
  return graph, limit

def custom_dfs(graph, limit):
  # catstreak = graph.root.cat
  def inner(node, catstreak, limit):
    print("Parent",node.value, catstreak)
    if (catstreak + node.cat) > limit:
      return 0
    if len(node.childrens) == 0:
      print("Path!",node, catstreak)
      return 1

    catstreak = catstreak+1 if node.cat else 0
    rests = 0
    node.isVisited = True
    for child in node.childrens:
      if not child.isVisited:
        print("\t{}-Child".format(node.value),child.value, catstreak)
        rests += inner(child, catstreak, limit)
    return rests

  return inner(graph.root, 0, limit)
  

if __name__ == "__main__":
  graph, limit = make_graph()
  print(graph.nodes)
  print(custom_dfs(graph, limit))
  