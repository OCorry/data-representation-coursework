from requestsLab import readbooks

books = readbooks()
total = 0 
count = 0
for book in books:
    total +=book['Price']
    count+= 1 
    average = round(total/count, 2)
print('the average price of', count, 'books is',average)