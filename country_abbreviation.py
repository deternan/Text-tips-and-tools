
# coding=utf8

'''
version: April 06, 2020 02:11 PM
Last revision: April 06, 2020 03:00 PM

Author : Chao-Hsuan Ke
'''

'''
country dict
'''


Taiwan_Chinese_dict = {'台灣': 'tw', '臺灣': 'tw', '呆丸': 'tw', '台湾': 'tw'}
China_Chinese_dict = {'中國': 'cn', '大陸': 'cn', '老共': 'cn', '中国': 'cn'}
Japan_Chinese_dict = {'日本': 'jp'}
America_Chinese_dict = {'美國': 'us', '美国': 'us', '米國': 'us', '米国': 'us'}


#print(Taiwan_Chinese_dict.get('臺灣'))
#print(China_Chinese_dict.get('中國'))


def get_abbreviation(country):
    getAbb = None
    tagCheck = False
    if Taiwan_Chinese_dict.get(country) != None:
        getAbb = Taiwan_Chinese_dict.get(country)
        tagCheck = True

    if China_Chinese_dict.get(country) != None:
        getAbb = China_Chinese_dict(country)
        tagCheck = True

    if Japan_Chinese_dict.get(country) != None:
        getAbb = Japan_Chinese_dict.get(country)
        tagCheck = True

    if America_Chinese_dict.get(country) != None:
        getAbb = America_Chinese_dict.get(country)
        tagCheck = True


    if tagCheck == True:
        print(getAbb)
    else :
        print('None')


get_abbreviation('阿根廷')
