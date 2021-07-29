assignlist = [1, 5, 8, 5, 210, 87]
r_item = 210
print("original list")
print(assignlist)


for item in assignlist:
	if(item==r_item):
		assignlist.remove(r_item)
print("updated list")
print(assignlist)