import math
import random

def erlang_b(channels, offered_traffic):
    b = 1.0
    for m in range(1, channels + 1):
        b = offered_traffic * b / (m + offered_traffic * b)
    return b

def traffic_at_blocking(channels, target=0.02):
    low, high = 0.0, 2.0 * channels
    for _ in range(80):
        mid = (low + high) / 2
        if erlang_b(channels, mid) > target:
            high = mid
        else:
            low = mid
    return (low + high) / 2

def valid_cluster_sizes(limit=20):
    values = set()
    for i in range(limit + 1):
        for j in range(limit + 1):
            n = i*i + i*j + j*j
            if 1 <= n <= limit:
                values.add(n)
    return sorted(values)

def reuse_distance(radius_km, n):
    return radius_km * math.sqrt(3*n)

def sir_db(cluster_size, path_loss_exp, interferers=6):
    linear = (math.sqrt(3*cluster_size)**path_loss_exp) / interferers
    return 10 * math.log10(linear)

def report():
    total_channels = 336
    radius = 0.5
    print("MOBILE COMPUTING - ASSIGNMENT 1 (CO1)")
    print("Cellular Frequency Planning Simulation")
    print("=" * 54)
    for n in [3, 4, 7, 12]:
        if total_channels % n != 0:
            continue
        ch = total_channels // n
        d = reuse_distance(radius, n)
        a = traffic_at_blocking(ch, 0.02)
        print("N =", n, "channels/cell =", ch,
              "reuse distance =", round(d, 3), "km",
              "traffic/cell =", round(a, 2), "Erlangs")
        for exponent in [2.5, 3, 4]:
            print("  path-loss n =", exponent,
                  "SIR =", round(sir_db(n, exponent), 2), "dB")
    print("Valid cluster sizes:", valid_cluster_sizes())
    print("Subscriber traffic estimates:")
    for users in [1000, 10000, 20000, 100000]:
        offered = users * 0.025
        print(users, "users ->", offered, "Erlangs")

if __name__ == "__main__":
    report()
