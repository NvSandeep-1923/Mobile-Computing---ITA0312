"""Q5: DSDV-style routing-table update using destination sequence numbers."""
from pathlib import Path
OUT = Path(__file__).with_name('output')
OUT.mkdir(exist_ok=True)
routes = {'D': {'next_hop': 'B', 'hops': 3, 'seq': 10}}

def update(destination, next_hop, hops, seq):
    old = routes.get(destination)
    if old is None or seq > old['seq'] or (seq == old['seq'] and hops < old['hops']):
        routes[destination] = {'next_hop': next_hop, 'hops': hops, 'seq': seq}
        return 'UPDATED'
    return 'IGNORED (older sequence or longer route)'

print('Q5 - DSDV Proactive Routing Table Updates')
print('Initial table:', routes)
for advertiser, dest, next_hop, hops, seq in [
    ('C', 'D', 'A', 2, 12),
    ('B', 'D', 'C', 1, 12),
    ('E', 'D', 'E', 4, 8),
]:
    result = update(dest, next_hop, hops, seq)
    print(f'Node {advertiser} advertises route to {dest} via {next_hop}, hops={hops}, seq={seq}: {result}')
print('\nFinal routing table:')
for dest, route in routes.items():
    print(f"Destination {dest}: next hop={route['next_hop']}, hops={route['hops']}, sequence={route['seq']}")
print('Note: Small DSDV-style logic demonstration, not a full protocol simulator.')
(OUT / 'dsdv_route_table.txt').write_text(str(routes) + '\n')
