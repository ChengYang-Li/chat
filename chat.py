# 對話紀錄改寫練習

# 讀取檔案
def read_file(filename):
	record = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 用utf-8-sig去掉 "\ufeff"
		for line in f:
			record.append(line.strip())
	return record

# 格式轉換
def transfer(record):
	# out_record = []
	# i = 0
	# top = '未知'
	# while i < len(record):	
	# 	if 'Allen' in record[i]:
	# 		top = 'Allen'
	# 		i += 1
	# 		continue
	# 	elif 'Tom' in record[i]:
	# 		top = 'Tom'
	# 		i += 1
	# 		continue
	# 	out_record.append(top + ': ' + record[i])
	# 	i += 1
	# return out_record
	out_record =[]
	person = '未知'
	for line in record:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		out_record.append(person + ': ' + line)
	return out_record
	# out_record =[]
	# person = None
	# for line in record:
	# 	if line == 'Allen':
	# 		person = 'Allen'
	# 		continue
	# 	elif line == 'Tom':
	# 		person = 'Tom'
	# 		continue
	# 	if person:
	# 		out_record.append(person + ': ' + line)
	# return out_record

# 寫入檔案
def write_file(filename, out_record):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for out in out_record:
			f.write(out + '\n')

# 主要程式
def main():
	record = read_file('input.txt')
	out_record = transfer(record)
	write_file('output.txt', out_record)

if __name__ == '__main__':
	main()