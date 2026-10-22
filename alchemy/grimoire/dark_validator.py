from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    cleaned = ingredients.lower()

    for char in ",.!?;:":
        cleaned = cleaned.replace(char, " ")

    allowed = dark_spell_allowed_ingredients()

    valid = any(
        word in allowed
        for word in cleaned.split()
    )

    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
