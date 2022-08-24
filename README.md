# 2022 Vietnamese Students in Korea SW Training Program - 2022 주한베트남유학생 SW 교육

## Assignment Report

### Student Information

#### Name: Ho Duc Hieu (호둑휴)
#### Undergraduate student majoring in Computer Science and Engineering
#### Email: hoduchieu01@snu.ac.kr

### Summary
Firstly, the services including Elasticsearch, Logstash, and Kibana were successfully installed and implemented on the Azure Cloud Service. Secondly, the cloud platform of Elasticsearch was also implemented based on cloud.elastic.co. In this project, the dataset 한국환경공단 전기자동차 충전소 정보 was used to analyze and visualized on the Elasticsearch platform based on the real-time provision of nationwide public and private charger status for electric vehicle users and activation of electric vehicle distribution (charging station ID, charger ID, status information) with the dataset of one thousand chargers.

The table below shows the relevant link to this project.

| Item                                                                    | Description                       | Link                        |
| ------------------------------------------------------------------------|-----------------------------------|-----------------------------|
| Implementing Elasticsearch, Logstash, and Kibana on Azure Cloud Service | Elasticsearch Port: 9200, Kibana Port: 5601, Logstash: 5044| Platform: http://20.214.225.33:5601/ |
| Final Project | This is an username and password for viewer. Username: user and Password: user123456 | https://hoduchieu01-b5b07a.kb.us-central1.gcp.cloud.es.io:9243/app/r/s/XPdxl |

### Project Implementation

#### Implementing Elasticsearch, Logstash, and Kibana on Azure Cloud service
According to the documentation and lectures, the installation of Elasticsearch, Logstash, and Kibana were implemented on Azure Cloud service with the public IP address is http://20.214.225.33 with the list of port as the figure below.

![image](https://user-images.githubusercontent.com/23649434/186332304-1cdfc2b9-fe70-4815-b14f-26bf10e070c9.png)
Figure 1. Overview of Virtual Machine on Azure Cloud service (20.214.225.33)

![image](https://user-images.githubusercontent.com/23649434/186332347-5ef5fd03-c900-47e6-b8c0-a79816aa123c.png)
Figure 2. Networking including ports for each service


#### Setting up the server using cloud.elastic.co
Accoring to the documentation and lectures, the server on cloud.elastic.co was also implemented as a platform for analyzing and visualizing dataset of this project. The username and password for viewer role were also added as follows (Username: user and Password: user123456), the username and password for admin were also sent via email. The link of final platform: https://hoduchieu01-b5b07a.kb.us-central1.gcp.cloud.es.io:9243/

#### Dataset Crawling & Dataset Processing & Data Visualization
By accessing into the account provided by organizers, the dataset was collected through API link.  
There are various way for crawling the data from API. In this project, I reported 3 different ways in [Java code](./getChargerInfo.java), [Python code](./getChargerInfo.py), and working with [XML file](./getChargerInfoXML.xml) in VBA of Excel. From the first and second methods, the code was used and uploaded in repository.

![image](https://user-images.githubusercontent.com/23649434/186334691-7b78f8ee-0dd0-45ff-9a21-691a976eab33.png)
Figure 3. Java Code for crawling data from API

![image](https://user-images.githubusercontent.com/23649434/186334590-d6f11baa-d5fe-4994-8675-996f277a1907.png)
Figure 4. Python Code for crawling data from API

For the third method, the [XML data file](./getChargerInfoXML.xml) was downloaded from the API link and was imported using VBA of Excel to generate [data file in Excel](./getChargerInfoData.xlsx).
![image](https://user-images.githubusercontent.com/23649434/186332970-97fe101a-aff1-4c73-8ed3-41e9be5a8dae.png)
Figure 5. XML file of the dataset

![image](https://user-images.githubusercontent.com/23649434/186333661-254dea9b-52c4-434a-a753-ec15cf8d5312.png)
Figure 6. The datafile in Excel

According to this figure, the dataset consists various data fields including  (statNm, statId, chgerId, chgerType, addr, lat, lng, busiId, bnm, busiNm, busiCall, stat, ReportTime, output, zcode, zscode, kind, kindDetail, parkingFree, limitYn, delYnthus). It was pre-processed on the Excel to correct the data format, for example, Report Time and make the dataset clear and concise. 

Finally, the dataset in [CSV file](./getChargerInfoData.csv) was uploaded on the Elasticsearch platform and new position field was created from the lat and lng values in term of visualizing and creating the map of chargers in Republic of Korea. Based on the dataset, various visualization tools were used to show the features of this dataset. The dashboard can be view via https://hoduchieu01-b5b07a.kb.us-central1.gcp.cloud.es.io:9243/app/r/s/XPdxl

#### Summary of the Dashboard
In general, this dashboard shows the visualization of the information on the 1000 Electric vehicle charging stations by the Korea Environment Corporation. According to the visualization, it can be seen that the organization of all chargers is 환경부 with the business ID of ME. On the other hand, the output of chargers is 50 with 98.8% and the charger type is 6 in the most chargers area. Moreover, the highest number of records for charger ID is 804 for type 1. The pie chart shows the variation of the kind details. In addition, the map of chargers visualized the chargers in the Republic of Korea and there are many chargers in big cities like Seoul, and Busan, and also sea contour roads of the Jeju islands. Finally, the pie chart shows the number of chargers with free parking with 57.9% and non-free parking with 42.1%.

![image](https://user-images.githubusercontent.com/23649434/186336182-e54d1436-f43a-4c40-8b48-2af2e542a749.png)
Figure 7. Figure of the Dashboard 

![image](https://user-images.githubusercontent.com/23649434/186336252-099aecbf-373f-47a9-b08c-12b1eeed6dc5.png)
Figure 8. Figure of the Dashboard 

### Acknowledgement
I would like to express my very great appreciation to organizers and the Ministry of Science and ICT, the National IT Industry Promotion Agency, and the Korea Software Industry Association for organizing this course to provide me a lot of knowledge and new experience.
<br>
I would like to express my deep gratitude to the lectures 최승용, 김창호, 박태숙, 정태성 for their valuable time supporting us in class and project assignments and the data.go.kr for approving us using 한국환경공단 전기자동차 충전소 정보 dataset.



