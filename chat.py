# 對話紀錄改寫練習

# 讀取檔案
with open('input.txt', 'r', encoding = 'utf-8') as f:
	record = []
	for line in f:
		record.append(line.strip())

# 主要程式
out_record = []
i = 0
top = 'Clay'

while i < len(record):	
	if 'Allen' in record[i]:
		top = 'Allen: '
		i += 1
		continue
	if 'Tom' in record[i]:
		top = 'Tom: '
		i += 1
		continue
	out_record.append(top + record[i])
	i += 1

print(out_record)

# 寫入檔案
with open('output.txt', 'w', encoding = 'utf-8') as f:
	for out in out_record:
		f.write(out + '\n')