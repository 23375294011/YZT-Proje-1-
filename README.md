# YZT-Proje-1-
E-ticaret satış veri analizi projesi
Proje Amacı:
Bu proje, e-ticaret veri setini analiz ederek satış performansını, popüler ürünleri ve müşteri bilgilerini anlamayı amaçlamaktadır. Analiz sonucunda “hangi ürüne odaklanmalı” ve “müşteri kitlesi hakkında bilgiler” gibi öngörüler sunulmuştur.

1️⃣ Veri Seti ve Ön İşleme

Veri setleri: basket_details.csv ve customer_details.csv

İki veri seti customer_id üzerinden birleştirildi (left join).

basket_count ve Price sütunları kullanılarak Revenue (gelir) hesaplandı.

basket_date sütunu tarih formatına dönüştürüldü.

2️⃣ Temel Analiz Bulguları
a) Müşteri Dağılımı

Toplam müşteri sayısı: X

Cinsiyete göre dağılım:

Erkek: Y

Kadın: Z

b) Sepet ve Satış Bilgileri

Toplam sepet sayısı: T

Ortalama sepet başına ürün sayısı: A

Sepet sayısı dağılımı histogram ile görselleştirildi.

c) En Popüler Ürünler

Top 10 ürün (satış adedi bazında):

Ürün ID	Toplam Satış Adedi
…	…

En çok gelir getiren ürün: Ürün ID: X

💡 Öneri: Şirket bu ürüne odaklanmalı, reklam ve stok yatırımı artırılabilir.

d) Zaman Trendleri

Sepet tarihleri incelenerek aylık satış trendi gözlemlendi.

Gelir artış/düşüşleri grafik ile gösterildi (isteğe bağlı matplotlib kullanımı).

3️⃣ Görselleştirmeler

En Popüler 10 Ürün – Bar grafiği

Cinsiyete Göre Kullanıcı Dağılımı – Bar grafiği

Sepet Sayısı Dağılımı – Histogram

(Grafikler Jupyter/Matplotlib ile oluşturulmuştur.)

4️⃣ Özet ve Öneriler

Hangi ürüne odaklanmalı: En çok gelir getiren ürün, şirket için öncelikli.

Müşteri hedefleme: Cinsiyet ve sepet sayısı analizlerine göre reklam ve kampanyalar optimize edilebilir.

Stok ve reklam: Popüler ürünler için öncelikli stok ve pazarlama yatırımı önerilir.

Kampanya fırsatları: Daha az satan ürünler için bundle ve indirim kampanyaları planlanabilir.
