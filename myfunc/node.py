class Node:
    def __init__(self, price):
        self.price = price
        self.left = None
        self.right = None
    
    def insert(self, price):
        if price < self.price :
            if self.left:
                self.left.insert(price)
            else:
                self.left = Node(price)
                
        elif price > self.price :
            if self.right: #ถ้ามีnodeทางขวาอยู่เเล้วก็ดันไปให้ทางขวา
                self.right.insert(price)
            else:  #ถ้าไม่มีnodeใหม่
                self.right = Node(price)
                
    def print(self,p=""):
        print(p,self.price)
        if self.left:
            q=p+"-"
            self.left.print(q)
        if self.right:
            q=p+"*"
            self.right.print(q)
                
    def inorder(self): #น้อยไปมาก
        if self.left:
            self.left.inorder()
        print(self.price, end = " ")
        if self.right:
            self.right.inorder()
            
    def search(self, price):
        if price == self.price:
            return True, self
        if self.left and price < self.price:
            return self.left.search(price)
        if self.right and price > self.price:
            return self.right.search(price)
            return False, None 
        
    def min(self):
        # if self.left:
        #     return self.left.min()
        #     return self
        if not self.left:
            return self
        return self.left.min()
        
    def max(self):
        # if self.right:
        #     return self.right.max()
        #     return self
        if not self.right:
            return self
        return self.right.max()
        
    def min_max(self):
        if self.left:
            if  self.left.price >= self.left.min().price:
                print(self.price, end = " ")
        if self.right:
            if  self.left.price <= self.right.max().price:
                print(self.price, end = " ")
        
    def remove(self, s,):
        m = s.right
        l = s.right
        while m.left:
            l = m 
            m = m.left 
        if m.price != l.price:
            m.right = s.right 
        l.left = None 
        m.left = s.left
        del s 
        return m 

    def delete(self, price):
        if self.price == price:
            return True, self
        if self.left and price < self.price:
            r,s = self.left.delete(price)
            if r:
                if s.left is None and s.right is None:
                    self.left = None 
                    del s
                elif s.left and s.right:
                    m = self.remove(s)
                    self.left = m 
                elif s.left or s.right:
                    self.left = s.left if s.left else s.right
                    del s 
        if self.right:
            r,s = self.right.delete(price)
            if r:
                if s.left is None and s.right is None:
                    self.right = None 
                    del s 
                elif s.left and s.right:
                    m = self.remove(s)
                    self.right = m 
                elif s.left or s.right:
                    self.right = s.left if s.left else s.right
                    del s  
                    return False, None 