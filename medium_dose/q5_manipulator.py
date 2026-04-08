import sys

def generate_valid_configs(target, L1, L2, L3, D):
    configs = []
    for inner in range(min(L1, target) + 1):
        for outer in range(min(L3, target) + 1):
            if abs(inner - outer) > D:
                continue
            middle = target - inner - outer
            if 0 <= middle <= L2:
                configs.append((inner, middle, outer))
    return configs


def transition_cost(prev, curr, W):
    W1, W2, W3 = W
    return (abs(curr[0] - prev[0]) * W1 +
            abs(curr[1] - prev[1]) * W2 +
            abs(curr[2] - prev[2]) * W3)


def min_wear_cost(limits, wear_factors, targets, D):
    L1, L2, L3 = limits
    W = wear_factors

    start = (0, 0, 0)

    # dp maps config → (min_cost, previous_config)
    dp = {start: (0, None)}

    # Store dp at each step for path reconstruction
    dp_history = []

    for target in targets:
        valid_configs = generate_valid_configs(target, L1, L2, L3, D)

        if not valid_configs:
            print(f"No valid configuration for target {target}!")
            return -1

        new_dp = {}

        for curr_config in valid_configs:
            best_cost = sys.maxsize
            best_prev = None

            for prev_config, (prev_cost, _) in dp.items():
                cost = prev_cost + transition_cost(prev_config, curr_config, W)
                if cost < best_cost:
                    best_cost = cost
                    best_prev = prev_config

            new_dp[curr_config] = (best_cost, best_prev)

        dp_history.append((target, new_dp))
        dp = new_dp

    # Find best final config
    best_final = min(dp, key=lambda c: dp[c][0])
    best_cost  = dp[best_final][0]

    # ── Reconstruct path ──
    print("\n── Optimal path ──")
    path = []
    config = best_final

    # Walk backwards through dp_history
    for t_idx in range(len(targets) - 1, -1, -1):
        _, dp_step = dp_history[t_idx]
        cumulative_cost, prev_config = dp_step[config]
        path.append((targets[t_idx], config, cumulative_cost, prev_config))
        config = prev_config

    path.reverse()

    # Print path forward
    prev_config = (0, 0, 0)
    print(f"Start → {prev_config}")
    for target, config, cumulative, _ in path:
        step = transition_cost(prev_config, config, W)
        print(f"Target {target:>4} → config {config} | "
              f"step cost {step:>4} | cumulative cost {cumulative}")
        prev_config = config

    return best_cost


if __name__ == "__main__":
    limits       = list(map(int, input("Enter limits (L1 L2 L3): ").split()))
    wear_factors = list(map(int, input("Enter wear factors (W1 W2 W3): ").split()))
    targets      = list(map(int, input("Enter targets: ").split()))
    D            = int(input("Enter max diff D: "))

    print("=== Manipulator Arm — Minimum Wear Cost ===\n")
    print(f"Limits       : {limits}")
    print(f"Wear factors : {wear_factors}")
    print(f"Targets      : {targets}")
    print(f"Max diff (D) : {D}")

    result = min_wear_cost(limits, wear_factors, targets, D)
    print(f"\nMinimum total wear cost: {result}")