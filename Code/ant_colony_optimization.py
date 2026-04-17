import random
import math

def aco_bin_packing(items, capacity, ants=20, iterations=50):
    n = len(items)
    pheromone = [1.0] * n
    best_bins = float('inf')

    for _ in range(iterations):
        for _ in range(ants):
            order = sorted(range(n), key=lambda i: random.random() * pheromone[i])
            bins = []

            for idx in order:
                item = items[idx]
                placed = False
                for b in bins:
                    if sum(b) + item <= capacity:
                        b.append(item)
                        placed = True
                        break
                if not placed:
                    bins.append([item])

            if len(bins) < best_bins:
                best_bins = len(bins)

        for i in range(n):
            pheromone[i] *= 0.9
            pheromone[i] += 1.0 / best_bins

    return best_bins
