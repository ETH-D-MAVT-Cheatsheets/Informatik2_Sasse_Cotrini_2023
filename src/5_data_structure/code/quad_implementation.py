class QuadTree:
    def __init__(self, l, u, max_cap):
        self.l = l #lower left corner coordinate
        self.u = u #upper right corner coordinate
        self.m = max_cap
        self.points = []
        self.children = None
        self.count = 0 #points within quadtree