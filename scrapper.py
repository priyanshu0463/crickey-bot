import requests
from bs4 import BeautifulSoup
import csv
from io import StringIO

url = "https://www.espncricinfo.com/live-cricket-score"
response = requests.get(url)



def get_response(message)->str:
    p_message=message.lower()
    if p_message == 'hello' or p_message == 'hi':
        return 'Hey there'
    
    if p_message == '/livescore':
        
        soup = BeautifulSoup(response.text, 'html.parser')

    
        link_element = soup.find('a', href=True, class_='ds-no-tap-higlight')
        url_a = 'https://www.espncricinfo.com'+link_element['href']
        # print(url_a)

        response_a=requests.get(url_a)
        if response.status_code == 200:
            soup_a = BeautifulSoup(response_a.text, 'html.parser')
            txt=soup_a.find_all('div',class_="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-mb-2")
            
            team=":    Team              over/target       current\n"
            for i in range(len(txt)):
                t=txt[i].find_all('span')+txt[i].find_all('strong')
                m='  '
                for j in range(3):
                    if j==(2):
                        if j < len(t):
                            m=m+""+t[j].get_text()+"       "
                        else:
                            m = m + "       N/A"+"        "

                        team=team+"\n   "+m
                    else:
                        if j < len(t):
                            m=m+t[j].get_text()+"       "
                        else:
                            m = m + "       N/A"+"        "
            # print(team)

            txt1=soup_a.find('div',class_="ds-text-compact-xxs ds-p-2 ds-px-4 lg:ds-py-3")
            z=(txt1.find('p').get_text() if  txt1.find('p') is not None else "match yet to start" )
            txt2=soup_a.find('div',class_="ds-text-tight-s ds-font-regular ds-overflow-x-auto ds-scrollbar-hide ds-whitespace-nowrap ds-mt-1 md:ds-mt-0 lg:ds-flex lg:ds-items-center lg:ds-justify-between lg:ds-px-4 lg:ds-py-2 lg:ds-bg-fill-content-alternate ds-text-typo-mid3 md:ds-text-typo-mid2")
            sum=""
            sum2=txt2.find_all("span") if txt2 is not None else ""
            for i in sum2:
                sum=sum + i.get_text()

            

            response_message= "\n"+team+"\n \n \n     SUMMARY:  \n     "+z+" \n     "+sum+"\n"

            print(response_message)
            return response_message
        
    if p_message=='/generate':
        
        response_message=get_response('/livescore')
        return response_message
        
    
          
    if p_message =='!help':
        return '`/livescore : to get the live feed \n/generate : to generate the csv file \n!help : to see this message agani:)`'
    
    
    return 'i didnt understand the message'