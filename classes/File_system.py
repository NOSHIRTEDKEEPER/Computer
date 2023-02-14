

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


root = TreeNode("/")
a = TreeNode("bin/")
b = TreeNode("boot/")
c = TreeNode("dev")
d = TreeNode("etc")
e = TreeNode("home")
f = TreeNode("lib")
g = TreeNode("media")
h = TreeNode("mnt")
i = TreeNode("opt")
j = TreeNode("proc")
k = TreeNode("root")
l = TreeNode("run")
m = TreeNode("sbin")
n = TreeNode("system")
o = TreeNode("tmp")
p = TreeNode("usr")
q = TreeNode("var")

root.add_child(a)
root.add_child(b)
root.add_child(c)
root.add_child(d)
root.add_child(e)
root.add_child(f)
root.add_child(g)
root.add_child(h)
root.add_child(i)
root.add_child(j)
root.add_child(k)
root.add_child(l)
root.add_child(m)
root.add_child(n)
root.add_child(o)
root.add_child(p)
root.add_child(q)

root.traverse()


class View_filesys:
    def __init__(self, File_system):
        self.filesys = File_system.stringify_list()
