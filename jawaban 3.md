1. ketika buffer diubah menjadi 3 buffer maksimal hanya bisa menampung 3 item
2. - saat buffer = 5 (awal) producer relatif jarang blocking
   - saat buffer = 3 (lebih kecil) producer akan lebih sering blocking
   - pola yang terlihat: output jadi lebih bergantian
   intinya:
   semakin kecil buffer semakin sering terjadi blocking dan sinkronisasi semakin intens
3. Mutex
   - hanya 1 thread boleh masuk critical section
   - bersifat binary lock(0/1)
   semaphore
   - Bisa mengatur lebih dari 1 resource
   - nilainya bisa > 1 (contoh: 3, 5, dll)