# Streamlit Alarm App

Aplikasi alarm sederhana berbasis web menggunakan [Streamlit](https://streamlit.io/). Setel alarm, dan aplikasi akan membunyikan suara saat waktunya tiba.

## Cara Menjalankan

1. **Clone repo**  
   ```bash
   git clone https://github.com/NAMAUSER/streamlit-alarm-app.git
   cd streamlit-alarm-app
   ```

2. **Install dependensi**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**  
   ```bash
   streamlit run app.py
   ```

4. **Setel alarm**  
   - Pilih waktu alarm, klik "Set Alarm"
   - Biarkan aplikasi tetap terbuka agar alarm berbunyi saat waktunya tiba

## Catatan

- Alarm berbunyi hanya jika aplikasi tetap aktif dan halaman tidak di-refresh di tengah jalan.
- Suara alarm menggunakan file audio dari internet (_alarm_clock.ogg_).
