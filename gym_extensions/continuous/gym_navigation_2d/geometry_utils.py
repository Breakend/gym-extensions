import scipy
from scipy import stats
import numpy as np
from math import sqrt
from itertools import product

def closest_point_on_segment(p, a, b):
    lsqr = (a[0]-b[0])**2 + (a[1]-b[1])**2
    pa = p-a
    ba = b-a

    if (lsqr < 1e-15):
        return a

    t_opt = pa.dot(ba) / lsqr
    t_opt = max(min(t_opt, 1), 0)
    cp = a + t_opt * (b-a)
    return cp

def point_to_segment_distance(p, a, b):
    cp = closest_point_on_segment(p, a, b)
    return np.linalg.norm(cp - p) 

def point_to_rectangle_distance(p, ca, wa, ha):

    if (abs(p-ca) < np.array([wa/2.0, ha/2.0])).all():
        return 0.
    
    a1 = ca + np.array([wa/2.0, ha/2.0])
    a2 = ca + np.array([wa/2.0, -ha/2.0])
    a3 = ca + np.array([-wa/2.0, -ha/2.0])
    a4 = ca + np.array([-wa/2.0, ha/2.0])

    d1 = point_to_segment_distance(p, a1, a2)
    d2 = point_to_segment_distance(p, a2, a3)
    d3 = point_to_segment_distance(p, a3, a4)
    d4 = point_to_segment_distance(p, a4, a1)
    return min([d1, d2, d3, d4])

def point_is_on_left(a, b, c):
    """Returns true iff c is on the left of the infinite line ab"""
    return (a[0] - c[0]) * (b[1] - c[1]) > (a[1] - c[1]) * (b[0] - c[0])
    
def segments_intersect(a, b, c, d):
    """Returns true iff the line segments ab and cd intersect""" 
    epsilon = 1e-10
    
    if point_to_segment_distance(a, c, d) < epsilon or point_to_segment_distance(b, c, d) < epsilon:
        return True

    if point_to_segment_distance(c, a, b) < epsilon or point_to_segment_distance(d, a, b) < epsilon:
        return True

    return point_is_on_left(a,b,c) != point_is_on_left(a,b,d) and point_is_on_left(c,d,a) != point_is_on_left(c,d,b)

def rectangle_edges(z1,z2,z3,z4):
    yield (z1, z2)
    yield (z2, z3)
    yield (z3, z4)
    yield (z4, z1)

def rectangle_vertices(c,w,h):
    yield c + np.array([w/2.0, h/2.0])
    yield c + np.array([w/2.0, -h/2.0])
    yield c + np.array([-w/2.0, -h/2.0])
    yield c + np.array([-w/2.0, h/2.0])

    
def rectangles_intersect(ca,wa,ha, q1,q2,q3,q4):
    a1 = ca + np.array([wa/2.0, ha/2.0])
    a2 = ca + np.array([wa/2.0, -ha/2.0])
    a3 = ca + np.array([-wa/2.0, -ha/2.0])
    a4 = ca + np.array([-wa/2.0, ha/2.0])

    cq = (q1 + q2 + q3 + q4)/4.0
    cq_is_in_rectangle = abs(cq[0] - ca[0]) < wa/2.0 and abs(cq[1] - ca[1]) < ha/2.0 
    
    segment_intersections = [segments_intersect(e1[0], e1[1], e2[0], e2[1]) for e1, e2 in product(rectangle_edges(a1,a2,a3,a4), rectangle_edges(q1,q2,q3,q4))]
    return any(segment_intersections) or cq_is_in_rectangle


def rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb):
    a1 = ca + np.array([wa/2.0, ha/2.0])
    a2 = ca + np.array([wa/2.0, -ha/2.0])
    a3 = ca + np.array([-wa/2.0, -ha/2.0])
    a4 = ca + np.array([-wa/2.0, ha/2.0])

    b1 = cb + np.array([wb/2.0,   hb/2.0])
    b2 = cb + np.array([wb/2.0,  -hb/2.0])
    b3 = cb + np.array([-wb/2.0, -hb/2.0])
    b4 = cb + np.array([-wb/2.0,  hb/2.0])
        
    for e1, e2 in product(rectangle_edges(a1,a2,a3,a4), rectangle_edges(b1,b2,b3,b4)):
        if segments_intersect(e1[0], e1[1], e2[0], e2[1]):
            return 0.0
    
    da1 = point_to_rectangle_distance(a1, cb, wb, hb)
    da2 = point_to_rectangle_distance(a2, cb, wb, hb)
    da3 = point_to_rectangle_distance(a3, cb, wb, hb)
    da4 = point_to_rectangle_distance(a4, cb, wb, hb)

    db1 = point_to_rectangle_distance(b1, ca, wa, ha)
    db2 = point_to_rectangle_distance(b2, ca, wa, ha)
    db3 = point_to_rectangle_distance(b3, ca, wa, ha)
    db4 = point_to_rectangle_distance(b4, ca, wa, ha)    
    return min([da1, da2, da3, da4, db1, db2, db3, db4])
