# Promosyonlar Rossmann satışlarını ne kadar artırıyor?

Rossmann mağaza verisiyle hazırlanmış, kaydırdıkça ilerleyen interaktif bir veri hikâyesi (scrollytelling) projesi.

**Çalışma sorusu:** Rossmann mağazalarındaki promosyonlar günlük satışları gerçekten ne kadar artırıyor ve bu etki her mağaza tipinde aynı mı?

**Canlı site:** _(site yayınlandığında eklenecek)_

## Kısa bulgular

- Aynı gün tipinde (hafta içi) karşılaştırıldığında, promosyonlu günlerde ortalama günlük satış yaklaşık %39 daha yüksek.
- İncelenen 1.115 mağazanın hiçbirinde promosyonlu günlerde satış düşmedi; artış mağazadan mağazaya yaklaşık %2 ile %102 arasında değişiyor.
- Artış mağaza tipine göre farklı: a, c ve d tiplerinde yaklaşık %38–42, b tipinde (yalnızca 17 mağaza) yaklaşık %20.
- Bu sonuçlar bir **ilişkiyi** gösterir; promosyonun tek başına nedeni olduğunu kanıtlamaz.

## Veri kaynağı ve lisans

- Kaynak: Kaggle, *Rossmann Store Sales* — https://www.kaggle.com/competitions/rossmann-store-sales
- Erişim tarihi: 10 Ekim 2026
- Lisans / kullanım koşulları: _(Kaggle *Rules* sayfasındaki koşullar buraya yazılacak)_
- Ham veri bu depoda yer almaz; `data/raw/README.md` içindeki bağlantıdan indirilir.

## Depo yapısı

```
├── README.md
├── data/
│   ├── raw/          (ham veriye bağlantı)
│   └── processed/    (özet veriler)
├── notebooks/
│   └── analiz.ipynb  (temizleme, analiz, özet dosyaların üretimi)
├── site/             (scrollytelling sitesi)
└── docs/             (storyboard)
```

## Projeyi yerelde çalıştırma

1. Ham veriyi Kaggle'dan indirin ve `train.csv` ile `store.csv` dosyalarını `data/raw/` klasörüne koyun.
2. `notebooks/analiz.ipynb` dosyasını Jupyter veya Google Colab'da açın.
3. Colab'da çalıştırıyorsanız iki dosyayı oturuma yükleyin; yerelde çalıştırıyorsanız `RAW` ve `OUT` yollarını `Path('../data/raw')` ve `Path('../site/data')` olarak ayarlayın.
4. *Restart & Run All* ile baştan sona çalıştırın. Özet dosyalar `site/data/` içinde üretilir.

## Kullanılan kütüphaneler

Python 3, pandas, numpy. _(Site için kullanılan kütüphaneler eklenecek.)_

## Kullanılan kod kaynakları

_(Site geliştirilirken kullanılan açık kaynak kütüphaneler ve örnekler burada belirtilecek.)_

## Yapay zekâ kullanım beyanı

Bu projede **Claude (Anthropic)** yapay zekâ asistanı kod yazma desteği, hata ayıklama, storyboard çizimlerinin hazırlanması ve proje yapısının düzenlenmesi için kullanılmıştır. Analiz bulgularının yorumları ve hikâye metinleri öğrenciye aittir.

## Yazar

Beril Özdizdar — Manisa Celal Bayar Üniversitesi, Büyük Veri Analistliği
GitHub: [Beril-ozdr](https://github.com/Beril-ozdr)
