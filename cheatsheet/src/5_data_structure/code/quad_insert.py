def subdivide(self):
    lx, ly = self.l
    ux, uy = self.u
    mx, my = (lx + ux) / 2, (ly + uy) / 2
    self.children = [None, None, None, None]
    self.children[0] = QuadTree((lx, ly),(mx, my),self.m)
    self.children[1] = QuadTree((mx, ly),(ux, my),self.m)
    self.children[2] = QuadTree((mx, my),(ux, uy),self.m)
    self.children[3] = QuadTree((lx, my),(mx, uy),self.m)

def get_index(self, point):
    lx, ly = self.l
    ux, uy = self.u
    mx, my = (lx + ux) / 2, (ly + uy) / 2
    px, py = point
    if lx <= px < mx:
        if ly <= py < my:
            return 0
        elif my <= py <= uy:
            return 3
    elif mx <= px <= ux:
        if ly <= py < my:
            return 1
        elif my <= py <= uy:
            return 2
    return None


def insert(self, point):
    if self.children is not None:
        index = self.get_index(point)
        if index is not None:
            self.children[index].insert(point)
            self.count += 1
            return
    self.points.append(point)
    if len(self.points) > self.m:
        self.subdivide()
        for point in self.points:
            index = self.get_index(point)
            if index is not None:
                self.children[index].insert(point)
                self.count += 1
        self.points = []
