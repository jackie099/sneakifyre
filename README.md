# SneakiFyre Android App

## Introduction
Android application that uses image recognition to classify a shoe and return its name,price, and highest bid. The application will only display the shoe if it is above a certain confidence level (.4-.6). Clicking on the buttons will redirect the user to https://www.stockx.com/<shoe name> so that they could buy/sell the shoe. 
## Specifications

- Using [TensorFlow Lite for Android](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/lite/java/demo)
- Using [TensorFlow](https://github.com/tensorflow/tensorflow) to train sneaker detection model
- Using StockX RESTful API for shoe data

## Authors
- Zhenghui Li
- Kevin Kye
