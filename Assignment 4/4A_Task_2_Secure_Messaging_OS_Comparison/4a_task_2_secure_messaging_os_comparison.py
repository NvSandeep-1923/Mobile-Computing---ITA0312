platforms={"Android":("FCM/system push","Doze and background limits"),"iOS":("APNs/system push","Background App Refresh and notification type"),"Windows":("Push notification service","package and OS background task policy")}
print("4A TASK 2 - SECURE MESSAGING")
for p,(push,policy) in platforms.items(): print(f"{p}: {push}; {policy}")
print("\nSCREEN-OFF TRACE")
for i,s in enumerate(["Network stack receives packet","System push service receives notification","OS checks payload type and background policy","Eligible callback or visible notification is dispatched","App stores encrypted message metadata","User opens notification and fetches authenticated content"],1): print(f"{i}. {s}")
print("\nKILLED PROCESS: visible push may still display; silent callback is not guaranteed.")
print("Use server-side durable queue, authenticated fetch and idempotent processing.")
