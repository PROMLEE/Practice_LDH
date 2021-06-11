def splay(self, v):
        while v and v.parent != None:
            p = v.parent
            if p.parent == None:
                if p.left == v: # rotateRight at v.parent = p
                    self.rotateRight(p)
                else:
                    self.rotateLeft(p)
            else:
                pp = p.parent
            if p.left == v and pp.left == p:
                self.rotateRight(p)
                self.rotateRight(v.parent)
            elif p.right == v and pp.right == p:
                self.rotateLeft(p)
                self.rotateLeft(v.parent)

            elif p.left == v and pp.right == p:
                self.rotateRight(p)
                self.rotateLeft(v.parent)
            else:
                self.rotateLeft(p)
                self.rotateRight(v.parent)
        return v

    def search(self, key):
            v = super(splayTree, self).search(key)
            if v:
                self.root = self.splay(v)
            return v

    def insert(self, key):
        v = super(splayTree, self).insert(key)
        if v:
            self.root = self.splay(v)
        return v

    def delete(self, x): # delete "node" x (not key)
        if x == None: return
        self.splay(x)               # splay x, then it will be the root
        L, R = x.left, x.right
        m = L
        while m and m.right:
            m = m.right
        if m:
            L.parent = None             # current root is L whose parent should be None
            self.root = self.splay(m)   # m will be the root, so m.right is None
            m.right = R

        if R: R.parent = m          # R becomes the right subtree of m
            self._update_height(m)
            else:                           # L is empty
                self.root = R
                if R: R.parent = None