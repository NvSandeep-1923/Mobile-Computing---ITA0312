"""Q7: Paired OFDMA validation — best-subcarrier versus minimum-share redesign."""
import numpy as np

SEED = 77
REALISATIONS = 1000
USERS = 8
SUBCARRIERS = 64
MIN_SHARE = 4
SNR = 10.0


def jain(x):
    x = np.asarray(x, dtype=float)
    d = len(x) * np.sum(x ** 2)
    return float(np.sum(x) ** 2 / d) if d else 0.0


def evaluate(gain):
    rate = np.log2(1 + SNR * gain)
    best_user = np.argmax(gain, axis=0)
    original_alloc = [np.where(best_user == u)[0].tolist() for u in range(USERS)]
    redesigned_alloc = [[] for _ in range(USERS)]
    remaining = set(range(SUBCARRIERS))
    # Stage 1: allocate four resources/user, choosing each user's best unassigned subcarrier.
    for u in range(USERS):
        for _ in range(MIN_SHARE):
            k = max(remaining, key=lambda idx: rate[u, idx])
            redesigned_alloc[u].append(k)
            remaining.remove(k)
    # Stage 2: allocate remaining resources to the user with the highest rate.
    for k in sorted(remaining):
        u = int(np.argmax(rate[:, k]))
        redesigned_alloc[u].append(k)

    def metrics(allocation):
        user_rates = np.array([sum(rate[u, k] for k in allocation[u]) for u in range(USERS)])
        counts = np.array([len(x) for x in allocation])
        return user_rates.sum(), user_rates.min(), jain(user_rates), int(np.sum(counts == 0)), counts
    return metrics(original_alloc), metrics(redesigned_alloc)


def main():
    rng = np.random.default_rng(SEED)
    results = {"Best-subcarrier": [], "Minimum-share": []}
    alloc_counts = {"Best-subcarrier": [], "Minimum-share": []}
    for _ in range(REALISATIONS):
        gain = rng.exponential(1.0, size=(USERS, SUBCARRIERS))
        old, new = evaluate(gain)  # paired: both schedulers see the same gain matrix
        for name, result in (("Best-subcarrier", old), ("Minimum-share", new)):
            results[name].append(result[:4])
            alloc_counts[name].append(result[4])

    print("Q7 — DAY-4 DESIGN CHALLENGE: DIAGNOSE, REDESIGN AND VALIDATE")
    print(f"Paired runs={REALISATIONS}; users={USERS}; subcarriers={SUBCARRIERS}; SNR=10 dB; min share={MIN_SHARE}.")
    print("Policy             Sum rate    Min user rate   Jain fairness   Zero-resource users")
    for name, rows in results.items():
        a = np.asarray(rows)
        print(f"{name:<18} {a[:,0].mean():>9.3f} {a[:,1].mean():>15.3f}"
              f" {a[:,2].mean():>15.4f} {a[:,3].mean():>20.3f}")
    print("Mean allocated subcarriers per user (users 1–8):")
    for name, rows in alloc_counts.items():
        avg = np.mean(np.asarray(rows), axis=0)
        print(f"  {name:<18}: " + ", ".join(f"{v:.1f}" for v in avg))
    print("Evidence: paired seeded teaching simulation; values depend on the stated scheduler rule.")


if __name__ == "__main__":
    main()
