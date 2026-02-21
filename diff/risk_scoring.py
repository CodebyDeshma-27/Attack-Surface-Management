def score_risk(diff):
    risks = []

    for item in diff["added"]:
        risks.append({
            "change": item,
            "severity": "HIGH",
            "reason": "New exposure detected"
        })

    for item in diff["removed"]:
        risks.append({
            "change": item,
            "severity": "LOW",
            "reason": "Service removed"
        })

    return risks
