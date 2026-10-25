# Steam Pazar Panosu

Manisa’da kurulmuş kurgusal bir bağımsız oyun stüdyosunun yapımcısı için hazırlanmış canlı veri panosu: yeni oyunu hangi türde ve hangi fiyatla çıkarmalı?

**Canlı adres:** https://beril-ozdr.github.io/steam-pazar-panosu/

Bu proje, Büyük Veri Analistliği programı Kullanıcı Arayüzü Tasarımı dersi dönem ödevidir (Beril Özdizdar).

## Ne yapar?

- Steam’deki en çok oynanan 100 oyunu fiyat, tür ve anlık oyuncu sayısıyla gösterir.
- Fiyat × oyuncu sayısı grafiğinde fareyle bir alan seçince KPI kartları, tür grafiği ve tablo seçime göre güncellenir (koordineli görünümler).
- Türe göre medyan fiyatı gösterir.
- Tür, en yüksek fiyat ve ücretsiz oyunlar için filtre sunar; tablo sütunlarına göre sıralanır.

## Veri kaynakları ve veri hattı

| Kaynak | Ne için | Anahtar |
|---|---|---|
| [SteamSpy API](https://steamspy.com/api.php) | Oyun listesi, fiyat, tür, olumlu/olumsuz oy | Gerekmez |
| [Steam Web API](https://developer.valvesoftware.com/wiki/Steam_Web_API) | Anlık oyuncu sayısı | Gerekmez |

`.github/workflows/update-data.yml` iş akışı her gün çalışır, `scripts/fetch_data.py` ile veriyi çeker ve `data/latest.json` dosyasını günceller. Aynı çalıştırma `data/history.csv` dosyasına bir özet satırı ekler; böylece kaynaklar geçmiş vermese bile kendi zaman serimizi biriktiririz. Çekim başarısız olursa mevcut veriye dokunulmaz, pano son başarılı veriyle açılır ve “Son güncelleme” zamanı her zaman ekranda görünür.

## Depo yapısı

```
index.html                    # pano arayüzü (D3.js)
scripts/fetch_data.py         # veri toplama
data/latest.json              # arayüzün okuduğu veri (bot günceller)
data/history.csv              # çalıştırma başına özet
.github/workflows/update-data.yml
```

## Yerelde çalıştırma

```
python scripts/fetch_data.py
python -m http.server 8000
```

Ardından tarayıcıda `localhost:8000` adresini açın. `index.html` dosyasını çift tıklayarak açmak çalışmaz, çünkü tarayıcılar yerel dosyadan veri okumayı engeller.

## Tasarım kararları

- **Koyu tema:** Uzun süre bakılan bir pano için göz yormayan, geceleri de rahat okunan bir yüzey.
- **Oyun estetiği yalnızca başlıkta:** Piksel yazı tipi sadece başlıkta kullanıldı; rakamlar ve metinler okunaklı bir yazı tipinde.
- **Tek ana grafik:** Saçılım grafiği sayfanın merkezinde; tür grafiği ve tablo onu destekliyor.
- **Dayanıklılık:** Yükleniyor, hata ve boş durumları ayrı tasarlandı; sunucuya ulaşılamazsa son kayıtlı veri gösterilir ve kullanıcı bilgilendirilir.

## Erişilebilirlik

- Filtreler, sıralama ve “Seçimi temizle” klavyeyle kullanılabilir; odak halkası görünür.
- Grafiklerin altında özet cümleler var; tür grafiği için “Veriyi tablo olarak gör” seçeneği bulunur.
- Renk tek başına anlam taşımaz: seçili noktalar büyür ve çerçeve alır.
- Fırçayla seçim fareye dayalıdır; klavye kullanıcıları için aynı soruları cevaplayan filtreler sunuldu.

## Bilinen sınırlılıklar

- Bir oyunun türü, kaynağın verdiği **ilk tür etiketidir**; çok türlü oyunlar tek türe indirgenir. Oyun sayısı az olan türlerin medyanı bu yüzden yanıltıcı olabilir.
- Steam anlık oyuncu sayısı vermeyen oyunlar sıfır görünür.
- Fiyatlar ABD doları cinsindendir.
- Oyun adları kaynaktaki hâliyle gösterilir; kaynak eski adı kullanıyor olabilir.
- Veri yaklaşık günlük güncellenir, anlık değildir.

## Kullanıcı testi

2 kişiyle, her biri 3 görevle yapılacak test. *(Testten sonra doldurulacak.)*

| Katılımcı | Görev | Başarılı mı? | Gördüğüm sorun | Yaptığım düzeltme |
|---|---|---|---|---|
| 1 | | | | |
| 1 | | | | |
| 1 | | | | |
| 2 | | | | |
| 2 | | | | |
| 2 | | | | |

Önce/sonra ekran görüntüleri: *(eklenecek)*

## Ölçümler

| Ölçüm | Hedef | Sonuç | Tarih |
|---|---|---|---|
| Lighthouse mobil erişilebilirlik | ≥ 90 | 100 | 25 Ekim 2026 |
| Lighthouse mobil performans | ≥ 80 | 89 | 25 Ekim 2026 |
| Görünüm 360 px ve 1440 px | Sorunsuz | İkisinde de düzgün | 25 Ekim 2026 |

## Yapay zekâ kullanım beyanı

Bu projede **Claude (Anthropic)** yapay zekâ asistanı kullanıldı.

**Yapay zekânın katkısı:**
- `scripts/fetch_data.py` ve `.github/workflows/update-data.yml` dosyalarının ilk taslağı,
- `index.html` arayüz kodunun ilk taslağı ve koyu tema düzenlemesi,
- GitHub’a yükleme adımlarında yönlendirme ve bu README’nin ilk taslağı.

**Benim yaptıklarım:**
- Ödev kartlarını okuyup projenin kapsamını ve kullanılacak veri kaynaklarını belirledim.
- Tasarım yönünü (koyu zemin, şık ve modern görünüm) ben belirledim.
- GitHub deposunu açtım, dosyaları depoya yükledim, günlük veri güncelleme iş akışını çalıştırdım ve GitHub Pages’i açıp siteyi yayına aldım.
- Yayında karşılaştığım hatayı (`index.html` dosyası ana klasörde olmadığı için sitenin açılmaması) buldum ve düzelttim.
- Yayındaki panoyu inceleyip sonuçları kontrol ettim.

## CV cümlesi

GitHub Actions ile günlük güncellenen, Steam oyun pazarını D3.js ile görselleştiren ve koordineli görünümler sunan canlı bir veri panosu tasarladım ve yayına aldım.
