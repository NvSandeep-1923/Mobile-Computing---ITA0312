assets=[("Auth token","shared-file extraction","private storage + Keystore key","partially blocked"),("Patient DB","file extraction","encrypted DB + protected key","partially blocked"),("API traffic","Wi-Fi interception","TLS + certificate validation","blocks passive interception"),("Exported Activity","malicious intent","not exported unless required","blocked if protected"),("App update","repackaged APK","package signing verification","blocked absent signing-key compromise"),("Location/camera","unauthorised access","runtime permission + user indicator","partially blocked")]
print("4B TASK 4 - MOBILE SECURITY AUDIT")
for a,x,c,r in assets: print(f"{a}: attack={x}; control={c}; result={r}")
print("\nWEAKENED CONTROL: allow cleartext only with local test endpoint and test data.")
print("Expected verdict changes TLS-protected -> exposed. Restore HTTPS after test.")
print("Review third-party endpoint inventory; remove/upgrade libraries sending identifiers over HTTP.")
print("No live patient traffic is inspected.")
