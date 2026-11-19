layers=[("Hardware","CPU, RAM, modem, sensors"),("Linux kernel/drivers","scheduler, memory, network, drivers, Binder"),("HAL","vendor hardware interfaces"),("Native libraries/services","graphics, media, SQLite, TLS, system services"),("ART","DEX verification, interpreter, JIT/AOT, heap/GC"),("Application framework","Activity, Service, permissions, notifications"),("Applications","UI, business logic, data, network")]
print("4A TASK 1 - ANDROID ARCHITECTURE")
for i,(n,d) in enumerate(layers,1): print(f"{i}. {n}: {d}")
print("\nCALL TRACE")
for s in ["App calls framework API","Framework calls service through Binder","Service checks caller identity and permissions","Service accesses HAL/native library or kernel interface","Kernel validates access and controls hardware"]: print(" -> "+s)
print("Security: UID isolation, SELinux and framework permission checks.")
print("Power: PowerManager coordinated with wakelocks, suspend and CPU frequency controls.")
