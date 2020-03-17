# Author: Guðjón Ingi Valdimarsson
# Date: 17.03.2020

# Implement helper classes here
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

    def _put_recur(self, key, data, root):
        if key == "":
            root.data = data
        else:
            if key[0] == "l":
                if root.left == None:
                    root.left = LCRNode()
                self._put_recur(key[1:], data, root.left)

            elif key[0] == "c":
                if root.center == None:
                    root.center = LCRNode()
                self._put_recur(key[1:], data, root.center)

            elif key[0] == "r":
                if root.right == None:
                    root.right = LCRNode()
                self._put_recur(key[1:], data, root.right)

            else:
                print ("Key string is invalid!")

    def put_data(self, key, data):
        self._put_recur(key, data, self.root)

    def  _get_recur(self, key, root):
        if key == "":
            return root.data
        else:
            if key[0] == "l":
                if root.left == None:
                    return None
                return self._get_recur(key[1:], root.left)

            if key[0] == "c":
                if root.center == None:
                    return None
                return self._get_recur(key[1:], root.center)
                
            if key[0] == "r":
                if root.right == None:
                    return None
                return self._get_recur(key[1:], root.right)
                

    def get_data(self, key): # returns data for that key or None if non-existant
        return self._get_recur(key, self.root)


class HashMap:
    def __init__(self):
        self.array_length = 16
        # MUST USE ONE OF THE FOLLOWING LINES, BUT NOT BOTH
       # self.hash_table = [ [ ] for _ in range(self.array_length) ]
       # self.hash_table = [ { } for _ in range(self.array_length) ]
        self.item_count = 0

    def __setitem__(self, key, data): # overrides/updates if already there
        pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING

    def __getitem__(self, key): # returns data - returns None if nothing there
        pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING

    def __len__(self):
        return 0


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
