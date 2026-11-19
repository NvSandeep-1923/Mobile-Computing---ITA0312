"""Q4: Worked Mobile IP flow for a mobile healthcare application."""
from pathlib import Path
OUT = Path(__file__).with_name('output')
OUT.mkdir(exist_ok=True)
mobile_node = 'Doctor-Tablet'
home = '10.20.0.25'
visits = [('Hospital-Ward', '172.20.1.25'), ('Ambulance-Network', '172.30.1.25'), ('Emergency-Ward', '192.168.5.25')]
print('Q4 - Mobile Healthcare / Mobile IP Communication Flow')
print(f'Mobile node: {mobile_node} | Home address: {home}')
print('Correspondent node: Hospital Patient-Record Server')
for location, coa in visits:
    print(f'\nLocation: {location}')
    print(f'  Obtain Care-of Address: {coa}')
    print('  Register new location with Home Agent')
    print(f'  Home Agent binding: {home} -> {coa}')
    print('  Secure request for patient record -> tunnel/route -> tablet')
print('\nRequirements: low delay, reliable delivery, authentication, privacy and efficient handoff.')
print('Note: Workflow demonstration only; no patient data or live network is used.')
(OUT/'healthcare_flow.txt').write_text(f'{mobile_node} home address: {home}\nVisited access points: {len(visits)}\nFinal CoA: {visits[-1][1]}\n')
