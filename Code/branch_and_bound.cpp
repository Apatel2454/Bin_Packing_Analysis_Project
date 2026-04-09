#include <vector>
#include <algorithm>
#include <chrono>
#include "metrics.h"

static const int CAP = 100;

int best;
int OPT;

void dfs(std::vector<int>& items, int idx, std::vector<int>& bins) {
    if (idx == items.size()) {
        best = std::min(best, (int)bins.size());
        return;
    }

    if (bins.size() >= best) return;

    int x = items[idx];

    for (int i = 0; i < bins.size(); i++) {
        if (bins[i] + x <= CAP) {
            bins[i] += x;
            dfs(items, idx + 1, bins);
            bins[i] -= x;
        }
    }

    bins.push_back(x);
    dfs(items, idx + 1, bins);
    bins.pop_back();
}

Result branchAndBound(std::vector<int> items) {
    auto start = std::chrono::high_resolution_clock::now();
    long long mem_before = getMemoryUsageKB();

    sort(items.rbegin(), items.rend());
    best = items.size();

    std::vector<int> bins;
    dfs(items, 0, bins);

    OPT = best;

    auto end = std::chrono::high_resolution_clock::now();
    long long mem_after = getMemoryUsageKB();

    return {
        best,
        std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count(),
        mem_after - mem_before,
        1.0
    };
}
