import os
from google.cloud import storage
from transformers import AutoModelForSequenceClassification



def load_model():
    if not os.path.exists('local_model'):
        os.makedirs('local_model')
    client = storage.Client()
    bucket = client.get_bucket('')
    blob = bucket.blob('')
    blob.download_to_filename('')
    clob = bucket.blob('')
    clob.download_to_filename('')
    try:
        MODEL_PATH = "local_model"

        # Load the model
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
        return model

    except:
        print(f"\n❌ No model found in GCS bucket")

        return None
