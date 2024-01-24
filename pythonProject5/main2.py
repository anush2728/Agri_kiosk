# import LiveSpeech 
from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
	# here the result is stored in phrase which
	# ultimately displays all the words recognized
	print(phrase)
else:
	print("Sorry! could not recognize what you said")
