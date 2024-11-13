def delete(self, value):
    node_to_remove = self.search(value)

    if node_to_remove is None:
        return

    if node_to_remove.left is None or node_to_remove.right is None:
        self._replace_node(
            node_to_remove, node_to_remove.left or node_to_remove.right)
    else:
        successor = self._find_min(node_to_remove.right)
        node_to_remove.value = successor.value
        self._replace_node(successor, successor.right)

    self.delete_fix(node_to_remove)

def delete_fix(self, x):
    while x != self.root and x.color == 'black':
        if x == x.parent.left:
            sibling = x.sibling()
            if sibling.color == 'red':
                sibling.color = 'black'
                x.parent.color = 'red'
                self.rotate_left(x.parent)
                sibling = x.sibling()
            if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                sibling.color = 'red'
                x = x.parent
            else:
                if sibling.right is None or sibling.right.color == 'black':
                    sibling.left.color = 'black'
                    sibling.color = 'red'
                    self.rotate_right(sibling)
                    sibling = x.sibling()
                sibling.color = x.parent.color
                x.parent.color = 'black'
                if sibling.right:
                    sibling.right.color = 'black'
                self.rotate_left(x.parent)
                x = self.root
        else:
            sibling = x.sibling()
            if sibling.color == 'red':
                sibling.color = 'black'
                x.parent.color = 'red'
                self.rotate_right(x.parent)
                sibling = x.sibling()
            if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                sibling.color = 'red'
                x = x.parent
            else:
                if sibling.left is None or sibling.left.color == 'black':
                    sibling.right.color = 'black'
                    sibling.color = 'red'
                    self.rotate_left(sibling)
                    sibling = x.sibling()
                sibling.color = x.parent.color
                x.parent.color = 'black'
                if sibling.left:
                    sibling.left.color = 'black'
                self.rotate_right(x.parent)
                x = self.root
    x.color = 'black'
