def add_edge(self, u, v):
    if (u in self.U and v in self.V) or (u in self.V and v in self.U):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    else:
        raise ValueError("Edge must connect vertices from different sets")
