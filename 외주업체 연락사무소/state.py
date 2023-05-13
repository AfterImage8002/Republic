states = ['AK0', 'AL0', 'AR0', 'AZ0', 'CA0', 'CO0', 'CT0', 'DE0', 'FL0', 'GA0', 'HI0', 'IA0', 'ID0', 'IL0', 'IN0', 'KS0', 'KY0', 'LA0', 'MA0', 'MD0', 'ME0', 'MI0', 'MN0', 'MO0', 'MS0', 'MT0', 'NC0', 'ND0', 'NE0', 'NH0', 'NJ0', 'NM0', 'NV0', 'NY0', 'OH0', 'OK0', 'OR0', 'PA0', 'RI0', 'SC0', 'SD0', 'TN0', 'TX0', 'UT0', 'VA0', 'VT0', 'WA0', 'WI0', 'WV0', 'WY0']

for i, state in enumerate(states):
    state_tag = f"{state} = {{\n    color = rgb {{ 20 133 237 }}\n    color_ui = rgb {{ 87 160 255 }}\n}}"
    print(f"#{i}:\n {state_tag}")
