import pywhatkit
import pandas as pd

dataframe1 = pd.read_excel('whatsappAutomation.xlsx')

# print(dataframe1.iloc[0][0])

for x in range(0,10):
    print(dataframe1.iloc[x][1])
    if dataframe1.iloc[x][0] != 0:
        text = "Dear " + dataframe1.iloc[x][1] + "\nThis is an automated message using python to send bulk message.\n% Please ignore this %"
        print(dataframe1.iloc[x][0])
        print(text)
        pywhatkit.sendwhatmsg_instantly(dataframe1.iloc[x][0], text, 10, tab_close=True)

