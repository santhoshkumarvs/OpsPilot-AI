from core.rca_engine import perform_root_cause_analysis

def test_memory_alert_analysis():
    test_input = {
        ("auth-service", datetime(2025, 5, 26, 11, 1, tzinfo=timezone.utc)): [
            {
                "message": "Memory usage spike",
                "metric": "memory",
                "service": "auth-service",
                "timestamp": "2025-05-26T11:01:00Z"
            }
        ]
    }
    result = perform_root_cause_analysis(test_input, [], [])
    assert result["root_cause"]["auth-service"] == "Memory usage spike"
