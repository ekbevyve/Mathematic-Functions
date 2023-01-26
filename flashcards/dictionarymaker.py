#make a dictionary
"""
fuction makes a dictionary from a csv file.
"""
def makeadict(filename):
    import csv
    #initializing variables, opening files
    file = open(filename, 'r')
    table ={}
    reader = csv.reader(file)
    for row in reader:
        #append dictionary with the key and data
        table[row[0]]=row[1]
    return table
#testing function
dictionary=makeadict('file.txt')
print(dictionary)
