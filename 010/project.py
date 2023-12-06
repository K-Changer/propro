import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Excel ���� �б�
excel_file = "MDP_00015_Youtube��û_Ű����_�������ɺ�_Top50_202207.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(excel_file, sheet_name = 0)

# ���� �� ���� ������ ���͸�
men_data = df[df['sex_code'] == 'M']
women_data = df[df['sex_code'] == 'F']

# ���̺��� �׷�ȭ�ϰ� ���� �� ������ ���� �˻��� �� ���
men_terms_count = men_data.groupby('ages')['Search Terms'].value_counts().unstack().fillna(0)
women_terms_count = women_data.groupby('ages')['Search Terms'].value_counts().unstack().fillna(0)

# ���� �˻�� ���� �� ���̾�׷� ����
common_terms = pd.merge(men_terms_count, women_terms_count, on='Age', how='inner')

# �� ���̾�׷� �÷���
plt.figure(figsize=(10, 6))
venn = sns.heatmap(common_terms, annot=True, cmap='YlGnBu', fmt='g') #(��Ʈ�� �ð�ȭ, �ּ� �߰� ����, ���� ����, �ּ� ���� �Ϲ�)
venn.set_title('���� �� ������ ���� ���� �˻���')
plt.show()

# ���� �� ���� �˻��� ���� �ű��
ranked_men_terms = men_data['Search Terms'].value_counts().reset_index()
ranked_men_terms.columns = ['Search Terms', '���� (����)']

ranked_women_terms = women_data['Search Terms'].value_counts().reset_index()
ranked_women_terms.columns = ['Search Terms', '���� (����)']

# ���� �Ű��� �˻��� ǥ��
print("���� �˻��� ����:")
print(ranked_men_terms)

print("\n���� �˻��� ����:")
print(ranked_women_terms)