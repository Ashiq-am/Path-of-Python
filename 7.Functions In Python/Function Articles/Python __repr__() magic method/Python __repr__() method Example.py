class GFG:

    def __init__(self, f_name, m_name, l_name):
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name

    def __repr__(self):
        return f'GFG("{self.f_name}","{self.m_name}","{self.l_name}")'


gfg = GFG("Geeks", "For", "Geeks")
print(repr(gfg))
