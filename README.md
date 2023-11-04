# B.Sc Project, Healthcare System
BSc Project in Amirkabir University of Technology(Tehran Polytechnique), Prototyping a Healthcare System using microservices architecture include four services: 1.User 2. Disease Prediction 3. Expertise Detection 4. Search Physician <br>
this project was under supervision of Professor [Amir Kalbasi](https://scholar.google.com/citations?user=oISEZIUAAAAJ&hl=en&oi=ao) <br>
You can see full report in this file(in Persian): [Thesis Report](https://github.com/pouyanhessabi/B.Sc-Final-Project-Healthcare-Microservice/blob/main/Report/Hessabi%20Final%20Report.pdf)

# Abstract
Applications in the field of healthcare have developed according to the user's needs and their capabilities have increased. Accurate disease diagnosis with methods based on artificial intelligence is one of the up-to-date issues of these systems. Apart from the diagnosis of the disease, in many cases the patient does not know which doctor he should consult with which specialty. This confusion may lead to referring to an unrelated specialist and waste a lot of time.Software architecture has always been one of the important issues in design and development. Microservices architecture, as an indicative model of software architecture, which was created with the philosophy of separating large system components into smaller services, offers many solutions for design and implementation. In this project, the healthcare system for disease diagnosis and referral to a specialist has been designed and prototyped using microservice architecture. The system is divided into small and independent services in a way that is scalable and can be developed and maintained in the future. In this project, the user can interact with the program using the user interface and meet his needs by connecting to the services. The implemented services are: user login service, disease prediction service, expertise detection service, physician search service. Each of the services has different capabilities that will be discussed below.</br>
In the end, with the tools and evaluation methods and their matching with the system requirements, relying on the principles of software engineering, it can be seen that the microservice architecture and the technologies used are a suitable option for the design of the desired system.

# Thesis Table of Content
**Chapter 1: Introduction** <br>
**Chapter 2: Review of Previous Works** <br>
**Chapter 3: Microservices Architecture** <br>
**Chapter 4: System Requirements** <br>
**Chapter 5: Design and Implementation** <br>
**Chapter 6: System Evaluation** <br>
**Chapter 7: Conclusion and Future Recommendations** <br>
# System Features
The system include four services: 1.User 2. Disease Prediction 3. Expertise Detection 4. Search Physician. </br>
**Use-Case Diagram:** </br>
![](https://github.com/pouyanhessabi/B.Sc-Final-Project-Healthcare-Microservice/blob/main/Report/Gif/Disease%20and%20Expertise%20Prediction.gif)
## User
This service includes three main functions: registration, validation and login, user profile, home page. The main implementation of this service has been done with the libraries inside the Flask framework. <br>
**Run**: <br>
![](https://github.com/pouyanhessabi/B.Sc-Final-Project-Healthcare-Microservice/blob/main/Report/Gif/User%20Gif.gif)
## Disease Prediction
This service gets patient symptoms and give probable diseases. it has implemented with `XGBoost`, [symptoms-disease dataset](https://github.com/pouyanhessabi/B.Sc-Final-Project-Healthcare-Microservice/blob/main/services/ai/data/dataset.csv)<br>
**Run**: <br>
![](https://github.com/pouyanhessabi/B.Sc-Final-Project-Healthcare-Microservice/blob/main/Report/Gif/Disease%20and%20Expertise%20Prediction.gif)
## Expertise Detection
This service gets list of diseases and give probable expertise that the patient should visit. it can be seperated in UI. [disease-expertise dataset](https://github.com/pouyanhessabi/B.Sc-Final-Project-Healthcare-Microservice/blob/main/services/ai/data/average_result.xlsx)<br>
**Run**: <br>
![](https://github.com/pouyanhessabi/B.Sc-Final-Project-Healthcare-Microservice/blob/main/Report/Gif/Disease%20and%20Expertise%20Prediction.gif)
## Search Physician
This service gets an expertise and give the physicians with particular expertise sorted by user rating. we can use this service from both navigation-bar and previous service.<br>
**Run**: <br>
![](https://github.com/pouyanhessabi/B.Sc-Final-Project-Healthcare-Microservice/blob/main/Report/Gif/Search.gif)

# Implementation Technologies
`Python`, `HTML/CSS/JS`, `Flask`, `XGBoost`, `MySQL`, `Docker` </br>

have fun :)








