def test_event_correlation_basic():
    from core.event_correlation import correlate_events
    assert correlate_events([], [], []) == []
