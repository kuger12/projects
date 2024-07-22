import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""this code classes iris flowers based on the sepales 
and petales on 3 clsses iris-setosa  ,iris-versicolor  ,iris-virginica
"""

# it s just a function to visualize the data set , just skip it
def data_visualisation() : 
    df = pd.read_csv("/home/yassine/Desktop/unreal/bezdekIris.data" , names = ["sepal_lenght" , "sepal_width" , "petal_lenght" , "petal_width" , "type"])


    k1 = df[df["type"] == "Iris-setosa"].filter(items = ["sepal_lenght" , "sepal_width"])
    k2 = df[df["type"] == "Iris-versicolor"].filter(items = ["sepal_lenght" , "sepal_width"])#.plot(kind = "scatter" , x="sepal_lenght" , y = "petal_lenght" , c = "red")
    k3 = df[df["type"] == "Iris-virginica"].filter(items = ["sepal_lenght" , "sepal_width"])#.plot(kind = "scatter" , x="sepal_lenght" , y = "petal_lenght" , c = 'green')

    plt.scatter(k1["sepal_lenght"] , k1["sepal_width"] , s = 10)
    plt.scatter(k2["sepal_lenght"] , k2["sepal_width"] , s = 10)
    plt.scatter(k3["sepal_lenght"] , k3["sepal_width"] , s = 10)


    plt.show()



# Extracting data
df = pd.read_csv("/home/yassine/Desktop/unreal/bezdekIris.data" , names = ["sepal_lenght" , "sepal_width" , "petal_lenght" , "petal_width" , "espece"])


rows = np.array([np.array(df[["sepal_lenght" , "sepal_width", "petal_lenght" , "petal_width" ]].loc[x] , dtype= float) for x in range(150)])


vector = np.array([5.9, 3. , 5.1, 1.8])

#The formula of calculating the distance
n_rows = (rows - vector)**2
n_rows = np.sum(n_rows , axis = 1)
n_rows = np.sqrt(n_rows)


#column represanting distances
df["distance"] =  n_rows

#changeable
k = 7

# sort distances
df.sort_values(by = 'distance' , inplace= True)

# get the 7 first distances
typ_count = df.head(k).value_counts(subset= "espece")



print("prediction is : ")


#Not the best way to do this , but it sees the class that has the highest number and pick it as an espece
if len(typ_count.index) == 1 :
    print(typ_count.index[0])

elif len(typ_count.index) == 2 : 
    if typ_count[typ_count.index[0]] > typ_count[typ_count.index[1]] :
        print(typ_count.index[0])
    else :
        print(typ_count.index[1])
else :
        if typ_count[typ_count.index[0]] > typ_count[typ_count.index[1]] and typ_count[typ_count.index[0]] > typ_count[typ_count.index[2]] :
           print(typ_count.index[0])
        
        elif typ_count[typ_count.index[1]] > typ_count[typ_count.index[0]] and typ_count[typ_count.index[1]] > typ_count[typ_count.index[2]] :
           print(typ_count.index[1])
        
        else :
            print(typ_count.index[2])

