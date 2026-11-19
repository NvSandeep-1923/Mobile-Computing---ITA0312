"""Q5: DSDV-style routing-table update using destination sequence numbers."""
from pathlib import Path
OUT = Path(__file__).with_name('output')
OUT.mkdir(exist_ok=True)
routes = {'D': {'next_hop':'B', 'hops':3, 'seq':10}}
def update(destination, next_hop, hops, seq):
    old = routes.get(destination)
    if old is None or seq > old['seq'] or (seq == old['seq'] and hops < old['hops']):
        routes[destination] = {'next_hop':next_hop, 'hops':hops, 'seq':seq}
        return 'UPDATED'
    return 'IGNORED (older sequence or longer route)'
print('Q5 - DSDV Proactive Routing Table Updates')
print('Initial table:', routes)
for event in [('C', 'D', 'A', 2, 12), ('D', 'D', 'C', 1, 12), ('E', 'D', 'E', 4, 8)]:
    node, dest, hop, hops, seq = event
    result = update(dest, hop, hops, seq)
    print(f'Node {node} advertises route to {dest} via {hop}, hops={hops}, seq={seq}: {result}')
print('\nFinal routing table:')
for dest, r in routes.items():
    print(f"Destination {dest}: next hop={r['next_hop']}, hops={r['hops']}, sequence={r['seq']}")
print('Note: Small DSDV-style logic demonstration, not a full protocol simulator.')
(OUT/'dsdv_route_table.txt').write_text(str(routes)+'\n')
