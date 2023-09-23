from datetime import datetime


Condition_Choices = (
    ('USED', 'USED'),
    ('NEW', 'NEW'),
    ('COLLISION','COLLISION'),
    ('PARTS', 'PARTS'),

    )

Doors_Choices = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),

    )

Features_Choices = (
    ('Cruise Control', 'Cruise Control'),
    ('Audio Interface', 'Audio Interface'),
    ('Airbags', 'Airbags'),
    ('Air Conditioning', 'Air Conditioning'),
    ('Seat Heating', 'Seat Heating'),
    ('Alarm System', 'Alarm System'),
    ('ParkAssist', 'ParkAssist'),
    ('Power Steering', 'Power Steering'),
    ('Reversing Camera', 'Reversing Camera'),
    ('Direct Fuel Injection', 'Direct Fuel Injection'),
    ('Auto Start/Stop', 'Auto Start/Stop'),
    ('Wind Deflector', 'Wind Deflector'),
    ('Bluetooth Handset', 'Bluetooth Handset'),
    )

Transmission_Choices = (
    ('AUTOMATIC', 'AUTOMATIC'),
    ('MANUAL', 'MANUAL'),
    ('OTHER', 'OTHER'),

)


Year_Choices =[]
for r in range(1900,(datetime.now().year+1)):
    Year_Choices.append((r,r))
