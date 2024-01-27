"""

잘못 입력된 역 정보 추출하기
지하철 데이터를 분석하더 중, 2호선과 4호선 역 이름 데이터에 3호선 데이터가 잘못 기입이 되어 있다는 점을 발견했습니다.

2호선 역 이름 리스트에는 “독립문” 역이, 4호선 역 이름 리스트에는
“잠원”, “대청”, “원흥” “삼송” 역이 잘못 기입이 되어 있습니다.

인덱싱과 슬라이싱을 활용해서, 2호선과 4호선 리스트에 잘못 기입된 3호선 역 이름 추출해봅시다.

"""

# 2호선 역 이름 리스트 15개
line2 = ['동대문역사문화공원','신당','상왕십리','왕십리','한양대','뚝섬','성수','건대입구','구의','강변','잠실나루','*독립문','까치산','시청','을지로입구']

# 2호선 역 이름 리스트에서 3호선 역 이름 정보를 추출해 보겠습니다(3호선 *표시)
#error_line3 = 

# 4호선 역 이름 리스트 15개
line4 = ['충무로','경마공원','쌍문','명동','과천','범계','초지','정부과천청사','안산','오이도','신길온천','*잠원','*대청','*원흥','*삼송']

# 4호선 역 이름 리스트에서 3호선 역 이름 정보들을 추출해 보겠습니다(3호선 *표시)
#error_line3_list =


print("2호선 리스트에 입력된 3호선 역 이름 정보 :", error_line3)
print("4호선 리스트에 입력된 3호선 역 이름 정보 :", error_line3_list)

#-----------------> 풀이 후


# 2호선 역 이름 리스트 15개
line2 = ['동대문역사문화공원','신당','상왕십리','왕십리','한양대','뚝섬','성수','건대입구','구의','강변','잠실나루','*독립문','까치산','시청','을지로입구']

# 2호선 역 이름 리스트에서 3호선 역 이름 정보를 추출해 보겠습니다(3호선 *표시)
error_line3 = line2[-4]

# 4호선 역 이름 리스트 15개
line4 = ['충무로','경마공원','쌍문','명동','과천','범계','초지','정부과천청사','안산','오이도','신길온천','*잠원','*대청','*원흥','*삼송']

# 4호선 역 이름 리스트에서 3호선 역 이름 정보들을 추출해 보겠습니다(3호선 *표시)
error_line3_list = line4[-4:]


print("2호선 리스트에 입력된 3호선 역 이름 정보 :", error_line3)
print("4호선 리스트에 입력된 3호선 역 이름 정보 :", error_line3_list)