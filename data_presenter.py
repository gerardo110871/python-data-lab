#2
#we open the file using open('') name of the file inside the quotes
open_file = open('CupcakeInvoices.csv')
#3
# this will print all the items in the file
# for row in open_file:
#     print(row)
#4
# this prints out the item in index 2 which is the flavor of the cupcake
# for row in open_file:
#     flavor = row.split(',')
#     print(flavor[2])
#5
# this loop prints the total for each invoice seperately
# for row in open_file:
#     items = row.split(',')
#     total = int(items[3]) * float(items[4])
#     print(total)
#6
# now to add all the totals in all the invoices we need to make a new variable to store
# them and each iteration will add the total amount storing it into the total variables
# then adding that amount to the total of the next invoice and so forth
# total = 0

# for row in open_file:
#   items = row.split(',')
#   total = total + (int(items[3]) * float(items[4]))

# print(total)

#7
open_file.close()