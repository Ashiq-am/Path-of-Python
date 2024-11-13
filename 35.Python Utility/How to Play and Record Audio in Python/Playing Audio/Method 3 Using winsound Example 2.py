#Import windound
import winsound

#Beep at frequency = 5000 Hz for duration of 1000 ms
winsound.Beep(5000, 1000)

#windows exit sound after completion of above
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
