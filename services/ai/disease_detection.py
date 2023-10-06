from services.ai.ai_process import DiseaseDetection
from services.ai.shared_method import get_the_five_highest_value_dictionary, normalized_dictionary_values


def model_init(load_model: bool):
    disease_detection = DiseaseDetection()
    if load_model:
        disease_detection.load_model("services\\ai\\models\\")
    else:
        disease_detection.train('./data/dataset.csv')
        disease_detection.save_model()
    return disease_detection


def detect_disease_from_symptom(model, symptoms):
    print('Symptoms: ', symptoms)
    raw_disease = model.predict(symptoms, min_matching_ratio=0.5)
    raw_disease = normalized_dictionary_values(raw_disease)
    diseases = get_the_five_highest_value_dictionary(raw_disease)
    print('Diseases: ', diseases)
    return diseases
