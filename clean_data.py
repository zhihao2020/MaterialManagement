import csv
import re
old_file = r"D:\wuzi\refer\库存store.txt"
new_file = r"D:\wuzi\material\laobao_store.csv"
with open(old_file,"r",encoding="gb18030",errors="ignore") as fd:
    content = fd.readline()
    
    while content:
        #print(content)
        input_content = content.split("\t")
        with open(new_file,'a',encoding='utf-8',errors="ignore") as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(input_content)
        
        content = fd.readline()
        #fd.next()
        
