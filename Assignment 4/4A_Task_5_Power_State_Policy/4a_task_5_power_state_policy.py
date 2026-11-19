states=[("ACTIVE","user interaction / urgent event","idle timeout","foreground UI and bounded work"),("IDLE","screen off, no interaction","input / alarm / eligible job","system tasks and batched sampling"),("SUSPENDED_DOZE","stationary, unplugged, screen off","motion / user / maintenance window","restricted wake events and permitted jobs"),("CHARGING_MAINTENANCE","power connected","unplug / thermal policy change","batch upload, backup, indexing")]
print("4A TASK 5 - POWER STATES")
for n,a,b,w in states: print(f"{n}\n  Entry: {a}\n  Exit: {b}\n  Allowed: {w}")
print("\nBATTERY SAVER AT 15%")
print("Kernel: lower frequency/voltage and limit wakeups.")
print("Runtime: defer nonessential compilation and maintenance.")
print("App: batch uploads, reduce stationary sampling, defer non-urgent work.")
print("Preserve urgent alerts and disclose reduced precision.")
