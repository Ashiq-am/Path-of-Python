from youtube_transcript_api import YouTubeTranscriptApi

# assigining srt variable with the list of dictonaries
# obtained by the the .get_transcript() function
# and this time it gets only teh subtitles that
# are of english langauge.
srt = YouTubeTranscriptApi.get_transcript("SW14tOda_kI",
										languages=['en'])

# prints the result
print(srt)
