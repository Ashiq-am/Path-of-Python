class TrieNode :
    def __init__(self):
        self.children = {}

class Trie :
    def __init__(self) :
        self.root = TrieNode()

    def insert(self, n) :
        temp = self.root
        i = 31
        while i >= 0 :
            bit = (n >> i) & 1
            if bit not in temp.children:
                temp.children[bit] = TrieNode()
            temp = temp.children[bit]
            i -= 1


    def max_xor_helper(self, value) :
        temp = self.root
        current_ans = 0
        i = 31
        while i >= 0:
            bit = (value >> i) & 1
            if bit^1 in temp.children:
                temp = temp.children[bit^1]
                current_ans += (1 << i)

            else:
                temp = temp.children[bit]
            i -= 1
        return current_ans

class Solution:
    def solve(self, A):
        trie = Trie()
        max_val = 0
        trie.insert(A[0])
        for n in A[1:]:
            max_val = max(trie.max_xor_helper(n),max_val)
            trie.insert(n)
        return max_val


if __name__=="__main__":
    A = [25, 10, 2, 8, 5, 3]
    print(Solution().solve(A))
