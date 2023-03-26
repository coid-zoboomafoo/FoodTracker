import requests
import xmltodict
import json

# Need to make something that allows you to run the code for a variety of different report parameters


url = 'https://marketnews.usda.gov/mnp/fv-report?&commAbr=&step3date=true&locAbr=HC&repType=termPriceDaily&locName=LOS+ANGELES&refine=false&type=termPrice&Run.y=16&Run.x=22&repTypeChanger=termPriceDaily&environment=&reportConfig=true&x=59&_environment=1&y=6&locAbrPass=ALL%7C%7C&locChoose=location&commodityClass=allcommodity&locAbrlength=1&organic=&repDate=03%2F24%2F2023&endDate=03%2F25%2F2023&format=xml&rebuild=false'
response = requests.get(url)

with open('file.xml', 'wb') as f:
    f.write(response.content)


# Open the XML file and read it into a string
with open('file.xml', 'r') as xmlfile:
    xmlstring = xmlfile.read()

# Convert the XML string to a dictionary using xmltodict
xmldict = xmltodict.parse(xmlstring)

# Convert the dictionary to a JSON string using the json module
jsonstring = json.dumps(xmldict)

# Write the JSON string to a file
with open('file.json', 'w') as jsonfile:
    jsonfile.write(jsonstring)


# commAbr	ALFALFAS-V
# step3date	true
# locAbr	HC
# repType	termPriceDaily
#locName	LOS ANGELES
# refine	false
#Run	Run
#type	termPrice
#repTypeChanger	termPriceDaily
#environment	
#reportConfig	true
#x	59
#_environment	1
#y	6
#locAbrPass	`ALFALFA SPROUTS
#locChoose	location
#commodityClass	allcommodity
#locAbrlength	1
#organic	
#repDate	02/23/2023
#endDate	03/25/2023
#format	xml
#rebuild	false