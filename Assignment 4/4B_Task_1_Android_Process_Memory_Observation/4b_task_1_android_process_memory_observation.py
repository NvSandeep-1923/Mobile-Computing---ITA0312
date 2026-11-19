import os,platform
print("4B TASK 1 - PROCESS/MEMORY OBSERVATION TEMPLATE")
print("Host OS:",platform.platform()," PID:",os.getpid())
print("Note: host PID is not Android PID/UID/PSS evidence.")
for condition,event,state in [("Foreground","onResume","low kill priority"),("Background 5 min","onStop / cached","may be trimmed"),("Low-memory trim","onTrimMemory may occur","process may be killed")]: print(f"{condition}: {event}; {state}")
print("\nRUN ON ANDROID DEVICE:")
for c in ["adb shell getprop ro.build.version.release","adb shell ps -A","adb shell dumpsys activity processes","adb shell dumpsys meminfo <package.name>","adb shell service list","adb shell cat /proc/<pid>/status","adb logcat -d | grep -E 'ActivityTaskManager|am_|GC|lifecycle'"]: print(c)
