#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import load_model
from keras.preprocessing import image
import numpy as np


# In[2]:


img_width, img_height = 224, 224
CATEGORIES=['beige','black','blue', 'brown', 'gray' ,'green', 'orange','red', 'silver', 'white','yellow']


# In[3]:


model = load_model('color_model.h5')


# In[8]:


test_image = image.load_img('1.jfif', target_size=(img_width, img_height,3))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
test_image = test_image.reshape(1,img_width, img_height,3)    
result = model.predict_classes(test_image, batch_size=1)
print("this car is:", CATEGORIES[result[0]])


# In[ ]:




