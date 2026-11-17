"""Q2: Simplified FDMA versus TDMA resource-use simulation for mobile traffic."""
import numpy as np

SEED = 22
SLOTS = 5000
FDMA_CAPACITY = 80
TDMA_USABLE_SLOTS = 72  # 80 nominal slots minus 10% time/control overhead


def workload(name, rng):
    if name == "Continuous voice":
        return np.full((SLOTS, 40), True, dtype=bool)
    if name == "Bursty data (10% duty)":
        return rng.random((SLOTS, 100)) < 0.10
    voice = np.full((SLOTS, 28), True, dtype=bool)
    data = rng.random((SLOTS, 30)) < 0.10
    return np.concatenate([voice, data], axis=1)


def evaluate(active):
    demand = active.sum(axis=1)
    fdma_served = np.minimum(demand, FDMA_CAPACITY)
    tdma_served = np.minimum(demand, TDMA_USABLE_SLOTS)
    return {
        "demand": int(demand.sum()), "peak": int(demand.max()),
        "fdma_util": 100 * fdma_served.sum() / (SLOTS * FDMA_CAPACITY),
        "fdma_blocked": int((demand - fdma_served).sum()),
        "tdma_util": 100 * tdma_served.sum() / (SLOTS * TDMA_USABLE_SLOTS),
        "tdma_blocked": int((demand - tdma_served).sum()),
    }


def main():
    rng = np.random.default_rng(SEED)
    print("Q2 — SHARING THE CHANNEL: FDMA VS TDMA")
    print("FDMA: 2,000/25 = 80 channels; payload-equivalent = 80×21 = 1,680 kHz.")
    print("TDMA: 10 carriers×8 slots = 80; after 10% overhead = 72 usable slots.")
    print("Simulation: 5,000 intervals; ideal work-conserving TDMA scheduling.")
    print("Workload                    Demand    Peak  FDMA util  FDMA blocked  TDMA util  TDMA blocked")
    for name in ("Continuous voice", "Bursty data (10% duty)", "Mixed 70/30"):
        r = evaluate(workload(name, rng))
        print(f"{name:<27} {r['demand']:>7} {r['peak']:>7} {r['fdma_util']:>9.2f}%"
              f" {r['fdma_blocked']:>12} {r['tdma_util']:>9.2f}% {r['tdma_blocked']:>13}")
    print("Interpretation: bursty traffic leaves dedicated capacity idle; TDMA schedules active bursts.")
    print("Evidence: simplified resource-interval teaching model, not a GSM conformance simulator.")


if __name__ == "__main__":
    main()
