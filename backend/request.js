let payload = {
  creationParams: {
    origin: "/create",
    inputText: "Hello",
    flowType: "text-to-video",
    slug: "gameplay-background-video",
    hasToGenerateVoice: true,
    hasToTranscript: false,
    hasToSearchMedia: true,
    hasAvatar: false,
    hasWebsiteRecorder: false,
    hasTextSmallAtBottom: false,
    ratio: "9 / 16",
    selectedAudio: "Observer",
    selectedVoice: "nPczCjzI2devNBz1zQrb",
    selectedAvatarType: "video/mp4",
    nbGenerations: 1,
    captionPresetName: "Wrap 1",
    sourceType: "contentScraping",
    selectedStoryStyle: {
      value: "custom",
      label: "Custom"
    },
    generationPreset: "DEFAULT",
    hasToGenerateMusic: false,
    generationUserPrompt: "",
    imageGenerationModel: "cheap",
    hasEnhancedGeneration: false,
    hasEnhancedGenerationPro: false,
    inputMedias: [],
    hasToGenerateVideos: false,
    audioUrl: "https://cdn.tfrv.xyz/audio/observer.mp3"
  }
}

fetch("https://www.revid.ai/api/public/v2/render", {
  headers: {
    key: "aaee2be1-f86d-43f6-9f5d-0dd670342f81"
  },
  body: JSON.stringify(payload),
  method: "POST"
}).then((res) => {
  res.json().then((res) => {
    console.log(res)
  })
})
