class Node:
  def __init__(self,value,parent=None):
    self.children = []
    self.value = value
    self.cat = 0
    self.parent = parent
    self.isVisited = False

  def add_child(self,node):
    self.children.append(node)

  def add_parent(self, node):
    self.parent = node
    node.children.append(self)

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
    if src:
      src.add_child(dst)

  def hasCat(self,node):
    self.nodes[node].cat = 1

  def visit_node(self,node):
    self.isVisited[node.value] = True

  def get_children(self,node):
    return [i for i in node.children if not self.isVisited[i.value]]  

    
def make_graph():
  v = int(input())
  graph = Graph(v)
  parentless_nodes = []
  for i in range(1, v+1):
    parent_val = int(input())
    # parent_node = graph.nodes[parent_val] if parent_val != -1 else None
    if parent_val != -1:
      parent_node = graph.nodes[parent_val]
    else:
      parent_node = None
      parentless_nodes.append(graph.nodes[i])
      # print(parentless_nodes)

    graph.add_edge(parent_node, graph.nodes[i])
  # for node in graph.nodes.keys():
    # print(graph.nodes[node].children)

  
  return graph, parentless_nodes

def get_groups(graph, roots):
  heights = []
  # print(roots)
  for node in roots:
    stack = [(node,0)]
    h = 0
    while stack:
      node,h = stack.pop()
      graph.visit_node(node)
      h+=1
      minions = graph.get_children(node)
      if len(minions) == 0:
        continue
      else:
        stack.extend([(i,h) for i in minions])
    # print(h)
    heights.append(h)
  return (heights)
      
    
graph, roots = make_graph()
print(get_groups(graph,roots))