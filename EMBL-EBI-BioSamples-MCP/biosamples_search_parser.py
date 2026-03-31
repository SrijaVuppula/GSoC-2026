import json


def parse_search_query(query: str) -> dict:
    filters = {
        "organism": None,
        "sample_type": None,
        "collection_location": None,
        "condition_or_disease": None
    }

    lower_query = query.lower()

    organism_map = {
        "human": "Homo sapiens",
        "mouse": "Mus musculus",
        "rat": "Rattus norvegicus"
    }

    sample_type_keywords = [
        "liver",
        "blood",
        "tissue",
        "skin"
    ]

    disease_keywords = [
        "cirrhosis",
        "diabetes",
        "cancer",
        "asthma"
    ]

    location_keywords = [
        "London",
        "Athens",
        "Hyderabad",
        "Atlanta"
    ]

    for key, value in organism_map.items():
        if key in lower_query:
            filters["organism"] = value
            break

    for sample_type in sample_type_keywords:
        if sample_type in lower_query:
            filters["sample_type"] = sample_type
            break

    for disease in disease_keywords:
        if disease in lower_query:
            filters["condition_or_disease"] = disease
            break

    for location in location_keywords:
        if location.lower() in lower_query:
            filters["collection_location"] = location
            break

    return filters


if __name__ == "__main__":
    queries = [
        "Find human liver samples collected in London related to cirrhosis.",
        "Search for mouse blood samples from Athens with diabetes."
    ]

    for query in queries:
        result = {
            "input_query": query,
            "structured_search_filters": parse_search_query(query),
            "status": "ready_for_search"
        }

        print(json.dumps(result, indent=2))
        print("-" * 50)