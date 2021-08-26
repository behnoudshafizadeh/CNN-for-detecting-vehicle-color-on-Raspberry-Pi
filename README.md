# CNN-for-detecting-vehicle-color-on-Raspberry Pi
using CNN classifier to recognize the color of vehicle

## Overall Discription
as mentioned before in detecting color vehicle using CNN [link](https://github.com/behnoudshafizadeh/vehicle-color-recognition-using-CNN-model), we employ this project on our raspberry Pi Hardware to see the usablity of CNN in real world application.

![our raspberry pi](https://user-images.githubusercontent.com/53394692/130974671-99f06822-b3e3-47fd-8b53-3eed82b0932f.png)

## Requirements
as see before, we install requirements to `ALPR` task, for implementing vehicle color detection we need to install `compatible tensorflow` in our raspberry Pi, so for installing, you must download `.whl` files basis on `tensorflow version 2.4` to run deep learning structure, such as below (download these files and then install them) :

![suitable  whl file](https://user-images.githubusercontent.com/53394692/130968667-e4b15d4e-ea53-4555-8c8e-48d1999ac4d0.PNG)

and then isntall `keras` and `tensorflow` similar to following instructions :

![how to install tensorflow and keras on raspberry pi](https://user-images.githubusercontent.com/53394692/130968965-1fc317d1-6d4a-40af-89cf-f912467c5289.png)

## Environment
you see following figure which shows the contents of this project discussed in below :
```
input directory : input images
1.jfif,2.jfif : cropped vehicle from input image (input of algorithm)
color_model.h5 : weight of CNN classifier (trained before)
color_prediction.ipynb : (.ipynb) file for predicting color
predict.py : (.py) file used to predict color

```
![color detection folder](https://user-images.githubusercontent.com/53394692/130970905-7d3b60aa-9f35-4f0c-9825-b581e0a4800e.png)

## Test
for implementing CNN model, we use `python predict.py` to show the results :
(Notice : we use `IMAGE AI` in this [link](https://github.com/behnoudshafizadeh/IMAGE-AI_extracting-vehicle-from-image) in starting point to extract vehicles.)
and see the results in below :

![result of color detection](https://user-images.githubusercontent.com/53394692/130971043-ca3f96b4-46cf-42fe-aef9-7bf73c2622b4.PNG)
























