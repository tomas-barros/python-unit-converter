'''
    Ready convertions:
        FROM METERS:
            * mts -> km
            * mts -> cm
        FROM KILOMETERS:
            * km -> mts
            * km -> cm
        FROM CENTIMETERS:
            * cm -> mt
            * cm -> km
            * cm -> in
        FROM INCHES:
            * in -> cm
            * in -> mt
'''

# convert units

# to meters

# km_to_mts(kilometers) (ex: mts_to_km(2.3) returns: 2300.0)
def km_to_mts(kilometers):
    meters = kilometers * 1000
    return meters

# cm_to_meters(cms) (ex: cm_to_meters(230) returns: 2.3)
def cm_to_meters(cms):
    meters = cms / 100
    return meters

# mts_to_km(meters) (ex: mts_to_km(1000) returns: 1.0)
def mts_to_km(meters):
    kilometers = meters / 1000
    return kilometers

def inches_to_meters(inch):
    meters = inch * 39.37
    return meters

# to centimeters

# km_to_cms(km) (ex: km_to_cms(2) returns 200000)
def km_to_cms(km):
    cms = km * 100000
    return cms

# meters_to_cms(meters) (ex: meters_to_cms(2.3) returns: 229.9 (2.3))
def meters_to_cms(meters):
    cms = meters * 100
    return cms

# inch_to_cms(ex: inch_to_cms(2) returns 5.08)
def inch_to_cms(inch):
    cms = inch * 2.54
    return cms

# to kilometers

# cms_to_kilometers(cms) (ex: cms_to_kilometers(300000) returns 3.0)
def cms_to_kilometers(cms):
    kilometers = cms / 100000
    return kilometers





# cms_to_inches(cms) (ex: cms_to_inches(5.08) returns 2.0)
def cms_to_inches(cms):
    inches = cms / 2.54
    return inches

print(f'{inches_to_meters(78.74)}')