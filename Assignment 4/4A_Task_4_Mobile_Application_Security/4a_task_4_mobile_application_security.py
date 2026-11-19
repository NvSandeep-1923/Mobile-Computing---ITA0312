items=[("Request all permissions up front","Request dangerous permission in context; least privilege"),("Token in shared readable file","Use app-private encrypted storage and Keystore-backed key"),("Updates from any source","Verify trusted distribution and package signing identity"),("Plain HTTP","Enforce HTTPS/TLS, validate certificate, disable cleartext")]
print("4A TASK 4 - SECURITY DEFECTS AND REPAIRS")
for i,(a,b) in enumerate(items,1): print(f"{i}. {a}\n   Repair: {b}")
print("\nREGRESSION: request contacts only when user selects contact feature.")
print("Denied permission must not block unrelated note creation.")
print("Confidentiality first fails when malicious app reads the shared token file.")
print("No exploit is executed; this is a safe local audit model.")
