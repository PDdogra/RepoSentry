def calculate_score(issues):
    score = 100

    for issue in issues:
        if issue["severity"] == "HIGH":
            score -= 15
        elif issue["severity"] == "MEDIUM":
            score -= 8

    return max(score, 0)


def get_risk_level(score):
    if score >= 85:
        return "🟢 Good"
    elif score >= 60:
        return "🟡 Moderate"
    else:
        return "🔴 High Risk"