# Change these numbers and run to predict species!

mystery_penguin_flipper = int(input("Enter flipper size : "))
mystery_penguin_bill = int(input("Enter bill size : "))

# The model will use those values and the dataset to predict a species
from code import predict
predict(mystery_penguin_flipper,mystery_penguin_bill)
