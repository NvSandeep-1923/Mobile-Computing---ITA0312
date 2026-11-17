"""Q1: Immediate transmission versus store-and-forward for a mobile meter-reading tablet.
Teaching simulation based on Assignment 2 CO2. Uses a fixed seed and stated assumptions.
"""
import numpy as np

SEED = 16
N_UPDATES = 1000
AVAILABILITIES = (0.90, 0.60, 0.30)


def simulate(availability: float, n_updates: int = N_UPDATES):
    rng = np.random.default_rng(SEED + int(availability * 100))
    link_up = rng.random(n_updates) < availability
    immediate_delivered = int(link_up.sum())
    immediate_lost = n_updates - immediate_delivered
    # One update is created each interval; all queued updates flush when link returns.
    pending_times, queue_delays, queue_delivered = [], [], 0
    for t, up in enumerate(link_up):
        pending_times.append(t)
        if up:
            queue_delivered += len(pending_times)
            queue_delays.extend(t - created for created in pending_times)
            pending_times.clear()
    pending = len(pending_times)
    avg_delay = float(np.mean(queue_delays)) if queue_delays else float("nan")
    return immediate_delivered, immediate_lost, queue_delivered, pending, avg_delay


def main():
    print("Q1 — MOBILE COMMUNICATION OR MOBILE COMPUTING?")
    print("Model: 1,000 updates; one update per interval; link-up probability varies.")
    print("Queue assumption: all pending updates flush when the link returns (no rate cap).")
    print("Availability | Immediate OK | Immediate lost | Queue delivered | Pending | Avg delay")
    for p in AVAILABILITIES:
        a, b, c, d, e = simulate(p)
        print(f"{p:>11.0%} | {a:>12d} | {b:>14d} | {c:>14d} | {d:>7d} | {e:>9.2f}")
    print("Conclusion: store-and-forward preserves failed updates, at the cost of delivery delay.")
    print("Evidence: seeded teaching simulation, not a field measurement.")


if __name__ == "__main__":
    main()
