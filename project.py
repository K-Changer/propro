import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
# Excel 파일 읽기
excel_file = "./MDP_00015_Youtube시청_키워드_성별연령별_Top50_202207.xlsx"
# sheet_name = "Sheet1"
df = pd.read_excel(excel_file, sheet_name = 0)

# 남성 및 여성 데이터 필터링
men_data = df[df['sex_code'] == 'M']
women_data = df[df['sex_code'] == 'F']
print(men_data)

# 나이별로 그룹화하고 남성 및 여성의 고유 검색어 수 계산
men_terms_count = men_data.groupby('ages')['Search Terms'].value_counts().unstack().fillna(0)
women_terms_count = women_data.groupby('ages')['Search Terms'].value_counts().unstack().fillna(0)

# 공통 검색어에 대한 벤 다이어그램 생성
common_terms = pd.merge(men_terms_count, women_terms_count, on='Age', how='inner')

# 벤 다이어그램 플로팅
plt.figure(figsize=(10, 6))
venn = sns.heatmap(common_terms, annot=True, cmap='YlGnBu', fmt='g') #(히트맵 시각화, 주석 추가 여부, 색상 설정, 주석 설정 일반)
venn.set_title('나이 및 성별에 따른 공통 검색어')
plt.show()

# 남성 및 여성 검색어 순위 매기기
ranked_men_terms = men_data['Search Terms'].value_counts().reset_index()
ranked_men_terms.columns = ['Search Terms', '순위 (남성)']

ranked_women_terms = women_data['Search Terms'].value_counts().reset_index()
ranked_women_terms.columns = ['Search Terms', '순위 (여성)']

# 순위 매겨진 검색어 표시
print("남성 검색어 순위:")
print(ranked_men_terms)

print("\n여성 검색어 순위:")
print(ranked_women_terms)