import pandas
import winsound
import librosa
import time
import requests

#Base Definitions

basePath = "D:/BahnAnsagen/" #Root Folder
tableNumbersPlatforms = pandas.read_excel(basePath + "_info/2013_01_02_info.xls", sheet_name="gleise_zahlen") #Path to the Info Excel file
# API Request
URL = "https://dbf.finalrewind.org/Karlsruhe%20Hbf.json?detailed=1&version=3"
apiResponse = requests.get(url=URL,stream=True).json()

#Generating Numbers
numberAudioRequest = 900

#If num between 0 and 100
if numberAudioRequest <= 100 or numberAudioRequest == 200 or numberAudioRequest == 300 or numberAudioRequest == 400 or numberAudioRequest == 500 or numberAudioRequest == 600 or numberAudioRequest == 700 or numberAudioRequest == 800 or numberAudioRequest == 900:
    numberAudio = basePath + f"dt/gleise_zahlen/hoch/{numberAudioRequest}.wav"
    winsound.PlaySound(numberAudio,winsound.SND_FILENAME)
#if num between 101 and 999
elif numberAudioRequest <=999 and not numberAudioRequest == 100 and not numberAudioRequest == 200 and not numberAudioRequest == 300 and not numberAudioRequest == 400 and not numberAudioRequest == 500 and not numberAudioRequest == 600 and not numberAudioRequest == 700 and not numberAudioRequest == 800 and not numberAudioRequest == 900:
    hunFirstDigit = str(numberAudioRequest)[0]
    hundretsAudio = basePath + f"dt/gleise_zahlen/tief/{hunFirstDigit}00_.wav"
    hunLastTwoDigits = str(numberAudioRequest)[1:]
    if str(numberAudioRequest)[1] == "0":
        hunLastTwoDigits = str(numberAudioRequest)[2:]
        print(hunLastTwoDigits)
        hunLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{hunLastTwoDigits}.wav"
    else:
        hunLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{hunLastTwoDigits}.wav"
    winsound.PlaySound(hundretsAudio,winsound.SND_FILENAME)
    winsound.PlaySound(hunLastTwoDigitsAudio,winsound.SND_FILENAME)

# If num 4 digits
elif len(str(numberAudioRequest)) == 4:
    if str(numberAudioRequest)[2:] == "00":
        thoFirstTwoDigits = str(numberAudioRequest)[:2]
        thoFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{thoFirstTwoDigits}.wav"
        thoLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/00.wav"
    if str(numberAudioRequest)[2] == "0":
        thoFirstTwoDigits = str(numberAudioRequest)[:2]
        thoFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{thoFirstTwoDigits}.wav"
        thoLastTwoDigits = str(numberAudioRequest)[3]
        thoLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/0{thoLastTwoDigits}.wav"
    else:
        thoFirstTwoDigits = str(numberAudioRequest)[:2]
        thoFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{thoFirstTwoDigits}.wav"
        thoLastTwoDigits = str(numberAudioRequest)[2:]
        thoLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{thoLastTwoDigits}.wav"
    winsound.PlaySound(thoFirstTwoDigitsAudio,winsound.SND_FILENAME)
    winsound.PlaySound(thoLastTwoDigitsAudio,winsound.SND_FILENAME)
#if num 5 digits
elif len(str(numberAudioRequest)) == 5:
    if str(numberAudioRequest)[2] == "0":
        centFirstTwoDigits = str(numberAudioRequest)[:2]
        centFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{centFirstTwoDigits}.wav"
        centMiddleDigitAudio = basePath + f"dt/gleise_zahlen/tief/0.wav"
        centLastTwoDigits = str(numberAudioRequest)[3:]
        centLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{centLastTwoDigits}.wav"
    if str(numberAudioRequest)[3:] == "00":
        centFirstTwoDigits = str(numberAudioRequest)[:2]
        centFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{centFirstTwoDigits}.wav"
        centMiddleDigit = str(numberAudioRequest)[3]
        centMiddleDigitAudio = basePath + f"dt/gleise_zahlen/tief/{centMiddleDigit}.wav"
        centLastTwoDigits = str(numberAudioRequest)[4]
        centLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/0{centLastTwoDigits}.wav"
    else:
        centFirstTwoDigits = str(numberAudioRequest)[:2]
        centFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{centFirstTwoDigits}.wav"
        centMiddleDigit = str(numberAudioRequest)[2]
        centMiddleDigitAudio = basePath + f"dt/gleise_zahlen/tief/{centMiddleDigit}.wav"
        centLastTwoDigits = str(numberAudioRequest)[3:]
        centLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{centLastTwoDigits}.wav"
    winsound.PlaySound(centFirstTwoDigitsAudio,winsound.SND_FILENAME)
    winsound.PlaySound(centMiddleDigitAudio,winsound.SND_FILENAME)
    winsound.PlaySound(centLastTwoDigitsAudio,winsound.SND_FILENAME)
#if num 6 digits
elif len(str(numberAudioRequest)) == 6:
    if str(numberAudioRequest)[1:4] == "00":
        milFirstTwoDigits = str(numberAudioRequest)[:2]
        milFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milFirstTwoDigits}"
        milMiddleTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/00.wav"
        milLastTwoDigits = str(numberAudioRequest)[4:]
        milLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{milLastTwoDigits}"
    if str(numberAudioRequest)[4:] == "00":
        milFirstTwoDigits = str(numberAudioRequest)[:2]
        milFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milFirstTwoDigits}"
        milMiddleTwoDigits = str(numberAudioRequest)[2:4]
        milMiddleTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milMiddleTwoDigits}"
        milLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/00.wav"
    else:
        milFirstTwoDigits = str(numberAudioRequest)[:2]
        milFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milFirstTwoDigits}"
        milMiddleTwoDigits = str(numberAudioRequest)[2:4]
        milMiddleTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milMiddleTwoDigits}"
        milLastTwoDigits = str(numberAudioRequest)[4:]
        milLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{milLastTwoDigits}"
    winsound.PlaySound(milFirstTwoDigitsAudio,winsound.SND_FILENAME)
    winsound.PlaySound(milMiddleTwoDigitsAudio,winsound.SND_FILENAME)
    winsound.PlaySound(milLastTwoDigitsAudio,winsound.SND_FILENAME)





# Definition of the announcement elements
for departure in apiResponse["departures"]:
    trainPlatform = departure["platform"]
    trainFriendlyName = departure["train"]
    trainDestination = departure["destination"]
    trainVia = departure["via"]
    trainScheduledArrival = departure["scheduledArrival"]
    trainScheduluedDeparture = departure["scheduledDeparture"]
    trainArrivalDelay = departure["delayArrival"]
    trainDepartureDelay = departure["delayDeparture"]
    trainIsCancelled = departure["isCancelled"]
    trainDelayMessage = departure["messages"]["delay"]

#tableNumbersPlatforms.loc[tableNumbersPlatforms["Datei-Name", str(numberAudioRequest) + ".wav"]]