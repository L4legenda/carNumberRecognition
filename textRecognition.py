import easyocrUtils
import re


def getText(imgName):
    
    esocr = easyocrUtils.reader('./num_images/number_'+imgName)
    
    num = esocr[0][1]

    

    num = num.upper()

    num = re.sub('[\\|/:\- ]', '', num)

    print('num', num)

    newNum = ''
    newNum += numToText(num[0])
    newNum += textToNum(num[1])
    newNum += textToNum(num[2])
    newNum += textToNum(num[3])
    newNum += numToText(num[4])
    newNum += numToText(num[5])

    reg = ''

    if len(num) == 8:
        reg = num[-2:]
    elif len(num) == 9:
        reg = num[-3:]
    else:
        for n in esocr:
            r = n[1]
            r = re.sub('[\\|/:\- ]', '',  r)
            if  r.isdigit():
                reg = r

    print('reg', reg)

    newReg = ''

    for i in range(len(reg)):
        newReg += textToNum(reg[i])

    return newNum + " " + newReg

    

def numToText(num):
    objNums = {
        "0": "О",
        "4": "А",
        "7": "У",
        "*": "Х",
        "8": "В",
    }
    if num in objNums:
        return objNums[num]
    return num

def textToNum(text):
    objText = {
        "О": "0",
        "А": "4",
        "У": "7",
        "Ч": "4",
        "Ю": "0",
        "?": "7",
    }
    if text in objText:
        return objText[text]
    return text
