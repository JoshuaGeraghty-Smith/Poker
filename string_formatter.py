import re
import csv



with open('poker_lookup_table.txt') as f:
    lines = f.readlines()
    for line in lines:
        line=re.sub("\s+", ",", line.strip())
        line = line.split(",")
        empty_str=""
        for index, item in enumerate(line):
            if index > 4 and index < 10:
                empty_str += item

        del line[5:10]
        line.insert(5,empty_str)
        empty_str=""
        for index, item in enumerate(line):
            if index > 6:
                empty_str += item

        del line[7:]
        line.append(empty_str)





        line = ",".join(line)
        print(line)


