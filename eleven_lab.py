# from elevenlabs import generate, play, save, set_api_key

# set_api_key("sk_7da844a7a919d15bbde4361e120c3d6ec9bf94fdaa2ee932")  # Replace with your key

# audio = generate(
#     text="The first move is what sets everything in motion.",
#     voice="JBFqnCBsd6RMkjVDRZzb",
#     model="eleven_multilingual_v2"
# )

# save(audio, "output.mp3")

# import requests

# # Create speech (POST /v1/text-to-speech/:voice_id)
# response = requests.post(
#   "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128",
#   headers={
#     "xi-api-key": "sk_7da844a7a919d15bbde4361e120c3d6ec9bf94fdaa2ee932"
#   },
#   json={
#     "text": "The first move is what sets everything in motion.",
#     "model_id": "eleven_multilingual_v2"
#   },
# )

# print(response.json())




  
# import base64
# import json

# # Load the JSON file
# with open("audio.json", "r") as f:
#     data = json.load(f)

# # Extract base64 string
# audio_b64 = data["audio"]

# # Decode base64 to bytes
# audio_bytes = base64.b64decode(audio_b64)

# # Save to WAV file
# with open("output.wav", "wb") as f:
#     f.write(audio_bytes)

# print("Audio saved as output.wav")


# import requests
# import json

# TOKEN = "2SeFT7hpsUOjOL4dfdb4637ab3cc1d05d0472c8b08520ad72"
# url = f"https://production-sfo.browserless.io/scrape?token={TOKEN}"

# headers = {
#     "Cache-Control": "no-cache",
#     "Content-Type": "application/json"
# }

# data = {
#     "url": "https://www.sephora.com/",
#     "elements": [
#         { "selector": "a" }
#     ],
#     "waitForTimeout": 1000
# }

# response = requests.post(url, headers=headers, json=data)
# result = response.json()

# print(result)

# import requests

# TOKEN = "2SeFT7hpsUOjOL4dfdb4637ab3cc1d05d0472c8b08520ad72"
# url = f"https://production-sfo.browserless.io/scrape?token={TOKEN}"

# headers = {
#     "Cache-Control": "no-cache",
#     "Content-Type": "application/json",
    
# }

# data = {
#     "url": "https://www.daraz.com.bd/",
#         "elements": [
#         { "selector": "h1" }
#     ],
#     "waitForTimeout": 1000
# }

# try:
#     # First verify the API connection
#     print("Testing API connection...")
#     test_response = requests.get(f"https://production-sfo.browserless.io/", params={"token": TOKEN})
#     print(f"API status: {test_response.status_code}")
    
#     # Make the actual request
#     print("Sending scraping request...")
#     response = requests.post(
#         url,
#         headers=headers,
#         json=data,
#         timeout=5000  # Increased timeout
#     )
    
#     print(f"HTTP Status: {response.status_code}")
#     print(f"Response headers: {response.headers}")
    
#     # Check if response contains data
#     if not response.text.strip():
#         raise ValueError("Empty response received")
    
#     result = response.json()
#     print("Successfully parsed JSON response")
#     print(result)

# except requests.exceptions.JSONDecodeError:
#     print("Failed to decode JSON. Raw response:")
#     print(response.text)
#     print(f"Response length: {len(response.text)} bytes")
    
# except requests.exceptions.RequestException as e:
#     print(f"Request failed: {str(e)}")
    
# except Exception as e:
#     print(f"Unexpected error: {str(e)}")


# import requests

# TOKEN = "2SeFT7hpsUOjOL4dfdb4637ab3cc1d05d0472c8b08520ad72"
# url = f"https://production-sfo.browserless.io/scrape?token={TOKEN}"
# headers = {
#     "Cache-Control": "no-cache",
#     "Content-Type": "application/json"
# }

# data = {
#     "url": "https://www.sephora.com/",
#     "elements": [
#         { "selector": "div" }
#     ],
#     "waitForTimeout": 1000
# }

# response = requests.post(url, headers=headers, json=data)
# result = response.json()

# print(result)


from pytubefix import YouTube
 
def download_youtube_audio(url, output_path="."):
    """
    Downloads the audio from a YouTube video and saves it as an MP3.
 
    Args:
        url (str): The URL of the YouTube video.
        output_path (str): The directory to save the audio file. Defaults to current directory.
    """
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            print(f"Downloading audio from: {yt.title}")
            audio_stream.download(output_path=output_path, filename=f"{yt.title}.mp3")
            print("Download complete!")
        else:
            print("No audio stream found for this video.")
    except Exception as e:
        print(f"An error occurred: {e}")
 
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=OihgT6fRLrE"  # Replace with the actual YouTube video URL
    download_youtube_audio(video_url)