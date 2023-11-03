def analyze_geological_composition(geological_data):
    """
    Analyzes the geological composition of a planet or celestial body.
    
    Args:
    geological_data (dict): Input data on the geological features of the planet.
                            Contains information on rock types, mineral composition, and topography.
    
    Returns:
    str: Markdown code providing a comprehensive analysis of the planet's geological characteristics.
    """
    
    markdown_output = ""
    
    # Analyze rock types
    rock_types = geological_data.get('rock_types', [])
    if rock_types:
        markdown_output += "## Rock Types\n\n"
        for rock_type in rock_types:
            markdown_output += f"- {rock_type}\n"
        markdown_output += "\n"
    
    # Analyze mineral composition
    mineral_composition = geological_data.get('mineral_composition', {})
    if mineral_composition:
        markdown_output += "## Mineral Composition\n\n"
        for mineral, abundance in mineral_composition.items():
            markdown_output += f"- {mineral}: {abundance}\n"
        markdown_output += "\n"
    
    # Analyze topography
    topography = geological_data.get('topography', [])
    if topography:
        markdown_output += "## Topography\n\n"
        for feature in topography:
            markdown_output += f"- {feature}\n"
        markdown_output += "\n"
    
    # Analyze potential resources
    potential_resources = geological_data.get('potential_resources', [])
    if potential_resources:
        markdown_output += "## Potential Resources\n\n"
        for resource in potential_resources:
            markdown_output += f"- {resource}\n"
        markdown_output += "\n"
    
    # Analyze geological hazards
    geological_hazards = geological_data.get('geological_hazards', [])
    if geological_hazards:
        markdown_output += "## Geological Hazards\n\n"
        for hazard in geological_hazards:
            markdown_output += f"- {hazard}\n"
        markdown_output += "\n"
    
    return markdown_output
