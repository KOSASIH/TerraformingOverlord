def analyze_atmospheric_composition(atmospheric_data):
    # Extract atmospheric components and temperature from input data
    gas_concentrations = atmospheric_data['gas_concentrations']
    temperature = atmospheric_data['temperature']

    # Calculate total gas concentration
    total_concentration = sum(gas_concentrations.values())

    # Determine the suitability for human habitation based on gas concentrations and temperature
    suitability = ''
    if total_concentration > 0.8:
        suitability = 'Unsuitable for human habitation due to high gas concentrations.'
    elif total_concentration < 0.2:
        suitability = 'Unsuitable for human habitation due to low gas concentrations.'
    elif temperature < -50 or temperature > 50:
        suitability = 'Unsuitable for human habitation due to extreme temperature.'

    # Generate markdown code for the analysis
    markdown_code = f"""
    ## Atmospheric Analysis

    ### Gas Concentrations
    | Gas           | Concentration |
    |---------------|---------------|
    {"".join([f"| {gas:<14} | {concentration:<13.2f} |\n" for gas, concentration in gas_concentrations.items()])}

    ### Temperature
    - Average Temperature: {temperature:.2f}°C

    ### Suitability for Human Habitation
    {suitability}
    """

    return markdown_code
