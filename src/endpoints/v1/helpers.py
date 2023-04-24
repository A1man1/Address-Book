import math

def find_new_point_from_distance(x1,y1,d):
    R= 3963.0
    theta = (d/R)
    x2 = x1 + d * math.cos(theta)
    y2 = y1 + d * math.sin(theta)
    return (x2,y2)

def create_data(rows):
    return_data = []
    for rec in rows:
        data = dict(zip(rec.keys(), rec.values()))
        return_data.append(data)
    return return_data