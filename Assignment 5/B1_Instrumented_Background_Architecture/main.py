from dataclasses import dataclass
import json

@dataclass
class Item:
    ident:str; arr:int; priority:int; sensitive:bool=True; encrypted:bool=True; done:bool=False; attempts:int=0

def environment(s,t):
    if s=='GOOD': return {'bat':80,'net':'good','doze':False,'perm':True}
    if s=='DOZE': return {'bat':max(8,60-4*t),'net':'poor' if t%3 else 'good','doze':t>=5,'perm':True}
    return {'bat':70,'net':'good','doze':False,'perm':t<1}

def feasible(it,e,t):
    if not e['perm'] or (it.sensitive and not it.encrypted): return False
    if e['bat'] < (5 if it.priority==0 else 20): return False
    if e['net']=='none' or (e['net']=='poor' and it.priority!=0): return False
    if e['doze'] and it.priority!=0 and t%5!=0: return False
    return True

def simulate(scenario,policy,K=3,T=20):
    items=[Item(f'W{i+1:02}',0,i%3) for i in range(12)]
    stats={'enqueued':0,'deferred':0,'cancelled':0,'success':0,'peak_workers':0,'critical_delay':[]}
    delivered=set()
    for t in range(T):
        e=environment(scenario,t)
        pending=[i for i in items if not i.done and i.ident not in delivered]
        if not e['perm']:
            stats['cancelled']+=len(pending); break
        order=pending if policy=='FIFO' else sorted(pending,key=lambda i:(i.priority,i.arr,i.ident))
        slots=K; running=0
        for it in order:
            if slots<=0: break
            if feasible(it,e,t):
                slots-=1; running+=1; stats['enqueued']+=1; stats['success']+=1; it.done=True; delivered.add(it.ident)
                if it.priority==0: stats['critical_delay'].append(t-it.arr)
            else:
                stats['deferred']+=1
                if policy=='FIFO': slots-=1
        stats['peak_workers']=max(stats['peak_workers'],running)
        if len(delivered)+stats['cancelled']==len(items): break
    stats['backlog']=len(items)-len(delivered)-stats['cancelled']
    return stats

if __name__=='__main__':
 print('B1 - Instrumented Background Scheduler')
 for s in ['GOOD','DOZE','PERMISSION_REVOKED']:
  print('Scenario:',s)
  for p in ['FIFO','PRIORITY']:
   v=simulate(s,p); print(p,json.dumps(v,sort_keys=True))
 print('Priority rule: priority ascending (0=critical), then arrival/ID; infeasible priority items are skipped without blocking later candidates.')
 print('Model scope: WorkManager-style scheduler simulation, not a real Android Service execution.')
