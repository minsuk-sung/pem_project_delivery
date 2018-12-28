'''
	PEM Delivery Project
	Parsing Code
	Python Ver : Python 3.6.5

	input_data 폴더에 있는 txt파일에 대해서 개행 전까지 읽은 한줄의 텍스트를 읽고
	output_data 폴더에 파싱한 결과를 입력하자
'''

# 파싱할 입력 데이터의 경로
INPUT_DATA_ROUTE = './input_data/result.txt'
# 파싱할 출력 데이터의 경로
OUTPUT_DATA_ROUTE = './output_data/result_'
# 파일 번호
fileno = 0

# 입력 데이터 스트림 열기
input_f = open(INPUT_DATA_ROUTE, mode='rt', encoding='euc-kr')

# 입력 데이터의 끝까지 수행
while True:
    # 각 데이터에 대해서 개행문자 전까지 읽어오기
	route = input_f.readline()
	# 끝을 만난다면 루프 탈출
	if not route:
		break
	print('='*50)
	print(str(fileno)+'번째 경로')
	print('='*50)
	print(route)
	
	output_f = open(OUTPUT_DATA_ROUTE+str(fileno)+'.csv','w',encoding='utf-8')
	output_f.write(route)
	fileno += 1
	output_f.close()

# 입력 데이터 스트림 닫기
input_f.close()