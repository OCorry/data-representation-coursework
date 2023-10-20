import csv 
import requests

retrieveTags=['TrainStatus',
              'TrainLatitude',
              'TrainLongitude',
              'TrainCode',
              'TrainDate',
              'PublicMessage',
              'Direction'
              ]


from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

#checking that it outputs to the terminal 
#print(doc.toprettyxml(), newline=' ')

#Storing the url as a xml file 
with open("url", "w") as xmlfp:
    doc.writexml(xmlfp)



objTrainPositionNodes =doc.getElementsByTagName("objTrainPositions")
with open("train.csv", mode ='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter= "\t", quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    for objTrainPositionsNode in objTrainPositionNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())

        train_writer.writerow(dataList)
    """
    #Modifying the program to print out the latitudes 
    objTrainPositionNodes =doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionNodes:
        trainlatitude = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
        trainlatitude = trainlatitude.firstChild.nodeValue.strip()
        #print(trainlatitude)
    """

    