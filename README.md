
<h1 align="center">
Body_Temperature Monitor_System-AIoT
</h1>


<div align= "center">
  <h4>Body Temperature Monitor System built with Keras/TensorFlow using Deep Learning concepts in order to predict temperature.</h4>
  
</div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/arthur-hui-chung-shen-b58961170)



</div>

## Motivation
Due to cases of COVID-19 ramping up, we have to implement measurements to slow the spread of severe COVID-19. With really convenient Internet and cloud platform nowadays, I would like to use technical skills with combining AI and IoT to assist government to decline the number of cases. This project presents AI concepts as deep learning approach with IoT and edge compute to detect whether your body temperature is higher 37.5 °C. And, if your body temperature is higher 37.5 °C, you will receive the warning notification by your LINE APP.

 



## TechStack used


- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)


##  Dataset

This dataset consists of __70 ADC values and temperatures__

The dataset were collected from the following sources:

* __Myself__



## Features
I have recorded the ADC value responding the specific temperature and I use the temperature as the label and ADC value as train dataset to train model by Convolutional Neural Network on Google Colab. I put the model into ESP32 (Edge Computing) to detect the temperature and upload to CHT IoT to analysis the data. In the end, we use IFTTT to send notification to warn users if their temperature is too high. 

## Results

#### ESP32
![](https://github.com/ArthurShen8118/Body_Temperature_Monitor_System-AIoT/blob/main/Readme_images/2020-10-23%2008%2035%2010.png)
#### IoT
![](https://github.com/ArthurShen8118/Body_Temperature_Monitor_System-AIoT/blob/main/Readme_images/2020-10-23%2008%2040%2055.png)
#### LINE APP
![](https://github.com/ArthurShen8118/Body_Temperature_Monitor_System-AIoT/blob/main/Readme_images/12322.jpg)
## Owner
Made with by [Arthur Hui-Chung Shen](https://github.com/ArthurShen8118)

Email: huichung.shen@gmail.com

