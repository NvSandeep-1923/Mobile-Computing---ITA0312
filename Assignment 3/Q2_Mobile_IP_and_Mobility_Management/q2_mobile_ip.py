"""Q2: Mobile IP registration, tunnelling and repeated-handoff worked example."""
from pathlib import Path

OUT = Path(__file__).with_name('output')
OUT.mkdir(exist_ok=True)

home_address = '10.0.0.7'
bindings = {}
packets = ['PKT-001', 'PKT-002', 'PKT-003']

print('Q2 - Mobile IP Worked Example')
print(f'Mobile Node home address: {home_address}')
for network, coa in [('Foreign-Network-A', '172.16.1.7'),
                     ('Foreign-Network-B', '192.168.2.7')]:
    print(f'\n[Registration] Mobile Node enters {network}')
    print(f'  Obtains Care-of Address: {coa}')
    print('  Sends registration request to Home Agent')
    bindings[home_address] = coa
    print('  Home Agent accepts registration and updates binding')
    print(f'  Binding: {home_address} -> {bindings[home_address]}')

print('\n[Packet delivery through Home Agent tunnel]')
for packet in packets:
    coa = bindings[home_address]
    print(f'  {packet}: intercept at Home Agent -> encapsulate -> tunnel to {coa} -> decapsulate -> deliver')

print('\nSummary: 2 successful registrations, 3 packets delivered via the latest Care-of Address.')
print('Note: This is a logical worked example; no real Mobile IP network is contacted.')
(OUT / 'mobile_ip_trace.txt').write_text(
    'Home address: ' + home_address + '\nFinal CoA: ' + bindings[home_address] +
    '\nPackets delivered: ' + ', '.join(packets) + '\n')
