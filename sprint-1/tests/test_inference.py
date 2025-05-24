from pipelines.inference.predict import TransactionInput, predict

def test_prediction():
    sample = TransactionInput(
        age=35,
        income=60000,
        transaction_count=3,
        transaction_amount=250.0
    )
    result = predict(sample)
    assert "prediction" in result
    assert result["prediction"] in [0, 1]
