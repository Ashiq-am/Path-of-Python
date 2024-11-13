from youtube_transcript_api import YouTubeTranscriptApi

# assigining srt variable with the list
# of dictonaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("SW14tOda_kI")

# prints the result
print(srt)
