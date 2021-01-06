from zeep import Client
import xmltodict,json


#wsdl = " http://dev.usbooking.org/us/UnitedSolutions?wsdl"
client = Client(wsdl="http://dev.usbooking.org/us/UnitedSolutions?wsdl")
xml_file = client.service.FlightAvailability('GULFTN', 'PASSWORD', 'PLZ161', 'KTM', 'BWA', '7-1-2021', '', 'O', 'NP', 1, 0,'49.25.14.12')
#xml_file1 = client.service.Reservation('U4', 'd27185d1-dc00-491e-88bf-17905b44c162', 'TMPPNR', 'HK', '05/01/2021', '21:49')
#print(xml_file)
with open("xmlfile", "w") as xmlfile1:
    xmlfile1.write(xml_file)
    xmlfile1.close()

data_dict = xmltodict.parse(xml_file)
json_data = json.dumps(data_dict)
with open("data.json", "w") as json_file:
    json_file.write(json_data)
    json_file.close()


