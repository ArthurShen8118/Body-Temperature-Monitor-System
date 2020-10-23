


import keras_lite_convertor as kc

path_name = 'temperature.txt'

Data_reader = kc.Data_reader(path_name, mode='regression')

data, label = Data_reader.read()

split_num = int(len(data)*0.85) 
train_data=data[:split_num]
train_label=label[:split_num]    


mean = train_data.mean() 
data -= mean
std = train_data.std()   
data /= std

label /= 100     


print(train_data.shape)    


validation_data = data[split_num:-5]    
print(validation_data.shape)
validation_label = label[split_num:-5]   

test_data = data[-5:]     
print(test_data.shape)
test_label = label[-5:]



from tensorflow.keras.models import Sequential
from tensorflow.keras import layers

model = Sequential()
model.add(layers.Dense(20,activation = 'relu', 
                       input_shape=(1,)))  
model.add(layers.Dense(20,activation = 'relu'))
model.add(layers.Dense(20,activation = 'relu'))
model.add(layers.Dense(1))
model.summary()    



model.compile(optimizer='adam',loss='mse',metrics=['mae'])
train_history = model.fit(train_data,train_label,            
                          validation_data=(validation_data,validation_label),  
                          epochs=1000)   



print('predict:')
print(model.predict(test_data))
print()

print('real:')
print(test_label)


kc.save(model,'temperature_model.json')



print('mean=',mean)
print('std=',std)

