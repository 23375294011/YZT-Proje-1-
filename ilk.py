import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv(r'C:\Users\Bruger\Documents\yzt proje kampı\basket_details.csv')
df2=pd.read_csv(r'C:\Users\Bruger\Documents\yzt proje kampı\customer_details.csv')

df_merged=pd.merge(df,df2,on="customer_id",how="left")

print(df_merged.head())
print(df_merged.info())
print(df_merged.describe())
print(df_merged.columns)


print("\nTop 10 Müşteri (Basket sayısı):")
print(df_merged['customer_id'].value_counts().head(10))

print("\nTop 10 Ürün:")
print(df_merged['product_id'].value_counts().head(10))

print("\nTop 10 Sepet Tarihi:")
print(df_merged['basket_date'].value_counts().head(10))

print("\nTop 10 Sepet Sayısı:")
print(df_merged['basket_count'].value_counts().head(10))

print("\nCinsiyet Dağılımı:")
print(df_merged['sex'].value_counts().head(10))

numeric_df=df_merged.select_dtypes(include=[np.number])
for column in numeric_df.columns:
    mean_val=np.mean(numeric_df[column])
    std_val = np.std(numeric_df[column])
    var_val = np.var(numeric_df[column])
    print(f"\n {column} sütunu için istatistikler:")
    print(f"  Ortalama: {mean_val:.2f}")
    print(f"  Standart sapma: {std_val:.2f}")
    print(f"  Varyans: {var_val:.2f}")
df_merged['basket_date'] = pd.to_datetime(df_merged['basket_date'])
top_products= df_merged.groupby("product_id")["basket_count"].sum().sort_values(ascending=False).head(10)
top_products.plot(kind="bar",figsize=(10,6),color="skyblue")
plt.title("En Popüler 10 Ürün")
plt.xlabel("Ürün ID")
plt.ylabel("Satış Adedi")
plt.show()

plt.figure(figsize=(6,4))
df_merged['sex'].value_counts().plot(kind='bar', color='purple')
plt.title("Cinsiyete Göre Kullanıcı Dağılımı", fontsize=14)
plt.xlabel("Cinsiyet")
plt.ylabel("Kullanıcı Sayısı")
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df_merged["basket_count"], bins=10, color='orange', edgecolor="black")
plt.title("Sepet Sayısı Dağılımı", fontsize=14)
plt.xlabel("Sepet Sayısı")
plt.ylabel("Frekans")
plt.show()

print("\n Rapor Özeti:")
print(f"Toplam Satır Sayısı: {len(df_merged)}")
print(f"Toplam Müşteri Sayısı: {df_merged['customer_id'].nunique()}")
print(f"Toplam Ürün Sayısı: {df_merged['product_id'].nunique()}")
print(f"Toplam Sepet Sayısı: {df_merged['basket_count'].sum()}")
print(f"En Popüler Ürün ID: {top_products.idxmax()}")