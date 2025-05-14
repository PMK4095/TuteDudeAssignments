#task 10
og=[]
for i in range(1,11):
    og.append(i)
print("Original list: {}".format(og))
extracted=og[0:5]
print("Extracted first five elements: {}".format(og[0:5]))
print("Reversed extracted elements: {}".format(extracted[::-1]))
