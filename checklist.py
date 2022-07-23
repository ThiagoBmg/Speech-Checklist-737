PREFLIGHT = [
    {"item": "Preflight Checklist", "value": None},
    {"item": "Oxygen", "value": "Tested, 100%"},
    {"item": "Instrument Xfer & Display Switches", "value": "Normal, Auto"},
    {"item": "Window Heat", "value": "On"},
    {"item": "Pressurization Mode Selector", "value": "Auto"},
    {"item": "Flight Instruments", "value": "set"},
    {"item": "Parking Brake", "value": "set"},
    {"item": "Engine Start Levers", "value": "cutoff"},
    {"item": "Preflight Checklist is completed", "value": None},
]

BEFORE_START = [
    {"item": "Before Start Checklist", "value": None},
    {"item": "Flight Deck Door", "value": "Closed & locked"},
    {"item": "Fuel", "value": "Pumps On"},
    {"item": "Passenger Signs", "value": "On"},
    {"item": "Windows", "value": "Locked"},
    {"item": "MCP", "value": "Set"},
    {"item": "Takeoff speeds", "value": "Set"},
    {"item": "CDU Preflight", "value": "Completed"},
    {"item": "Rudder & Aileron Trim", "value": "Free & Zero"},
    {"item": "Taxi & Takeoff Briefing", "value": "Completed"},
    {"item": "Anti Collision Lights", "value": "On"},
    {"item": "Before Start Checklist is completed", "value": None},
]

BEFORE_TAXI = [
    {"item": "Before Taxi Checklist", "value": None},
    {"item": "Generators", "value": "On"},
    {"item": "Probe Heat", "value": "On"},
    {"item": "Anti-ice", "value": None},
    {"item": "Isolation Valves", "value": "Auto"},
    {"item": "Engine Start Switches", "value": "Continuous"},
    {"item": "Recall", "value": "Checked"},
    {"item": "Autobrake", "value": "RTO"},
    {"item": "Engine Start Levers", "value": "Idle Detent"},
    {"item": "Flight Controls", "value": "Checked"},
    {"item": "Ground Equipment", "value": "Clear"},
    {"item": "Before Taxi Checklist is completed", "value": None},
]


BEFORE_TAKEOFF = [
    {"item": "Before Takeoff Checklist", "value": None},
    {"item": "Flaps", "value": "Green light"},
    {"item": "Stabilizer Trim", "value": "Units"},
    {"item": "Before Takeoff Checklist is completed", "value": None},
]

AFTER_TAKEOFF = [
    {"item": "After Takeoff Checklist", "value": None},
    {"item": "Engine Bleeds", "value": "On"},
    {"item": "Packs", "value": "Auto"},
    {"item": "Landing Gear", "value": "Up & Off"},
    {"item": "Flaps", "value": "Up, No lights"},
    {"item": "After Takeoff Checklist is completed", "value": None},
]

DESCENT = [
    {"item": "Descent Checklist", "value": None},
    {"item": "Pressurization", "value": "Landing Altitude Set"},
    {"item": "Recall", "value": "Checked"},
    {"item": "Autobrake", "value": None},
    {"item": "Landing Data", "value": " Vref and Minimums set"},
    {"item": "Approach Briefing", "value": "Completed"},
    {"item": "Descent Checklist is completed", "value": None},
]


APPROACH = [
    {"item": "Approach Checklist", "value": None},
    {"item": "Altimeters", "value": "Set"},
    {"item": "Approach Checklist is completed", "value": None},
]

LANDING = [
    {"item": "Landing Checklist", "value": None},
    {"item": "Engine Start Switches", "value": "Continuous"},
    {"item": "Speed Brake", "value": "Armed"},
    {"item": "Landing Gear", "value": "Down"},
    {"item": "Flaps", "value": "Green Light"},
    {"item": "Landing Checklist is completed", "value": None},
]

SHUTDOWN = [
    {"item": "Shutdown Checklist", "value": None},
    {"item": "Fuel Pumps", "value": "Off"},
    {"item": "Probe Heat", "value": "Off"},
    {"item": "Hydraulic Panel", "value": "Set"},
    {"item": "Flaps", "value": "Up"},
    {"item": "Parking Brake", "value": None},
    {"item": "Engine Start Levers", "value": "Cutoff"},
    {"item": "Weather Radar", "value": "Off"},
    {"item": "Securing Aircraft is completed", "value": None},
]

SECURING_AIRCRAFT = [
    {"item": "Shutdown Checklist", "value": None},
    {"item": "IRS's", "value": "Off"},
    {"item": "Emergent Exit Lights", "value": "Off"},
    {"item": "Window Heat", "value": "Off"},
    {"item": "Packs", "value": "Off"},
    {"item": "Securing Aircraft is completed", "value": None},
]

FALLBACK_MESSAGE = [
    {"item": "Sorry, try again", "value": None}
]
