r=[("Android ART","DEX","interpretation + JIT + profile-guided AOT","managed heap / GC"),("iOS","signed Mach-O","native compiled code","ARC reference counting"),("Windows",".NET assembly or PE","CLR JIT or native code","CLR GC / native ownership")]
print("4A TASK 3 - RUNTIME MODELS")
for p,f,e,m in r: print(f"{p}: {f}; {e}; {m}")
print("\nANDROID COLD START")
for i,s in enumerate(["Launcher requests Activity","ActivityTaskManager resolves component","Zygote forks isolated process","ART maps/verifies DEX and initialises heap","Application object is created","Activity lifecycle callback runs","UI layout and rendering occur","First frame is displayed"],1): print(f"{i}. {s}")
print("Warm start can reuse a live process; a killed process requires process initialisation.")
print("Interpretation executes bytecode; JIT compiles at runtime; AOT compiles before execution.")
