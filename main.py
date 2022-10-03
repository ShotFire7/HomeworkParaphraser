#I really feel like eating vanilla ice cream right now not sure why

from selenium import webdriver
import pyautogui as pg
import time

#Open input data, iterate through the lines, and append every second line to a list
#Input data format goes like this: term \n definition
f = open("inputdata.txt", "r")
definitionList = []
newList = []
listIter = 0
i = 0
for x in f.readlines():
    i+=1
    if i % 2 == 0:
        definitionList.append(x)
i = -1
#get rid of the newline characters in the list
for x in definitionList:
    i+=1
    definitionList[i] = definitionList[i].replace("\n","")
i = 0
#copy our data to the outputdata - not processed yet
ff = open("outputdata.txt", "a")
ff.write(f.read())
ff.close()

#Main program - open browser, go to the website, and type each definition in the list
#into the textbox, then click the button, press escape to close the popup
#then get the text from the text box and append it to a final list
while listIter < len(definitionList): 
    web = webdriver.Chrome()
    web.get("https://quillbot.com/")
    time.sleep(2)
    
    inputField = web.find_element_by_xpath(r'//*[@id="inOutContainer"]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div[1]')
    mode = web.find_element_by_xpath(r'//*[@id="demo-simple-select"]/div/span')
    phraseButton = web.find_element_by_xpath(r'//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button')
    mode3 = web.find_element_by_xpath(r'//*[@id="quillTopControls"]/div[4]/div[1]/div/div[2]/div[2]/div/div/span/span[3]')
    outputField = web.find_element_by_xpath(r'//*[@id="editable-content-within-article"]')

    mode.click()
    time.sleep(0.5)
    mode2 = web.find_element_by_xpath(r'//*[@id="menu-"]/div[3]/ul/li[2]/div/span')
    mode2.click()
    try:
        mode3.click()
    except Exception as E:
        print(E)
        pass
    time.sleep(4)
    
    while i < 4:
        inputField.click()
        pg.hotkey('ctrl','a')
        pg.press('backspace')
        try:
            pg.write(definitionList[listIter])
        except:
            break
        time.sleep(1)
        pg.hotkey('ctrl','enter')
        time.sleep(5)
        pg.press('escape')
        if listIter != 0:
            if "QuillBot" in outputField.text or newList[listIter-1] == outputField.text or len(outputField.text) < 5:
                break
        newList.append(outputField.text)
        print(newList)
        listIter+=1
        i+=1
    i=0
    web.quit()
i=0
ii = 0
countingVar = 1

#sorting some data
with open('inputdata.txt', 'r') as file:
    data = file.readlines()

#doublespace the input data, add a dash and space after the words
while i < len(data):
    if countingVar%2 == 0:
        data[i] = newList[ii] + "\n\n"
        ii+=1
    else:
        print(i)
        print(data[i])
        data[i] = (data[i].replace("\n","") + " - ")
        print(data[i])
    i+=1
    countingVar+=1
print(data)
#write the data to the output file
with open('outputdata.txt', 'w') as file:
    file.writelines(data)

#debugging stuff
print(data)
print("----")
print(newList)
print('done!')