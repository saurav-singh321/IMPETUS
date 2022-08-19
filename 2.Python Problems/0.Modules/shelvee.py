import shelve
shv = shelve.open('hello')
# shv['name'] = 'saurav'
# shv['age'] = 20
# shv['city'] = 'Indore'
# shv.close()

print(shv.get('name'))
print(list(shv.items()))
print(list(shv.keys()))
print(list(shv.values()))
shv.pop('city')
print(list(shv.items()))
dict1 = {"profession":"student","sports":"football"}
shv.update(dict1)
print(list(shv.items()))
shv.close()

