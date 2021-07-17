# 對話紀錄改寫練習2

# 讀取檔案
def read_file(filename):
	record = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 用utf-8-sig去掉 "\ufeff"
		for line in f:
			record.append(line.strip())
	return record


# 格式轉換
def transfer(record):
	count_allen = 0
	sticker_allen = 0
	picture_allen = 0
	count_viki = 0
	sticker_viki = 0
	picture_viki = 0
	for line in record:
		line = line.split(' ')
		time = line[0]
		name = line[1]
		if name == 'Allen':
			# for i in range(2, len(line)):
			# 	count_allen += len(line[i])
			if line[2] == '貼圖':
				sticker_allen +=1
			elif line[2] == '圖片':
				picture_allen += 1
			else:
				for i in line[2:]:
					count_allen += len(i)
		elif name == 'Viki':
			# for i in range(2, len(line)):
			# 	count_viki += len(line[i])
			if line[2] == '貼圖':
				sticker_viki +=1
			elif line[2] == '圖片':
				picture_viki += 1
			else:
				for i in line[2:]:
					count_viki += len(i)
	print('Allen說了:', count_allen)
	print('Viki說了:', count_viki)
	print('Allen貼圖:', sticker_allen)
	print('Viki貼圖:', sticker_viki)
	print('Allen圖片:', picture_allen)
	print('Viki圖片:', picture_viki)


# 寫入檔案
def write_file(filename, out_record):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for out in out_record:
			f.write(out + '\n')


# 主要程式
def main():
	record = read_file('LINE-Viki.txt')
	out_record = transfer(record)
	#write_file('output.txt', out_record)


if __name__ == '__main__':
	main()