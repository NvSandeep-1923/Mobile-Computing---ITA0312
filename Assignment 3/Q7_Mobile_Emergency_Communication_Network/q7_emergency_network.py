"""Q7: Small emergency ad hoc network routing simulation using AODV-style discovery."""
from collections import deque
from pathlib import Path

OUT = Path(__file__).with_name('output')
OUT.mkdir(exist_ok=True)

graph = {
    'Ambulance': ['Rescue-1', 'Police'],
    'Rescue-1': ['Ambulance', 'Gateway'],
    'Police': ['Ambulance', 'Rescue-2'],
    'Rescue-2': ['Police', 'Gateway'],
    'Gateway': ['Rescue-1', 'Rescue-2', 'Hospital'],
    'Hospital': ['Gateway'],
}

def discover_route(source, destination, network):
    queue = deque([(source, [source])])
    visited = {source}
    while queue:
        node, path = queue.popleft()
        if node == destination:
            return path
        for neighbor in network.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

print('Q7 - Emergency Ad Hoc Network / AODV-Style Route Discovery')
for source, destination in [('Ambulance', 'Hospital'), ('Police', 'Hospital')]:
    path = discover_route(source, destination, graph)
    print(f'{source} -> {destination}: ' +
          (' -> '.join(path) if path else 'ROUTE_NOT_FOUND'))

print('\n[Link failure test] Gateway <-> Rescue-1 link fails')
failed = {k: [n for n in v if not ({k, n} == {'Gateway', 'Rescue-1'})]
          for k, v in graph.items()}
path = discover_route('Ambulance', 'Hospital', failed)
print('Ambulance -> Hospital after failure: ' +
      (' -> '.join(path) if path else 'ROUTE_NOT_FOUND'))
print('Result: alternate path selected when one path is unavailable.')
print('Note: Illustrative graph simulation, not a packet-level ns-3/OMNeT++ experiment.')
(OUT / 'emergency_route_trace.txt').write_text(
    'Alternate path after link failure: ' + (' -> '.join(path) if path else 'ROUTE_NOT_FOUND') + '\n')
