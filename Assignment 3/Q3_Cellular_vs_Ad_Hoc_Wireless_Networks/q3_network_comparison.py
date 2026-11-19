"""Q3: Compare cellular and ad hoc wireless network characteristics."""
from pathlib import Path
OUT = Path(__file__).with_name('output')
OUT.mkdir(exist_ok=True)
rows = [
    ('Infrastructure', 'Required (base stations)', 'Not required'),
    ('Communication', 'Through base stations', 'Direct or multi-hop'),
    ('Routing', 'Infrastructure-assisted', 'Distributed routing'),
    ('Mobility', 'Handoff between cells', 'Dynamic topology / route changes'),
    ('Topology', 'Planned cells', 'Frequently changing'),
    ('Scalability', 'Generally high', 'Depends on network size'),
    ('Failure handling', 'Alternative infrastructure', 'Other nodes / alternate paths'),
    ('Applications', 'Public mobile service', 'Disaster / field networks'),
]
print('Q3 - Cellular vs Ad Hoc Wireless Networks')
print(f"{'Parameter':<20} | {'Cellular':<29} | Ad Hoc")
print('-' * 90)
for a,b,c in rows:
    print(f'{a:<20} | {b:<29} | {c}')
print('\nDecision: Use an ad hoc network when fixed infrastructure is unavailable.')
print('Note: Qualitative comparison based on the assignment answer, not a performance benchmark.')
with (OUT/'network_comparison.csv').open('w') as f:
    f.write('Parameter,Cellular Network,Ad Hoc Network\n')
    for a,b,c in rows: f.write(f'"{a}","{b}","{c}"\n')
