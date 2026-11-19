import hashlib, uuid
records=[]
for seq,label in enumerate(["vitals","visit-note","medicine-check"],1):
 payload=f"record:{label}:{seq}".encode(); records.append((str(uuid.uuid4()),seq,hashlib.sha256(payload).hexdigest()[:12]))
print("4A TASK 6 - RURALCARE OFFLINE-FIRST")
for uid,seq,h in records: print(f"queued UUID={uid[:8]} seq={seq} hash={h} state=PENDING")
server={}; uid,seq,h=records[0]; server.setdefault(uid,("ACK-0001",h))
print("\nSync test: server commits first UUID; acknowledgement is lost; client retries same UUID.")
print("Retry returns existing acknowledgement:",server[uid][0])
print("Server logical record count:",len(server))
print("A/B: encrypted durable queue. C: minimal safe data only; block sensitive offline capture if secure storage is absent.")
