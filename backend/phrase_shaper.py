def shape_phrases(keywords: list[str]) -> str:
    """
    Turns raw extracted keywords into more natural, flowing English phrases.
    Example:
    ['refactor', 'mean-variance optimizer', 'volatility thresholds', 'market regimes']
    → "Refactor the mean-variance optimizer to adjust volatility thresholds across different market regimes."
    """

    if not keywords:
        return "the topic"

    action_verbs = {"refactor", "optimize", "adjust", "tune", "calibrate", "modify", "enhance", "reduce", "improve"}

    verbs = [kw for kw in keywords if any(verb in kw.lower() for verb in action_verbs)]
    objects = [kw for kw in keywords if kw not in verbs]

    if verbs and objects:
        main_action = verbs[0].capitalize()

        if len(objects) == 1:
            target = objects[0]
        else:
            target = ", ".join(objects[:-1]) + " and " + objects[-1]

        phrase = f"{main_action} the {target}"
    else:
        if len(keywords) == 1:
            phrase = keywords[0]
        else:
            phrase = ", ".join(keywords[:-1]) + " and " + keywords[-1]

    return phrase