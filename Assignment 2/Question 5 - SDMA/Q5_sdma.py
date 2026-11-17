"""Q5: Half-wavelength uniform linear array factor and angular SIR separation."""
import numpy as np

ELEMENTS = (2, 4, 8, 16)
SEPARATIONS = np.arange(5.0, 60.1, 1.0)
SIR_THRESHOLD_DB = 10.0


def array_factor(n_elements, theta_deg, steering_deg=0.0):
    theta = np.radians(theta_deg)
    steer = np.radians(steering_deg)
    psi = np.pi * (np.sin(theta) - np.sin(steer))
    den = np.sin(psi / 2)
    num = np.sin(n_elements * psi / 2)
    out = np.ones_like(np.asarray(psi, dtype=float))
    mask = np.abs(den) > 1e-12
    out[mask] = num[mask] / (n_elements * den[mask])
    return out


def main():
    print("Q5 — SDMA: SAME CHANNEL IN DIFFERENT DIRECTIONS")
    print("Uniform linear array; d=lambda/2; broadside steering; ideal far-field model.")
    print("Elements | Approx. HPBW (deg) | First sampled separation meeting 10 dB SIR")
    hpbw_values = {2: 101.6, 4: 50.8, 8: 25.4, 16: 12.7}
    for n in ELEMENTS:
        sir_values = []
        for delta in SEPARATIONS:
            amp = abs(float(array_factor(n, np.array([delta]))[0]))
            sir_values.append(-20 * np.log10(max(amp, 1e-12)))
        good = np.where(np.array(sir_values) >= SIR_THRESHOLD_DB)[0]
        separation = f"{SEPARATIONS[good[0]]:.0f}" if good.size else "not found"
        print(f"{n:>8} | {hpbw_values[n]:>18.1f} | {separation}")
    print("Toll-plaza decision: combine SDMA with time/frequency/code scheduling for clustered vehicles.")
    print("Evidence: ideal array-factor calculation, not a measured antenna pattern.")


if __name__ == "__main__":
    main()
