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

# to meters, returns from unit to meters

def km_to_mts(kilometers):
    meters = kilometers * 1000
    return meters

def cm_to_meters(cms):
    meters = cms / 100
    return meters

def mts_to_km(meters):
    kilometers = meters / 1000
    return kilometers

def inches_to_meters(inch):
    meters = inch * 39.37
    return meters

# to centimeters, returns from unit to centimeters

def km_to_cms(km):
    cms = km * 100000
    return cms

def meters_to_cms(meters):
    cms = meters * 100
    return cms

def inch_to_cms(inch):
    cms = inch * 2.54
    return cms

# to kilometers, returns from unit to kilometers

def cms_to_kilometers(cms):
    kilometers = cms / 100000
    return kilometers

# to inches, returns from unit to inches

def cms_to_inches(cms):
    inches = cms / 2.54
    return inches