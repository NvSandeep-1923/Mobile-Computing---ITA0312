items=[("DVFS / heterogeneous cores","CPU utilisation and thermal state","frequency/voltage and scheduler load","lower dynamic power; task may take longer"),("Doze / App Standby","screen off, stationary, unplugged","motion, screen, charging and usage bucket","defer jobs/network to maintenance windows"),("Application batching","non-urgent samples or uploads","queue size, deadline and battery","fewer wakeups/radio activations"),("Short wakelock","bounded critical operation","acquire/release lifecycle","temporary wake; long locks drain battery")]
print("4B TASK 5 - POWER MANAGEMENT")
for n,t,s,e in items: print(f"{n}\n  Trigger: {t}\n  State: {s}\n  Effect: {e}")
print("\nSTRESS: low battery + intermittent network")
print("Increase sample interval, batch uploads, use bounded retry/backoff, preserve emergency override.")
print("Energy estimates require device-current/voltage or profiler evidence; no physical measurement is fabricated.")
