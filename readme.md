# SpeakEasy: Interactive Voice Assistant with OpenAI Integration

## Overview

SpeakEasy is a Streamlit-based interactive voice assistant that leverages OpenAI for natural language understanding and generation. Users can record audio input, which is transcribed and used to generate responses from an AI model.

## Features

- **Audio Recording**: Record voice inputs directly in the browser using Streamlit's audio recording component.
- **Transcription**: Automatically transcribe recorded audio into text using OpenAI's transcription service.
- **AI Response**: Use the transcribed text to generate AI responses using OpenAI's GPT-3.5 model.
- **Text-to-Speech**: Convert AI-generated text responses into audio and play them back in the browser.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your_username/speakeasy.git
   cd speakeasy
   ```
2. **Install dependecies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the application**
    ```
    streamlit run app.py 
    ```


## Usage
- Enter your OpenAI API key in the sidebar to enable the voice recorder.
- Click on the voice recorder to start recording audio.
- After recording, the audio will be transcribed and displayed as text.
- The transcribed text will be used to generate an AI response from OpenAI.
- The AI response will be converted to audio and played back automatically with autoplay.

## Technologies Used
- Python: Programming language used for backend processing.
- Streamlit: Open-source app framework used for building web applications with Python.
- OpenAI API: AI-powered services used for audio transcription, natural language understanding, and text-to-speech.
- st_audiorec: Streamlit audio recording component used for capturing voice input in the browser.

## Contributing
Contributions are welcome! Please fork the repository, create a new branch, make your changes, and submit a pull request.