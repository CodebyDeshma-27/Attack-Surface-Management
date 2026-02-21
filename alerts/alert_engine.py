def generate_alerts(risks):
    return [r for r in risks if r["severity"] == "HIGH"]
