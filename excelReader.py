import openpyxl

wb = openpyxl.load_workbook('Image Caption Papers.xlsx')

## sheet1
sheet1 = wb.worksheets[2]
paperList = []
# 遍历
for row in sheet1.iter_rows():
    ## 定义变量
    paper = None
    meeting = None
    year = None  
    title = None  
    author = None
    pdfLink = None 
    codeLink = None
    counter = 0

    for cell in row:
        if counter == 0 and (cell.value == None  or cell.value == '会议'):
            # 无效数据，跳出循环
            break
        
        # 读取单元格
        # print(cell.coordinate, cell.value)
        if counter == 0:
            meeting = cell.value.strip()
        elif counter == 1:
            year = int(cell.value)
        elif counter == 2:
            title = cell.value.strip()
        elif counter == 3:
            author = cell.value.strip()
        elif counter == 4:
            # 标记
            pass 
        elif counter == 5:
            pdfLink = cell.value.strip() if cell.value != None else ''
        elif counter == 6:
            codeLink = cell.value.strip() if cell.value != None else ''
        elif counter == 7:
            # 备注
            pass
        else:
            break
    
        counter += 1

    # 处理数据
    if meeting != None:
        paperStr = '- **%s.** *%s*  [[pdf](%s)] [[code](%s)]' % (title, author, pdfLink, codeLink)
        paper = {'year': year, 'meeting': meeting, 'paperStr': paperStr}
        # print(paper)
        paperList.append(paper)




# 按照年份排序
def quickSort(paperList, left, right):
    '''
        根据paperList的年份进行快排
    '''
    if left < right:
        position = partition(paperList, left, right)
        quickSort(paperList, left, position - 1)
        quickSort(paperList, position + 1, right)

def partition(paperList, left, right):
    i = left
    j = left
    while j <= right:
        if paperList[j]['year'] >= paperList[left]['year']:
            j += 1
        else:
            i += 1
            temp = paperList[i]
            paperList[i] = paperList[j]
            paperList[j] = temp 
            j += 1 
    temp = paperList[left]
    paperList[left] = paperList[i]
    paperList[i] = temp 
    return i 


# 年份排序
length = len(paperList)
quickSort(paperList, 0, length - 1)
# for paper in paperList: print(paper)

yearList = [2021, 2020, 2019, 2018]
meetingList = ['CVPR', 'AAAI', 'ACMM', 'ACCV', 'IJCAI', 'ICCV', 'ECCV', 'NeurIPS']
for iYear in yearList: 
    print()
    print()
    print(iYear)
    for iMeeting in meetingList:
        print() 
        print(iMeeting)
        k = length - 1
        while k >= 0:
            paper = paperList[k]
            if paper['year'] == iYear and paper['meeting'] == iMeeting:
                print(paperList[k]['paperStr'])
            k -= 1





# k = length - 1
# while k >= 0:
#     paper = paperList[k]
#     if paper['year'] == 2019 and paper['meeting'] == 'NeurIPS': 
#         pass
#         # print(paperList[k]['paperStr'])
#         # print(paperList[k])
#     k -= 1
