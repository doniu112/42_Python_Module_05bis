def validate_ingredients(ingredients: str) -> str:
    from . import light_spellbook

    cleaned = ingredients.lower()

    for char in ",.!?;:":
        cleaned = cleaned.replace(char, " ")

    allowed = light_spellbook.light_spell_allowed_ingredients()

    valid = any(
        word in allowed
        for word in cleaned.split()
    )

    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
