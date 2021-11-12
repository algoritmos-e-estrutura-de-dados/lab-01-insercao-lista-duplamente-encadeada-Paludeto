
class Node:

    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Lista:

    def __init__(self):
        self.init = None
        self.tail = None

    def append(self, node):

        if self.init is None:
            new_node = Node(node)
            new_node.prev = None;
            self.init = new_node
        else: 
            new_node = Node(node)
            last = self.init
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
            new_node.next = None

    def prepend(self, node):

        if self.init is None:
            new_node = Node(node)
            new_node.prev = None
            self.init = new_node
        else: 
            new_node = Node(node)
            self.init.prev = new_node
            new_node.next = self.init
            self.init = new_node
            new_node.prev = None    

    def __str__(self):
        
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x) + ','
            node_aux = node_aux.next
        str_aux += ']'
        return str_aux

    def print_list(self): #criado para debug
        
        last = self.init
        while last:
            print(last.x)
            last = last.next


if __name__ == '__main__':
    lista = Lista()
    lista.append(Node(27))
    lista.append(Node(1))
    lista.print_list()
    lista.prepend(Node(5))
    lista.prepend(Node(19))
    lista.print_list()
