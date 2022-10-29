import pywhatkit
import pandas as pd

dataframe1 = pd.read_excel('whatsappAutomation.xlsx')
# dataframe1 = pd.read_excel('interviewer.xlsx')
# print


for x in range(472, 500):
    # print(dataframe1.iloc[x][0])
    # print(dataframe1.iloc[x][1])
    if dataframe1.iloc[x][0] != '':
        print(dataframe1.iloc[x][0])
        text = "Dear " + dataframe1.iloc[x][1] + ",\n\nThis is Utsav Bhardwaj, an alumnus of IIT Madras and CEO of Fyzen Career Solutions Pvt Ltd. Thank you for your interest to help final year students of IITs (who are appearing for campus placements) by conducting their Mock Interviews (with Live Feedback) through our Online Mock Interview Platform [interwiu.com], the link of which is given below. \n\n*https://interwiu.com/* \n\nKindly please register on the platform as a Professional (i.e., an Interviewer) as soon as possible. *Please use [interwiu.com] only on a Laptop/Desktop for best experience.* \n\nFor any queries/concerns, please feel free to reach out to me at +91-9176583479 anytime. \n\nThank you."
        # text = "Dear " + dataframe1.iloc[x][1] + "\nThis is an automated message using python"
        print(text)
        pywhatkit.sendwhatmsg_instantly(dataframe1.iloc[x][0], text, 10, tab_close=True)
        print('message sent...')
