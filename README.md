# Matematik Hafıza Oyunu

Bu proje, Python ve Tkinter kullanılarak geliştirilmiş 4x4'lük bir matematik hafıza oyunudur.

## Özellikler

- 4x4 oyun tahtası
- Rastgele matematiksel işlemler (toplama, çıkarma, çarpma, bölme)
- Her oyunda farklı işlemler
- Görsel geri bildirim (renkli kartlar)
- Eşleştirme mantığı
- Kazanma kontrolü

## Gereksinimler

- Python 3.x
- Tkinter (Python ile birlikte gelir)

## Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/oguzhanbilir/matMemoryGame.git
```

2. Proje dizinine gidin:
```bash
cd matMemoryGame
```

3. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

## Nasıl Oynanır

1. Oyunu başlatmak için:
```bash
python memory_game.py
```

2. Oyun Kuralları:
   - Kartlar kapalı olarak başlar
   - Her turda iki kart açılır
   - Açılan kartlardan biri matematiksel işlem, diğeri sonuç olmalıdır
   - Eşleşme doğruysa kartlar açık kalır, yanlışsa kapanır
   - Tüm kartlar eşleştiğinde oyun biter

## Renk Kodları

- Kapalı kartlar: Açık gri (lightgray)
- Açılan kartlar: Açık mavi (lightblue)
- Eşleşen kartlar: Açık yeşil (lightgreen)

## Geliştirici

Bu oyun [Oğuzhan Bilir](https://github.com/oguzhanbilir) tarafından geliştirilmiştir.
