from services.ai.ai_process import detect_disease
from services.ai.shared_method import get_the_five_highest_value_dictionary, normalized_dictionary_values


def detect_disease_from_symptom(symptoms):
    print('Symptoms: ', symptoms)
    raw_disease = detect_disease(symptoms)
    raw_disease = normalized_dictionary_values(raw_disease)
    diseases = get_the_five_highest_value_dictionary(raw_disease)
    print('Diseases: ', diseases)
    return diseases
