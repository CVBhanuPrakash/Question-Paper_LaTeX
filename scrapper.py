from posixpath import split
import re
import pandas as pd
data = open('test.tex').read()
final_csv = []
stringg = re.findall(r'\%question_start(.*?)\%question_end', data, re.S)
for i in range(0,len(stringg)):
    string = re.sub('\n', '', stringg[i])
    # split_string = re.findall('}\n{', string, re.S)
    # split_string = re.findall(r'%#', string, re.S)
    split_string = re.split(r'[%#]', string)
    # print(string)
    new_list = [x for x in split_string if x != '']
    if len(new_list)>=6:
        question_num = new_list[1]
        question_num = question_num[1:-1]
        question =new_list[2]
        question = question[1:-1]
        opt1 = new_list[3]
        opt1 = opt1[1:-1]
        opt2 = new_list[4]
        opt2 = opt2[1:-1]
        opt3 = new_list[5]
        opt3 = opt3[1:-1]
        opt4 =new_list[6]
        opt4 = opt4[1:-1]
        list_final = [question_num,question,opt1,opt2,opt3,opt4]
        final_csv.append(list_final)
        # for x in new_list:
        # print(question_num)
        # print(question)
        # print(opt1)
        # print(opt2)
        # print(opt3)
        # print(opt4)
df_final = pd.DataFrame(final_csv, columns = ['Question Number', "Question", "Option 1","Option 2","Option 3","Option 4"])
print(df_final)
df_final.to_csv('questions.csv')