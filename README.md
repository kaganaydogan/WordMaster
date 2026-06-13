# 📚 WordMaster

WordMaster, Python ve Flask kullanılarak geliştirilmiş modern bir İngilizce kelime öğrenme uygulamasıdır.

Kullanıcılar sisteme yeni İngilizce kelimeler ekleyebilir, kayıtlı kelimeleri görüntüleyebilir, silebilir ve quiz çözerek bilgilerini test edebilir. Proje, Nesne Yönelimli Programlama (OOP) prensipleri kullanılarak geliştirilmiştir.

---

## 🚀 Özellikler

* Kelime ekleme
* Kelime silme
* Kelime listeleme
* Kelime arama
* Quiz sistemi
* Rastgele kelime seçimi
* Doğru / Yanlış istatistikleri
* Başarı oranı hesaplama
* Dosyaya kayıt sistemi
* Boş kelime listesi kontrolü
* Responsive (Mobil Uyumlu) Tasarım
* Cam Efektli (Glassmorphism) Modern Arayüz
* Navbar destekli kullanıcı arayüzü
* OOP tabanlı sistem tasarımı

---

## 💻 Kullanılan Teknolojiler

* Python 3
* Flask
* HTML5
* CSS3
* Object Oriented Programming (OOP)
* File Handling (Dosya İşlemleri)

---

## 🏗️ Nesne Yönelimli Programlama (OOP)

Bu projede OOP kavramları aktif olarak kullanılmıştır.

### Encapsulation (Kapsülleme)

`Word` ve `User` sınıflarında private değişkenler kullanılmıştır.

```python
self.__english
self.__turkish
self.__username
```

### Inheritance (Kalıtım)

Admin sınıfı Student sınıfından kalıtım almaktadır.

```python
class Admin(Student):
```

### Kullanılan Sınıflar

* User
* Student
* Admin
* Word
* Quiz

---

## 📂 Proje Yapısı

```text
WordMaster/
│
├── app.py
├── words.txt
├── README.md
├── .gitignore
│
├── docs/
│   ├── Gereksinim_Analizi.docx
│   ├── Use_Case_Diagram.png
│   └── WordMaster_Class_Diagram.png
│
├── models/
│   ├── user.py
│   ├── student.py
│   ├── admin.py
│   ├── word.py
│   └── quiz.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_word.html
│   ├── words.html
│   ├── quiz.html
│   └── empty_words.html
│
└── static/
    └── style.css
```

---

## ⚙️ Kurulum

### 1. Depoyu klonlayın

```bash
git clone https://github.com/kullaniciadi/WordMaster.git
```

### 2. Proje klasörüne girin

```bash
cd WordMaster
```

### 3. Flask kurun

```bash
pip install flask
```

### 4. Uygulamayı çalıştırın

```bash
python app.py
```

### 5. Tarayıcıda açın

```text
http://127.0.0.1:5000
```

---

## 🎯 Proje Amacı

Bu proje, kullanıcıların İngilizce kelime hazinesini geliştirmesine yardımcı olmak amacıyla hazırlanmıştır.

Kullanıcılar:

* Yeni kelime ekleyebilir
* Kelimeleri görüntüleyebilir
* Kelimeleri silebilir
* Quiz çözebilir
* Başarı durumlarını takip edebilir

---

## 📊 UML Diyagramları

Proje içerisinde aşağıdaki analiz ve tasarım dokümanları bulunmaktadır:

* Gereksinim Analizi
* Use Case Diagram
* Class Diagram

Bu dosyalar `docs` klasörü içerisinde yer almaktadır.

---

## 👨‍💻 Geliştirici

Kağan Aydoğan

Bilgisayar Programcılığı Bölümü

BGT132 Programlama Temelleri Projesi

2026

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.
