from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("microsoft/FinBERT-base-uncased-finetuned-squad")
tokenizer = AutoTokenizer.from_pretrained("microsoft/FinBERT-base-uncased-finetuned-squad")

def predict_intent(sentence, company_name):
    # Encode the input sentence and company name
    input_ids = tokenizer.encode(sentence + " " + company_name, return_tensors="pt")

    # Predict the intent of the sentence
    output = model(input_ids)[0]
    _, intent = output.max(dim=1)

    # Map the intent to a label
    intent = intent.item()
    if intent == 0:
        label = "Invest"
    elif intent == 1:
        label = "Avoid"
    else:
        label = "Neutral"

    return label


