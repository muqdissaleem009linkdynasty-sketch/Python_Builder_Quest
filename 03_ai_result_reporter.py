result = {
    "label": "cat",
    "confidence": 0.62,
    "class_id": 3
}


def show_result(result):
    print(f"Label: {result['label']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Class ID: {result['class_id']}")

    if result["confidence"] >= 0.80:
        print("Confident prediction")
    else:
        print("Low confidence")


show_result(result)