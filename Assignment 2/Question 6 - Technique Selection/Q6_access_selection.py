"""Q6: Use the overall rating matrix printed in Assignment 2.
The source gives criterion weights but not criterion-by-technique ratings, so no
weighted score or sensitivity result is fabricated.
"""
import numpy as np

TECHNIQUES = ("SDMA", "TDMA", "FDMA", "CDMA", "OFDMA")
RATINGS = {
    "Wide-area cellular voice": [3, 4, 4, 4, 4],
    "Jam-resistant tactical link": [2, 2, 2, 5, 3],
    "High-rate stadium downlink": [4, 2, 2, 3, 5],
    "5,000 low-rate sensors": [2, 4, 2, 4, 3],
}
CRITERION_WEIGHTS = {
    "Spectral efficiency": 0.25, "Burst handling": 0.20,
    "Interference robustness": 0.20, "Mobility / scalability": 0.20,
    "Low complexity": 0.15,
}


def main():
    matrix = np.array(list(RATINGS.values()), dtype=float)
    print("Q6 — CHOOSING MULTIPLE-ACCESS TECHNIQUES")
    print("Criterion weights stated in the report:")
    for name, weight in CRITERION_WEIGHTS.items():
        print(f"  {name:<30} {weight:.0%}")
    print("Overall ratings supplied in the report (1=poor, 5=excellent):")
    print("Deployment                       " + "  ".join(f"{t:>6}" for t in TECHNIQUES))
    for deployment, scores in RATINGS.items():
        print(f"{deployment:<32}" + "  ".join(f"{v:>6}" for v in scores))
    print("Highest-rated technique in each deployment:")
    for deployment, scores in RATINGS.items():
        best = max(scores)
        winners = [TECHNIQUES[i] for i, value in enumerate(scores) if value == best]
        print(f"  {deployment}: {', '.join(winners)} (rating {best}/5)")
    means = matrix.mean(axis=0)
    print("Unweighted mean across four scenarios (descriptive only):")
    print("  " + ", ".join(f"{t}={s:.2f}" for t, s in zip(TECHNIQUES, means)))
    print("LIMITATION: criterion-specific ratings are absent from the supplied report.")
    print("A valid weighted sum and ±20% criterion-weight sensitivity test cannot be computed.")


if __name__ == "__main__":
    main()
