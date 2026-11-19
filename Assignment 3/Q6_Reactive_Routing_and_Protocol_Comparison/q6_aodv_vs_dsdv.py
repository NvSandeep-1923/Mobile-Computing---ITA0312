"""Q6: Illustrative AODV route discovery and comparison with proactive DSDV."""
from collections import deque
from pathlib import Path
OUT = Path(__file__).with_name('output')
OUT.mkdir(exist_ok=True)
graph = {'S':['A','B'], 'A':['S','D'], 'B':['S','C'], 'C':['B','D'], 'D':['A','C']}
def aodv_discovery(src, dst):
    q=deque([(src,[src])]); seen={src}; events=[f'{src} broadcasts RREQ for {dst}']
    while q:
        node,path=q.popleft()
        if node==dst:
            events.append(f'{dst} returns RREP along reverse path: ' + ' -> '.join(reversed(path)))
            return path,events
        for n in graph[node]:
            if n not in seen:
                seen.add(n); events.append(f'{node} forwards RREQ to {n}'); q.append((n,path+[n]))
    events.append('RERR: route not found')
    return None,events
print('Q6 - AODV Route Discovery (RREQ / RREP)')
path, events = aodv_discovery('S','D')
for e in events: print(e)
print('Installed route:', ' -> '.join(path) if path else 'ROUTE_NOT_FOUND')
print('\nAODV vs DSDV summary:')
print('AODV: reactive; route discovery occurs on demand; control messages follow route requests/failures.')
print('DSDV: proactive; routing tables are updated continuously; routes may be immediately available.')
print('Selection: AODV is a reasonable choice for a frequently changing network with intermittent traffic.')
print('Note: Graph-level teaching example, not a full network simulation.')
(OUT/'aodv_discovery_trace.txt').write_text('\n'.join(events)+'\n')
