# ================================================================================
#                  PYTHON GENERATOR MODULE FOR SNOFLAKE CODMPUTING
# ================================================================================

# importing necessary modules
import os
import pickle

# defining directory as program location
os.chdir(os.curdir+"\\Python\\pyGen\\saves")

# put following code in commentary until implementation of settings
# importing settings as SETTINGS list
# with open("data\\settings.txt","rb") as settings:
    # settings_unpickler=pickle.Unpickler(settings)
    # settings=settings_unpickler.load()


# list generator function
def pyList(userInput):
    """exports a list, based on userInput"""

    # step 1/4  replacing "," in userInput by " " for later split (gives user option to sepearte words with "," not "")
    userInput=userInput.replace(","," ")
    userInput=userInput.split()
    
    # step 2/4    prompts user wether or not to save list
    print(userInput)
    userPrompt=input("Do you wish to save above list ?  y/n\n ")
    
    # step 3a/4   user wishes to save list
    if userPrompt=="y":
        
        # requesting fileName and concatenating ".txt" to fileName
        userPrompt=input("enter file filename WITHOUT EXTENTION\n ")
        userPrompt=userPrompt+".txt"
       
        # checking for file extetion in userInput
        try:
            with open(userPrompt,"wb") as extentionTest:
                extentionTest_pickler=pickle.Pickler(extentionTest)
                extentionTest_pickler.dump(userInput)
        except TypeError:
            raise TypeError("invalid filename, do not use extentions")
        
        # step 4/4    saving list
            with open(userPrompt,"wb") as saveList:
                saveList_pickler=pickle.Pickler(saveList)
                saveList_pickler.dump(userInput)
        
    else:
        return("exiting")