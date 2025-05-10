import pandas
from playsound import playsound
import time
import requests
import re
from difflib import SequenceMatcher


#Base Definitions

basePath = "/home/nekonina/Documents/bahn/" #Root Folder
tableCities = pandas.read_excel(basePath + "_info/2013_01_02_info.xls", sheet_name="ziele") #Path to the Info Excel file
# API Request
URL = "https://dbf.finalrewind.org/Karlsruhe%20Hbf.json?detailed=1&version=3"
apiResponse = requests.get(url=URL,stream=True).json()

platformAudio = basePath + f"dt/module_3_1/016.wav"
entryAudio = basePath + f"dt/module_3_1/012.wav"
departureOnTimeAudio = basePath + f"dt/module_3_1/001.wav"
departureWithDelayAudio = basePath + f"dt/module_3_1/002.wav"
arrivalOnTimeAudio = basePath + f"dt/module_3_1/004.wav"
arrivalWithDelayAudio = basePath + f"dt/module_3_1/005.wav"
trainToAudio = basePath + f"dt/module_3_1/032.wav"
trainFromAudio = basePath + f"dt/module_3_1/038.wav"
viaSound = basePath + f"dt/module_3_1/035.wav"
attentionArrival = basePath + f"dt/module_3_1/046.wav"
gongdefault = basePath + f"gong/513/513_1.wav"
doNotBoard = basePath + f"dt/module_3_1/007.wav"
trainInformationOn = basePath + f"dt/module_3_1/030.wav"

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#Generating Numbers
def speakNumber(number):
    print(number)
    numberAudioRequest = int(re.findall(r'\d+',number)[0])
#If num between 0 and 100
    if numberAudioRequest <= 100 or numberAudioRequest == 200 or numberAudioRequest == 300 or numberAudioRequest == 400 or numberAudioRequest == 500 or numberAudioRequest == 600 or numberAudioRequest == 700 or numberAudioRequest == 800 or numberAudioRequest == 900:
        numberAudio = basePath + f"dt/gleise_zahlen/hoch/{numberAudioRequest}.wav"
        playsound(numberAudio)
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
        playsound(hundretsAudio)
        playsound(hunLastTwoDigitsAudio)

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
        playsound(thoFirstTwoDigitsAudio)
        playsound(thoLastTwoDigitsAudio)
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
        playsound(centFirstTwoDigitsAudio)
        playsound(centMiddleDigitAudio)
        playsound(centLastTwoDigitsAudio)
    #if num 6 digits
    elif len(str(numberAudioRequest)) == 6:
        if str(numberAudioRequest)[1:4] == "00":
            milFirstTwoDigits = str(numberAudioRequest)[:2]
            milFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milFirstTwoDigits}.wav"
            milMiddleTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/00.wav"
            milLastTwoDigits = str(numberAudioRequest)[4:]
            milLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{milLastTwoDigits}.wav"
        if str(numberAudioRequest)[4:] == "00":
            milFirstTwoDigits = str(numberAudioRequest)[:2]
            milFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milFirstTwoDigits}.wav"
            milMiddleTwoDigits = str(numberAudioRequest)[2:4]
            milMiddleTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milMiddleTwoDigits}.wav"
            milLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/00.wav"
        else:
            milFirstTwoDigits = str(numberAudioRequest)[:2]
            milFirstTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milFirstTwoDigits}.wav"
            milMiddleTwoDigits = str(numberAudioRequest)[2:4]
            milMiddleTwoDigitsAudio = basePath + f"dt/gleise_zahlen/tief/{milMiddleTwoDigits}.wav"
            milLastTwoDigits = str(numberAudioRequest)[4:]
            milLastTwoDigitsAudio = basePath + f"dt/gleise_zahlen/hoch/{milLastTwoDigits}.wav"
        playsound(milFirstTwoDigitsAudio)
        playsound(milMiddleTwoDigitsAudio)
        playsound(milLastTwoDigitsAudio)

#Generating Time
def speakTime(time):
    timeAudioRequest = time
    if str(time)[3:] == "00":
        hour = str(time)[:2]
        hourAudio = basePath + f"dt/zeiten/stunden/tief/{hour}.wav"
        playsound(hourAudio)
    else:
        hour = str(time)[:2]
        hourAudio = basePath + f"dt/zeiten/stunden/hoch/{hour}.wav"
        minute = str(time)[3:]
        minuteAudio = basePath + f"dt/zeiten/minuten/tief/{minute}.wav"
        playsound(hourAudio)
        playsound(minuteAudio)

#Train Types
def speakTrainName(trainName):
    regexResult = re.search(r"(.+?)(\d+)",trainName)
    for trainType in regexResult.group(1).split():
        traintypeAudio = basePath + f"/dt/zuggattungen/hoch/{trainType.lower()}.wav"
        try:
            playsound(traintypeAudio)
        except:
            playsound(basePath + "dt/zuggattungen/hoch/zug.wav")
    trainNumber = regexResult.group(2)
    speakNumber(trainNumber)

def speakCity(cityname):
    print(cityname)
    sorted = tableCities.sort_values(by="Tarifmäßige_Bahnhofsbezeichnung", key=lambda col: col.transform(lambda x: -similar(x,cityname)))
    cityNameAudio = basePath + f"/dt/ziele/variante2/hoch/{sorted.iloc[0]["Datei"]}"
    playsound(cityNameAudio)

# Definition of the announcement elements
for departure in apiResponse["departures"]:
    trainPlatform = departure["platform"]
    trainFriendlyName = departure["train"]
    trainDestination = departure["destination"]
    try:
        trainOrigin = departure["route"][0]["name"]
    except:
        pass
    trainVia = departure["via"]
    trainScheduledArrival = departure["scheduledArrival"]
    trainScheduluedDeparture = departure["scheduledDeparture"]
    trainArrivalDelay = departure["delayArrival"]
    trainDepartureDelay = departure["delayDeparture"]
    trainIsCancelled = departure["isCancelled"]
    trainDelayMessage = departure["messages"]["delay"]

  

    if trainPlatform == "":
        continue
    playsound(gongdefault)
    playsound(platformAudio)
    speakNumber(trainPlatform)
    playsound(entryAudio)
    speakTrainName(trainFriendlyName)


    if not trainScheduluedDeparture == None or trainScheduluedDeparture == "":
        playsound(trainToAudio)
        speakCity(trainDestination)
        if trainVia:
            playsound(viaSound)
            try: 
                speakCity(trainVia[1])
            except:
                speakCity(trainVia[0])
        if trainDepartureDelay == None or trainDepartureDelay < 5:

            playsound(departureOnTimeAudio)
        else:
            playsound(departureWithDelayAudio)
        speakTime(trainScheduluedDeparture)
        
    else:
        playsound(trainFromAudio)
        speakCity(trainOrigin)
        if trainArrivalDelay == None or trainArrivalDelay < 5:
            playsound(arrivalOnTimeAudio)
        else:
            playsound(arrivalWithDelayAudio)
        speakTime(trainScheduledArrival)
        playsound(doNotBoard)
    playsound(attentionArrival)

    if (trainDepartureDelay or 0) >=5:
        playsound(trainInformationOn)
        speakTrainName(trainFriendlyName)
        playsound(departureOnTimeAudio)
        speakTime(trainScheduluedDeparture)
        
        h = min(int(trainDepartureDelay / 5) * 5 if trainDepartureDelay < 60 else int(trainDepartureDelay / 10) * 10, 210)
        playsound(basePath + f"dt/zeiten/verspaetung_heute/{h:03}.wav")

    input()