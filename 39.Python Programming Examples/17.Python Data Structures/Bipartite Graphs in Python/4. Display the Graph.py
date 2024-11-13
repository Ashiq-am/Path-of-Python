def display(self):
    print("Set U:", self.U)
    print("Set V:", self.V)
    print("Adjacency List:")
    for vertex, neighbors in self.adj_list.items():
        print(f"{vertex}: {neighbors}")
