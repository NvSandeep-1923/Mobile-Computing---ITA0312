from itertools import product

DEVICES=[
 {'id':'D1','cpu':1.0,'battery':80,'charging':False,'bandwidth':20,'wifi':True},
 {'id':'D2','cpu':0.72,'battery':55,'charging':False,'bandwidth':6,'wifi':False},
 {'id':'D3','cpu':0.45,'battery':60,'charging':False,'bandwidth':1.5,'wifi':False},
 {'id':'D4','cpu':0.9,'battery':12,'charging':False,'bandwidth':30,'wifi':True},
 {'id':'D5','cpu':0.95,'battery':65,'charging':False,'bandwidth':2,'wifi':False},
]
RES=[('480p',0.55,0.7),('720p',0.78,1.0),('1080p',1.0,1.4)]
BITRATES=[1,2.5,5]
BATTERY_J=41580

def heuristic(d):
    if d['battery']<20 and not d['charging']: res='480p'; bitrate=1; defer='charging'
    else:
        viable=[r for r in RES if r[2]/max(d['cpu'],0.1)*5.8<=6]
        res=(viable[-1][0] if viable else '480p')
        allowed=[b for b in BITRATES if b<=0.6*d['bandwidth']]
        bitrate=max(allowed) if allowed else 1
        defer='now' if d['bandwidth']>=2 and d['battery']>=20 else 'Wi-Fi'
    q=next(r[1] for r in RES if r[0]==res)
    encode=5.8*(next(r[2] for r in RES if r[0]==res))/max(d['cpu'],0.1)
    energy=3.4+q*5.5+bitrate*1.2+encode*0.65
    impact=energy/BATTERY_J*100
    return res,bitrate,round(energy,1),round(encode,1),round(impact,3),defer

def exhaustive(d):
    best=None
    for r,b in product(RES,BITRATES):
        label,q,mult=r; t=5.8*mult/max(d['cpu'],0.1); e=3.4+q*5.5+b*1.2+t*0.65
        short=max(0,1-q); c=e+0.5*t+8*short
        cand=(c,label,b,e,t)
        if best is None or cand<best: best=cand
    return best

if __name__=='__main__':
 print('B4 - Video Encoding / Upload Heuristic')
 for d in DEVICES:
  h=heuristic(d); ex=exhaustive(d)
  print(f"{d['id']}: heuristic={h[0]} {h[1]}Mbps energy={h[2]}J time={h[3]}s batteryImpact={h[4]}% upload={h[5]} | exhaustive best={ex[1]} {ex[2]}Mbps cost={ex[0]:.1f}")
 print('Challenge: D4 has 12% battery but Wi-Fi and modest clip energy; fixed low-battery rule defers and forces 480p, while exhaustive cost may select higher quality.')
 print('Production decision: heuristic offers a small constant number of comparisons, not optimality. Monitor p95 encode/upload, battery/clip, thermal throttling, success, deferral and quality complaints.')
