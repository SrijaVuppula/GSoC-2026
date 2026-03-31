import re
import json


def extract_metadata(text: str) -> dict:
    metadata = {
        "organism": None,
        "sample_type": None,
        "collection_location": None,
        "collection_date": None,
        "condition_or_disease": None
    }

    lower_text = text.lower()

    organism_map = {
        "human": "Homo sapiens",
        "mouse": "Mus musculus",
        "rat": "Rattus norvegicus"
    }

    sample_type_keywords = [
        "liver biopsy",
        "blood sample",
        "tissue sample",
        "skin swab"
    ]

    disease_keywords = [
        "cirrhosis",
        "diabetes",
        "cancer",
        "asthma"
    ]

    for key, value in organism_map.items():
        if key in lower_text:
            metadata["organism"] = value
            break

    for sample_type in sample_type_keywords:
        if sample_type in lower_text:
            metadata["sample_type"] = sample_type
            break

    for disease in disease_keywords:
        if disease in lower_text:
            metadata["condition_or_disease"] = disease
            break

    year_match = re.search(r"\b(20\d{2}|19\d{2})\b", text)
    if year_match:
        metadata["collection_date"] = year_match.group(1)

    location_keywords = ["London", "Athens", "Hyderabad", "Atlanta"]
    for location in location_keywords:
        if location.lower() in lower_text:
            metadata["collection_location"] = location
            break

    return metadata


def find_missing_fields(metadata: dict) -> list:
    required_fields = [
        "organism",
        "sample_type",
        "collection_location",
        "collection_date",
        "condition_or_disease"
    ]
    return [field for field in required_fields if not metadata.get(field)]


def generate_clarification_questions(missing_fields: list) -> list:
    question_map = {
        "organism": "What organism does this sample come from?",
        "sample_type": "What is the sample type?",
        "collection_location": "Where was the sample collected?",
        "collection_date": "What is the collection date?",
        "condition_or_disease": "What condition or disease is associated with this sample?"
    }
    return [question_map[field] for field in missing_fields]


if __name__ == "__main__":
    sample_inputs = [
        "Human liver biopsy collected in London in 2023 from a patient with cirrhosis.",
        "Mouse blood sample collected in Athens from a subject with diabetes."
    ]

    for sample_text in sample_inputs:
        metadata = extract_metadata(sample_text)
        missing_fields = find_missing_fields(metadata)
        questions = generate_clarification_questions(missing_fields)

        result = {
            "input_text": sample_text,
            "structured_metadata": metadata,
            "missing_required_fields": missing_fields,
            "clarification_questions": questions,
            "status": "ready_for_submission" if not missing_fields else "needs_clarification"
        }

        print(json.dumps(result, indent=2))
        print("-" * 50)