#import libraries
import streamlit as st
from openai import AzureOpenAI
import openai
from st_audiorec import st_audiorec
import base64
import os
from dotenv import load_dotenv

load_dotenv()

def setup_openai_client(_apikey):
    # return AzureOpenAI(api_key=_apikey, azure_endpoint="https://stats.openai.azure.com/", api_version="2024-02-01")
    return openai.OpenAI(api_key=_apikey)

#transcribe audio to text
def transcribe_audio(client, audio_file):
    with open(audio_file, "rb") as audio_path:
        transcript = client.audio.transcription.create(model="whisper-1", file=audio_path)
        return transcript.text
    
#taking response from openai
def fetch_ai_response(client, input_text):
    messages = [{"role": "user", "content": input_text}]
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106", messages=messages)
    return response.choices[0].message.content

#convert text to audio
def text_to_audio(client, audio_path, text):
    response = client.audio.speech.create(model="tts-1", voice="nova", input=text)
    return response.stream_to_file(audio_path)

def text_cards(text, title="Response"):
    card_html = f"""
        <style>
            .container {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0; /* Background color for the container */
            }}

            .card {{
                width: 300px; /* Width of the card */
                padding: 20px;
                background-color: #ffffff; /* Background color of the card */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Box shadow for a subtle lift effect */
                border-radius: 10px; /* Border radius for rounded corners */
                text-align: center;
            }}

            .card h1 {{
                font-size: 24px; /* Font size for the title */
                margin-bottom: 10px;
                color: #333333; /* Text color for the title */
            }}

            .card p {{
                font-size: 16px; /* Font size for the text */
                color: #666666; /* Text color for the paragraph */
                line-height: 1.6; /* Line height for better readability */
            }}
        </style>

        <div class="container">
            <div class="card">
                <h1>{title}</h1>
                <p>{text}</p>
            </div>
        </div>
    """
    st.markdown(card_html,unsafe_allow_html=True)
    
    

#Frontend
def main():
    st.sidebar.title("API KEY CONFIGURATION")
    api_key = st.sidebar.text_input("Enter your API key", type="password")
    
    st.title("🔉 SpeakEasy")
    st.write("Hi There! Click on the voice recorder to interact with me. How can I help you? 🤔")
    
    # Check for api_key:
    if api_key:
        try:
            client = setup_openai_client(api_key)
            st.success("API key validated. You can now record audio.")
            
            # Adding the audio recorder
            wav_audio_data = st_audiorec()

            
            if wav_audio_data is not None:
                # st.audio(wav_audio_data, format="audio/wav")
                st.write("Audio recorded successfully!")
                audio_file="audio.mp3"
                with open(audio_file,"wb") as f:
                    f.write(wav_audio_data)
                    
                transcribed_text=transcribe_audio(client,audio_file)
                text_cards(transcribed_text,"Transcribed Text")
                
                ai_response=fetch_ai_response(client,transcribed_text)
                response_file="audio_response.mp3"
                text_to_audio(client,response_file,ai_response)
                st.audio(response_file)
                
                text_cards(ai_response,"AI response")
                
                
            else:
                st.warning("No audio recorded yet.")
        except Exception as e:
            st.error(f"Error setting up OpenAI client: {e}")
    else:
        st.warning("Please enter your API key to enable the recorder.")

if __name__ == "__main__":
    main()
