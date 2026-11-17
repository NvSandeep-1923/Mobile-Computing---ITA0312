"""Q4: OFDM subcarrier orthogonality and OFDMA allocation/fairness comparison."""
import numpy as np

SEED = 44
N = 64
USERS = 8
REALISATIONS = 1000
SNR = 10.0


def jain(values):
    values = np.asarray(values, dtype=float)
    denom = len(values) * np.sum(values ** 2)
    return float(np.sum(values) ** 2 / denom) if denom else 0.0


def main():
    rng = np.random.default_rng(SEED)
    n = np.arange(N)
    phi = np.exp(1j * 2 * np.pi * np.outer(n, np.arange(N)) / N)
    print("Q4 — OFDMA: SUBCARRIER ALLOCATION AND FAIRNESS")
    print("Normalised OFDM subcarrier inner products, N=64:")
    for a, b in ((0, 0), (0, 1), (0, 2), (1, 2)):
        val = np.vdot(phi[:, b], phi[:, a]) / N
        print(f"  ({a},{b}) = {val.real:+.3e}{val.imag:+.3e}j")

    totals = {name: [] for name in ("Fixed contiguous", "Interleaved round-robin", "Best-subcarrier")}
    fairs = {name: [] for name in totals}
    for _ in range(REALISATIONS):
        gain = rng.exponential(1.0, size=(USERS, N))
        rate = np.log2(1 + SNR * gain)
        allocations = {
            "Fixed contiguous": [np.arange(u * 8, (u + 1) * 8) for u in range(USERS)],
            "Interleaved round-robin": [np.arange(u, N, USERS) for u in range(USERS)],
        }
        best_user = np.argmax(gain, axis=0)
        allocations["Best-subcarrier"] = [np.where(best_user == u)[0] for u in range(USERS)]
        for name, blocks in allocations.items():
            user_rates = np.array([rate[u, blocks[u]].sum() for u in range(USERS)])
            totals[name].append(float(user_rates.sum()))
            fairs[name].append(jain(user_rates))

    print(f"Simulation: {REALISATIONS} fading realisations, {USERS} users, {N} subcarriers, SNR=10 dB.")
    print("Strategy                  Mean sum-rate (bit/s/Hz)   Mean Jain fairness")
    for name in totals:
        print(f"{name:<26} {np.mean(totals[name]):>12.3f}              {np.mean(fairs[name]):>8.4f}")
    print("Decision: guarantee a minimum share, then use channel-aware assignment for lecture-hall fairness.")
    print("Evidence: seeded Rayleigh-fading teaching simulation, not a standards PHY implementation.")


if __name__ == "__main__":
    main()
