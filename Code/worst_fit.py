def worst_fit(items, capacity):
    bins = []
    for item in items:
        max_space = -1
        worst_bin = None

        for b in bins:
            space = capacity - sum(b)
            if space >= item and space > max_space:
                max_space = space
                worst_bin = b

        if worst_bin:
            worst_bin.append(item)
        else:
            bins.append([item])
    return bins
