from . import elements
import elements as main_elements


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{elements.create_earth()}' "
        f"and '{elements.create_air()}'"
        )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{main_elements.create_fire()}' "
        f"and '{main_elements.create_water()}'"
        )
