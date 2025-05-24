import pytest
from pipelines.ingestion.data_loader import load_config, load_data

def test_config_load():
    config = load_config()
    assert "data_path" in config
    assert config["env"] == "dev"

def test_data_load():
    config = load_config()
    try:
        df = load_data(config)
        assert df.shape[0] > 0
    except Exception as e:
        pytest.fail(f"Ingestion failed: {e}")
