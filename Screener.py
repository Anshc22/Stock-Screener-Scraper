# Add more companies to the list to get info

# If there are any errors pertaining to any company, the company's name will be shown

Companies=['ADORWELD',	'AMBICAAGAR',	'ARSSINFRA',]


Companies_info=[]

#Add user agent
headers={"User-Agent":"Add User-Agent"}
def parse():
    for comp in Companies:
        url=f"https://www.screener.in/company/{comp}"
        r=requests.get(url,headers=headers)
        
        soup=bs(r.content,"html.parser")
        
        Basic_info=soup.find_all("span",{"class":"number"})
        Company=soup.find("h1",{"class":"margin-0"}).text

        tables=soup.find_all("table",{"class":"ranges-table"})[:2]
        Compounded_Sales=tables[0].find_all("td")
        Compounded_Profit=tables[1].find_all("td")

        try:
            try:
                PE=float(Basic_info[4].text.replace(",",""))
            except:
                PE=0
            info={"Company":Company,
                    "Market Cap":float(Basic_info[0].text.replace(",","")),
                    "Current Price":float(Basic_info[1].text.replace(",","")),
                    "High":float(Basic_info[2].text.replace(",","")),
                    "Low":float(Basic_info[3].text.replace(",","")),
                    "P/E":PE,
                    "Book Value":float(Basic_info[5].text.replace(",","")),
                    "Dividend Yield":float(Basic_info[6].text.replace(",","")),
                    "ROCE":float(Basic_info[7].text.replace(",","")),
                    "ROE":float(Basic_info[8].text.replace(",","")),
                    "Face Value":float(Basic_info[9].text.replace(",","")),
                    "TTM":Compounded_Sales[-1].text,
                    "Compounded Sales Growth For 3 Years":Compounded_Sales[-3].text,
                    "Compounded Profit Growth TTM":Compounded_Profit[-1].text,
                    "Compounded Profit Growth 3 Years":Compounded_Profit[-3].text,
                    "NetIncome 2019":float(soup.find(id="profit-loss").find_all("tr",{"class":"strong"})[2].find_all("td")[-3].text.replace(",","")),
                    "NetIncome 2020":float(soup.find(id="profit-loss").find_all("tr",{"class":"strong"})[2].find_all("td")[-2].text.replace(",","")),
                    "NetIncome 2021":float(soup.find(id="profit-loss").find_all("tr",{"class":"strong"})[2].find_all("td")[-1].text.replace(",","")),
                    "Operating Profit 2019":float(soup.find(id="profit-loss").find_all("tr",{"class":"strong"})[0].find_all("td")[-3].text.replace(",","")),
                    "Operating Profit 2020":float(soup.find(id="profit-loss").find_all("tr",{"class":"strong"})[0].find_all("td")[-2].text.replace(",","")),
                    "Operating Profit 2021":float(soup.find(id="profit-loss").find_all("tr",{"class":"strong"})[0].find_all("td")[-1].text.replace(",","")),
                    "Sales 2019":float(soup.find(id="profit-loss").find_all("tr",{"class":"stripe"})[0].find_all("td")[-3].text.replace(",","")),
                    "Sales 2020":float(soup.find(id="profit-loss").find_all("tr",{"class":"stripe"})[0].find_all("td")[-2].text.replace(",","")),
                    "Sales 2021":float(soup.find(id="profit-loss").find_all("tr",{"class":"stripe"})[0].find_all("td")[-1].text.replace(",","")),
                    "Expenses 2019":float(soup.find(id="profit-loss").find_all("tr")[2].find_all("td")[-3].text.replace(",","")),
                    "Expenses 2020":float(soup.find(id="profit-loss").find_all("tr")[2].find_all("td")[-2].text.replace(",","")),
                    "Expenses 2021":float(soup.find(id="profit-loss").find_all("tr")[2].find_all("td")[-1].text.replace(",","")),
                    "EPS 2019":float(soup.find(id="profit-loss").find_all("tr",{"class":"stripe"})[-1].find_all("td")[-3].text),
                    "EPS 2020":float(soup.find(id="profit-loss").find_all("tr",{"class":"stripe"})[-1].find_all("td")[-2].text),
                    "EPS 2021":float(soup.find(id="profit-loss").find_all("tr",{"class":"stripe"})[-1].find_all("td")[-1].text),
                    "Share Capital 2019":soup.find(id="balance-sheet").find_all("tr",{"class":"stripe"})[0].find_all("td")[-3].text,
                    "Share Capital 2020":soup.find(id="balance-sheet").find_all("tr",{"class":"stripe"})[0].find_all("td")[-2].text,
                    "Share Capital 2021":soup.find(id="balance-sheet").find_all("tr",{"class":"stripe"})[0].find_all("td")[-1].text,
                    "Expenses 2019":soup.find(id="balance-sheet").find_all("tr")[2].find_all("td")[-3].text,
                    "Expenses 2020":soup.find(id="balance-sheet").find_all("tr")[2].find_all("td")[-2].text,
                    "Expenses 2021":soup.find(id="balance-sheet").find_all("tr")[2].find_all("td")[-1].text,
                    "Long Term Liabilities 2019":soup.find(id="balance-sheet").find_all("tr",{"class":"stripe"})[1].find_all("td")[-3].text,
                    "Long Term Liabilities 2020":soup.find(id="balance-sheet").find_all("tr",{"class":"stripe"})[1].find_all("td")[-2].text,
                    "Long Term Liabilities 2021":soup.find(id="balance-sheet").find_all("tr",{"class":"stripe"})[1].find_all("td")[-1].text,
                    "Fixed Assets 2019":soup.find(id="balance-sheet").find_all("tr")[6].find_all("td")[-3].text,
                    "Fixed Assets 2020":soup.find(id="balance-sheet").find_all("tr")[6].find_all("td")[-2].text,
                    "Fixed Assets 2021":soup.find(id="balance-sheet").find_all("tr")[6].find_all("td")[-1].text
                    }
            # If they are >20 more than might want to opt for implementing a time.sleep() to not get banned
            Companies_info.append(info)
            print(f"--{comp} Scraped--\n")
            
            # time.sleep(5)
        except:
          # Company for which data couldn't be scraped
            print(f"Failed Scraping For {Company}")
parse()
# Change file name and path accordingly
pd.DataFrame(Companies_info).to_csv("Companies2.csv",index=False)
