import matplotlib.pyplot as plt
import random

def random_walk(vertexes, N):
    "Walk halfway from current point towards a random vertex; repeat for N points."
    points = [random.choice(vertexes)]
    for _ in range(N-1):
        points.append(midpoint(points[-1], random.choice(vertexes)))
    return points

def show_walk(vertexes, N=5000):
    "Walk halfway towards a random vertex for N points; show results."
    Xs, Ys = transpose(random_walk(vertexes, N))
    Xv, Yv = transpose(vertexes)
    plt.plot(Xs, Ys, 'r.')
    plt.plot(Xv, Yv, 'bs')
    plt.gca().set_aspect('equal')
    plt.gcf().set_size_inches(9, 9)
    plt.axis('off')
    plt.show()
    
def midpoint(p, q): return ((p[0] + q[0])/2, (p[1] + q[1])/2)

def transpose(matrix): return zip(*matrix)

triangle = ((0, 0), (0.5, (3**0.5)/2), (1, 0))
show_walk(triangle, 20000)

# square = ((0, 0), (0, 1), (1, 0), (1, 1))
# show_walk(square, 20000)

# right_triangle = ((0, 0), (0, 1), (1, 0))
# show_walk(right_triangle, 20000)

# pentagon = ((0.5, -0.688), (0.809, 0.262), (0., 0.850), (-0.809, 0.262), (-0.5, -0.688))
# show_walk(pentagon, 20000)
