import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)

def extract_fields(text):
    fields = {
        "Name": "Extracted Name",
        "Address": "Extracted Address",
        "Income": "Extracted Income",
        "Loan Amount": "Extracted Loan Amount"
    }
    return fields