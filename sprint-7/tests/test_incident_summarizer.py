def test_summary_template():
    from core.incident_summarizer import summarize_incident
    result = summarize_incident([], {})
    assert "root_cause" in result
