from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

video_clip = VideoFileClip("output0.mp4")
audio_clip = AudioFileClip("conversation.wav")

video_clip_duration = video_clip.duration
audio_clip_duration = audio_clip.duration

new_video_parts = [video_clip]

if audio_clip_duration > video_clip_duration:
    # Extend video by looping or repeating part
    length_to_add = audio_clip_duration - video_clip_duration
    subclip = video_clip.subclipped(0, min(length_to_add, video_clip.duration))
    new_video_parts.append(subclip)

# Concatenate all video parts
final_video = concatenate_videoclips(new_video_parts)

# Set the longer audio
final_video = final_video.with_audio(audio_clip)

# Write the output
final_video.write_videofile("final_output.mp4", codec="libx264", audio_codec="aac")



# for i in range(0, int(duration), 30):
#     subclip = clip.subclipped(i, min(i + 30, duration))
   
#     # Example edit: apply a fade-in effect
#     edited = subclip.crossfadein(2) 
    
#     segments.append(subclip)

#     final_clip = concatenate_videoclips(subclip)
#     subclip.write_videofile(f"output{i}.mp4")



# import speech_recognition as sr

# # Initialize the recognizer
# r = sr.Recognizer()

# # Load the audio file
# with sr.AudioFile("conversation.wav") as source:
#     audio_data = r.record(source)  # Read the entire audio file

# # Transcribe the audio using Google Web Speech API
# try:
#     text = r.recognize_google(audio_data)
#     print(f"Transcription: {text}")
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print(f"Could not request results from Google Speech Recognition service; {e}")








# final_clip = video_clip.with_audio(audio_clip)
# final_clip.write_videofile("output.mp4")