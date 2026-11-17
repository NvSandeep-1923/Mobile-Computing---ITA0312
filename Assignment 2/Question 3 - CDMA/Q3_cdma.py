"""Q3: Direct-sequence BPSK CDMA spreading, code correlation and near-far stress."""
import numpy as np

SEED = 33
BITS = 12000
NOISE_STD = 0.35


def hadamard(n):
    h = np.array([[1.0]])
    while h.shape[0] < n:
        h = np.block([[h, h], [h, -h]])
    return h


def ber_for_users(length, users, rng):
    codes = hadamard(length)[:users]
    bits = rng.choice([-1.0, 1.0], size=(users, BITS))
    noise = rng.normal(0.0, NOISE_STD, size=(BITS, length))
    received = np.zeros((BITS, length))
    for u in range(users):
        received += bits[u, :, None] * codes[u][None, :] / np.sqrt(length)
    received += noise
    decisions = np.sign(received @ codes[0] / np.sqrt(length))
    return int(np.count_nonzero(decisions != bits[0]))


def near_far_ber(length, power_ratio, rng):
    h = hadamard(length)
    weak_code, strong_code = h[4], h[5]
    bits = rng.choice([-1.0, 1.0], size=(2, BITS))
    strong = np.roll(strong_code, 1)  # one-chip offset leaves residual correlation
    signal = (bits[0, :, None] * weak_code[None, :]
              + np.sqrt(power_ratio) * bits[1, :, None] * strong[None, :]) / np.sqrt(length)
    signal += rng.normal(0.0, NOISE_STD, size=signal.shape)
    decisions = np.sign(signal @ weak_code / np.sqrt(length))
    return int(np.count_nonzero(decisions != bits[0]))


def main():
    rng = np.random.default_rng(SEED)
    print("Q3 — CDMA: ORTHOGONALITY, SPREADING AND NEAR-FAR")
    print("BPSK direct-sequence; 12,000 bits/user; chip-noise standard deviation = 0.35.")
    print("Length | Processing gain (dB) | K=2 BER | K=4 BER | K=8 BER")
    for length in (8, 16, 64):
        vals = [ber_for_users(length, k, rng) / BITS for k in (2, 4, 8)]
        print(f"{length:>6} | {10*np.log10(length):>20.2f} | {vals[0]:>7.5f} | {vals[1]:>7.5f} | {vals[2]:>7.5f}")
    corr = hadamard(8) @ hadamard(8).T / 8
    print(f"Walsh check: auto C0,C0={corr[0,0]:.1f}; cross C0,C1={corr[0,1]:.1f}.")
    print("Near-far: weak user plus one-chip-offset interferer (L=8):")
    for ratio in (1, 10):
        errors = near_far_ber(8, ratio, rng)
        print(f"  Interferer/desired power={ratio:>2}×: BER={errors/BITS:.5f} ({errors} errors)")
    print("Evidence: finite seeded simulation; zero errors would not prove zero true BER.")


if __name__ == "__main__":
    main()
