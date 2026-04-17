import random
import math

def simulated_annealing_bin_packing(items, capacity,
                                    initial_temp=1000,
                                    cooling_rate=0.995,
                                    iterations=5000):

    bins = []
    space_left = []

    for item in items:
        placed = False
        for i in range(len(bins)):
            if space_left[i] >= item:
                bins[i].append(item)
                space_left[i] -= item
                placed = True
                break
        if not placed:
            bins.append([item])
            space_left.append(capacity - item)

    current_solution = bins
    best_solution = [b[:] for b in bins]
    best_cost = len(best_solution)

    temperature = initial_temp

    for _ in range(iterations):
        if temperature <= 1e-3:
            break

        new_solution = [b[:] for b in current_solution]

        if len(new_solution) <= 1:
            break

        from_bin = random.randint(0, len(new_solution) - 1)
        if not new_solution[from_bin]:
            continue

        item = random.choice(new_solution[from_bin])
        new_solution[from_bin].remove(item)

        placed = False
        for b in new_solution:
            if sum(b) + item <= capacity:
                b.append(item)
                placed = True
                break

        if not placed:
            new_solution.append([item])

        new_solution = [b for b in new_solution if b]

        new_cost = len(new_solution)
        current_cost = len(current_solution)

        if (new_cost < current_cost or
            random.random() < math.exp((current_cost - new_cost) / temperature)):
            current_solution = new_solution

            if new_cost < best_cost:
                best_solution = [b[:] for b in new_solution]
                best_cost = new_cost

        temperature *= cooling_rate

    return best_cost
