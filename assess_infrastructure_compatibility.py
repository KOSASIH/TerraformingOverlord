def assess_infrastructure_compatibility(existing_infrastructure, proposed_terraforming_activities):
    """
    Assess the potential impact of terraforming on the planet's infrastructure.

    Args:
    existing_infrastructure (dict): Data on the existing infrastructure, including buildings, transportation systems, and energy sources.
    proposed_terraforming_activities (dict): Data on the proposed terraforming activities.

    Returns:
    str: Markdown code presenting an evaluation of the infrastructure compatibility and identifying necessary modifications or upgrades.

    """

    # Check compatibility of buildings
    building_compatibility = assess_building_compatibility(existing_infrastructure['buildings'], proposed_terraforming_activities['atmospheric_composition'])
    
    # Check compatibility of transportation systems
    transportation_compatibility = assess_transportation_compatibility(existing_infrastructure['transportation_systems'], proposed_terraforming_activities['surface_conditions'])
    
    # Check compatibility of energy sources
    energy_compatibility = assess_energy_compatibility(existing_infrastructure['energy_sources'], proposed_terraforming_activities['temperature_range'])

    # Generate markdown code for the evaluation
    markdown_code = f"## Infrastructure Compatibility Assessment\n\n"
    markdown_code += f"### Buildings\n\n"
    markdown_code += building_compatibility + "\n\n"
    markdown_code += f"### Transportation Systems\n\n"
    markdown_code += transportation_compatibility + "\n\n"
    markdown_code += f"### Energy Sources\n\n"
    markdown_code += energy_compatibility + "\n\n"

    return markdown_code


def assess_building_compatibility(existing_buildings, atmospheric_composition):
    """
    Assess the compatibility of existing buildings with the proposed atmospheric composition.

    Args:
    existing_buildings (list): List of existing buildings.
    atmospheric_composition (dict): Data on the proposed atmospheric composition.

    Returns:
    str: Markdown code presenting an evaluation of the building compatibility.

    """

    # Perform compatibility assessment based on the atmospheric composition
    # You can implement your own logic here based on the specific requirements of the terraforming project

    # Example implementation
    building_compatibility = ""
    for building in existing_buildings:
        building_compatibility += f"- {building}: Compatible\n"

    return building_compatibility


def assess_transportation_compatibility(existing_transportation_systems, surface_conditions):
    """
    Assess the compatibility of existing transportation systems with the proposed surface conditions.

    Args:
    existing_transportation_systems (list): List of existing transportation systems.
    surface_conditions (dict): Data on the proposed surface conditions.

    Returns:
    str: Markdown code presenting an evaluation of the transportation system compatibility.

    """

    # Perform compatibility assessment based on the surface conditions
    # You can implement your own logic here based on the specific requirements of the terraforming project

    # Example implementation
    transportation_compatibility = ""
    for system in existing_transportation_systems:
        transportation_compatibility += f"- {system}: Compatible\n"

    return transportation_compatibility


def assess_energy_compatibility(existing_energy_sources, temperature_range):
    """
    Assess the compatibility of existing energy sources with the proposed temperature range.

    Args:
    existing_energy_sources (list): List of existing energy sources.
    temperature_range (dict): Data on the proposed temperature range.

    Returns:
    str: Markdown code presenting an evaluation of the energy source compatibility.

    """

    # Perform compatibility assessment based on the temperature range
    # You can implement your own logic here based on the specific requirements of the terraforming project

    # Example implementation
    energy_compatibility = ""
    for source in existing_energy_sources:
        energy_compatibility += f"- {source}: Compatible\n"

    return energy_compatibility
