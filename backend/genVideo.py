import requests
import json


def generate_video(text: str):
    payload = """{
    "webhook": "fill this webhook",
    "creationParams": {
        "origin": "/create",
        "inputText": "Hello",
        "flowType": "text-to-video",
        "slug": "gameplay-background-video",
        "hasToGenerateVoice": true,
        "hasToTranscript": false,
        "hasToSearchMedia": true,
        "hasAvatar": false,
        "hasWebsiteRecorder": false,
        "hasTextSmallAtBottom": false,
        "ratio": "9 / 16",
        "selectedAudio": "Observer",
        "selectedVoice": "nPczCjzI2devNBz1zQrb",
        "selectedAvatarType": "video/mp4",
        "nbGenerations": 1,
        "captionPresetName": "Wrap 1",
        "sourceType": "contentScraping",
        "selectedStoryStyle": {
            "value": "custom",
            "label": "Custom"
        },
        "generationPreset": "DEFAULT",
        "hasToGenerateMusic": false,
        "generationUserPrompt": "",
        "imageGenerationModel": "cheap",
        "hasEnhancedGeneration": false,
        "hasEnhancedGenerationPro": false,
        "inputMedias": [],
        "hasToGenerateVideos": false,
        "audioUrl": "https://cdn.tfrv.xyz/audio/observer.mp3"
    }
}"""
    headers= {
        "key": "aaee2be1-f86d-43f6-9f5d-0dd670342f81"
    }
    print(payload)
    print(requests.post("https://www.revid.ai/api/public/v2/render", data=payload, headers=headers).json())

if __name__ == "__main__":
    generate_video("a")
