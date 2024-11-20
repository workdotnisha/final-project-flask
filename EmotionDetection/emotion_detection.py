import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=header)
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion.items(), key=lambda x: x[1])
    emotion['dominant_emotion'] = dominant_emotion
    return emotion