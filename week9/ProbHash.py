"""ProbHash"""
class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None]
        self.n = cap
    
    def hashFunction(self, mykey):
        return  mykey % self.n
    
    def rehashFunction(self, hashkey):
        return (hashkey+2) % self.n
    
    def insertData(self, student_obj):
        key = student_obj.getID()
        h = self.hashFunction(key)
        for _ in range(self.n):
            if self.hashtable[h] is None:
                self.hashtable[h] = student_obj
                return
            else:
                h = self.rehashFunction(h)
        return print("connot insert")
    
    def searchData(self, key):
        h = self.hashFunction(key)
        for _ in range(self.n):
            if self.hashtable[h] is not None:
                if self.hashtable[h].getID() == key:
                    print("Found %d at index %d" % (key, h))
                    return self.hashtable[h]
                else:
                    h = self.rehashFunction(h)
            else:
                h = self.rehashFunction(h)
        return print(str(key)+" dose not exist")
