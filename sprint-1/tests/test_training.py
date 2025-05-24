from pipelines.training.train_model import train

def test_training_accuracy():
    acc = train()
    assert acc > 0.5, f"⚠️ Accuracy too low: {acc}"
