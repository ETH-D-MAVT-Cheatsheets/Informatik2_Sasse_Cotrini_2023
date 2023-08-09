def rect_intersect(self, lr, ur):
    def intervals_overlap(a_start, a_end, b_start, b_end):
        a_end_in_b = b_start <= a_end <= b_end
        b_end_in_a = a_start <= b_end <= a_end
        return a_end_in_b or b_end_in_a
    self_lx, self_ly = self.l
    self_ux, self_uy = self.u
    rect_lx, rect_ly = lr
    rect_ux, rect_uy = ur
    return (intervals_overlap(self_lx, self_ux,
                              rect_lx, rect_ux) and
            intervals_overlap(self_ly, self_uy,
                              rect_ly, rect_uy))

def covered_by_rect(self, lr, ur):
    self_lx, self_ly = self.l
    self_ux, self_uy = self.u
    rect_lx, rect_ly = lr
    rect_ux, rect_uy = ur
    return (rect_lx <= self_lx and 
            rect_ly <= self_ly and
            self_ux <= rect_ux and
            self_uy <= rect_uy)


def count_in_rect(self, lr, ur):
    if self.rect_intersect(lr, ur):
        if self.children is None:
            pts = [p for p in self.points if lr[0] <= p[0] <= ur[0] and lr[1] <= p[1] <= ur[1]]
            return len(pts)
        else:
            return sum(c.count_in_rect(lr, ur) for c in self.children)
    elif self.covered_by_rect(lr, ur):
        return self.size()
    else:
        return 0 