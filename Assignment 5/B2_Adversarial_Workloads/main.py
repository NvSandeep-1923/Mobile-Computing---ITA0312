from dataclasses import dataclass

@dataclass
class Record:
    id:int; arrival:int; priority:int=2; complete:bool=False

def env_a(t): return {'battery':70,'network':'good','doze':False}
def env_b(t): return {'battery':70 if t%8<3 else 15,'network':'good' if t%8<3 else 'poor','doze':t%8>=3}

def run(workload,n=40,ticks=200):
    pending=[Record(i,i%ticks,0 if i%10==0 else 2) for i in range(n)]
    deferred=success=processed=0; history=[]
    for t in range(ticks):
        e=(env_a if workload=='A' else env_b)(t)
        ready=[x for x in pending if not x.complete and x.arrival<=t]
        ready.sort(key=lambda x:(x.priority,x.arrival,x.id))
        slots=3; ran=0; defer_now=0
        for x in ready:
            if slots==0: break
            allowed=(e['network']=='good' and e['battery']>=20 and (not e['doze'] or x.priority==0)) or x.priority==0
            if allowed:
                x.complete=True; success+=1; processed+=1; slots-=1; ran+=1
            else:
                deferred+=1; defer_now+=1
        history.append((t,e['battery'],e['network'],e['doze'],ran,defer_now))
        if success==n: break
    return {'workload':workload,'records':n,'processed':processed,'deferred_checks':deferred,'success':success,'backlog':n-success,'trace':history}

if __name__=='__main__':
 print('B2 - Same Size, Different Constraint Alignment')
 for name in ['A','B']:
  r=run(name); print(f"{name}: records={r['records']} processed={r['processed']} deferred_checks={r['deferred_checks']} successful={r['success']} backlog={r['backlog']}")
  print('first decisions (tick,battery,network,doze,executed,deferred):',r['trace'][:8])
 print('Prediction: B needs more re-evaluations because item arrivals overlap recurring low-battery/poor-network/Doze periods.')
 print('Interpretation: same record count does not imply equal effort; environment-window alignment drives retries and deferral checks.')
