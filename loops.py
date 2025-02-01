# list -> data structure which can hold mutiple vales of multiple type 
# Arrays -> data structure can hold multiple values of same type

list_of_cloud = ["aws","azure","gcp","alibaba","oracle","digital ocean","utho"]
cloud = "aws" # variables
print(list_of_cloud)

# add a new cloud salesforce
list_of_cloud.append("Salesforce")

# add a new cloud IBM 
list_of_cloud.append("IBM") # adds to the ends of list

print(list_of_cloud)

list_of_cloud.insert(6,"Heroku")

print(list_of_cloud)

print(len(list_of_cloud))

list_of_cloud.insert(0,"Hello Cloud")
print(list_of_cloud)

# Itreation in a list
for cloud in list_of_cloud:
    print(" ")
    print(cloud)

for i in range(1,11):
    print(i)    