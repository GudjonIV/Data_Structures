# Author: Guðjón Ingi Valdimarsson
# Date: 17.03.2020

class LCRNode():
    def __init__(self, data=None, left=None, center=None, right=None):
        self.data = data
        self.left = left
        self.center = center
        self.right = right

class LRCMap:
    def __init__(self, build = False):
        if build:
            self.root = LCRNode()
            self._build_tree_rec(self.root)
        else:
            self.root = LCRNode()
    
    def _build_tree_rec(self, root, size=7):
        if size != 0:
            root.left = LCRNode()
            root.center = LCRNode()
            root.right = LCRNode()
            self._build_tree_rec(root.left, size - 1)
            self._build_tree_rec(root.center, size - 1)
            self._build_tree_rec(root.right, size - 1)

    def put_data(self, key, data):
        self._get_node(key, self.root).data = data

    def get_data(self, key): # returns data for that key or None if non-existant
        node = self._get_node(key, self.root, True)
        if node:
            return node.data
        return None

    def _get_node(self, key, root, search=False): # Finds and returns the Node that is being looked for, None if search is true and node does not exist
        if key == "":
            return root
        else:
            if key[0] == "l":
                if root.left == None and search:
                    return None
                elif root.left == None:
                    root.left = LCRNode()
                return self._get_node(key[1:], root.left, search)

            elif key[0] == "c":
                if root.center == None and search:
                    return None
                elif root.center == None:
                    root.center = LCRNode()
                return self._get_node(key[1:], root.center, search)

            elif key[0] == "r":
                if root.right == None and search:
                    return None
                elif root.right == None:
                    root.right = LCRNode()
                return self._get_node(key[1:], root.right, search)
            
            else:
                print ("Invalid search string! {} is not valid".format(key[0]))
            

class HashMap:
    def __init__(self):
        self.array_length = 16
        # MUST USE ONE OF THE FOLLOWING LINES, BUT NOT BOTH
       # self.hash_table = [ [ ] for _ in range(self.array_length) ]
        self.hash_table = [ { } for _ in range(self.array_length) ]
        self.item_count = 0

    def _hash(self, key):
        a = 41
        ret = 0
        for index, c in enumerate(str(key)):
            ret += (a**index) * ord(c)
        return ret % self.array_length

    def __setitem__(self, key, data): # overrides/updates if already there
        index = self._hash(key)
        if self.__getitem__(key) == None:
            self.item_count += 1
        self.hash_table[index][key] = data

    def __getitem__(self, key): # returns data - returns None if nothing there
        index = self._hash(key)
        try:
            return self.hash_table[index][key]
        except KeyError:
            return None

    def __len__(self):
        return self.item_count


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    tm = LRCMap()
    tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")
    tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")
    print(tm.get_data("lrl"))
    print(tm.get_data("lrcclc"))
    print(tm.get_data("lc"))

    tm = LRCMap(True)
    tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")
    tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")
    print(tm.get_data("lrlrcclc"))
    print(tm.get_data("lrlclc"))
    print(tm.get_data("lrlrccr"))


    hm = HashMap()
    hm["key_value:345"] = "THIS IS THE DATA FOR KEY: key_value:345"
    hm[345] = "THIS IS THE DATA FOR KEY: 345"
    print(hm[345])
    print(hm[346])
    print(hm["key_value:345"])
    print(len(hm))
    hm[345] = "THIS IS THE NEW DATA FOR KEY: 345"
    print(hm[345])
    print(len(hm))
