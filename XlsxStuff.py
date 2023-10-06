import openpyxl
workbook = openpyxl.Workbook()
worksheet = workbook.active
readbook = openpyxl.load_workbook(filename = 'mobile games.xlsx')
sheetread = readbook["mobile_game_ratings"]
ar={}
arr=[]
for i in range(3,33):
    ar[float(sheetread['B'+str(i)].value)]= sheetread['A'+str(i)].value
    arr.insert(0, float(sheetread['B'+str(i)].value))
arr.sort(reverse=True)
for i in range(30):
    worksheet['A'+str(i+1)]=ar[arr[i]]
    worksheet['B'+str(i+1)]=arr[i]
workbook.save('mobile games NEW.xlsx')