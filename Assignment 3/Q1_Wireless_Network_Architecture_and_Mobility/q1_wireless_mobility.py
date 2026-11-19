"""Q1: Wireless mobility and handoff simulation (illustrative discrete events)."""
import csv
from pathlib import Path

OUT = Path(__file__).with_name('output')
OUT.mkdir(exist_ok=True)

# A mobile device sends 20 packets while moving from AP-A toward AP-B.
# Packet loss and interruption grow with the selected mobility scenario.
scenarios = [('Low', 1, 0), ('Medium', 3, 2), ('High', 5, 5)]
rows = []
for mobility, delay_ms, lost in scenarios:
    sent = 20
    delivered = sent - lost
    rows.append((mobility, sent, delivered, lost,
                 round(delivered / sent * 100, 1), delay_ms * 10))

csv_path = OUT / 'mobility_results.csv'
with csv_path.open('w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Mobility', 'Packets Sent', 'Packets Delivered', 'Packets Lost',
                'Delivery Ratio (%)', 'Illustrative Handoff Delay (ms)'])
    w.writerows(rows)

print('Q1 - Wireless Mobility / Handoff Simulation')
print('Scenario | Sent | Delivered | Lost | PDR | Handoff delay')
for mobility, sent, delivered, lost, pdr, delay in rows:
    print(f'{mobility:8} | {sent:4} | {delivered:9} | {lost:4} | {pdr:5.1f}% | {delay:6} ms')
print(f'\nCSV saved: {csv_path.name}')
print('Note: Parameters are illustrative, not measured from a physical wireless network.')
