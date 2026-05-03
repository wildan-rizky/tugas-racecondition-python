1. Mengapa thread lain sulit berjalan?
   masalah utamanya adalah starvation(kelaparan thread)
   Penjelasan:
   - thread high_priority:
     - Loop tanpa henti
     - selalu cepat mengambil lock1 dan lock2
     - hampir tidak memberikan kesempatan thread lain
   - Thread lain (thread1, thread2):
     - Harus menunggu lock tersedia
     - Tapi lock hampir selalu direbut kembali oleh thread prioritas tinggi
   Akibatnya:
   Thread lain seperti "tidak kebagian gilirian" untuk eksekusi
2. Hubungan dengan scheduling policy
   Ini berkaitan langsung dengan cara OS / python scheduler membagi CPU.
   1. Time-sharing (Round Robin / Preemtive)
      - CPU dibagi berdasarkan time slice
      - Idealnya semua thread dapat giliran
   Masalahnya:
    - Thread tanpa sleep() atau blocking:
      - Selalu siap jalan (CPU-bound)
      - Mendominasi eksekusi
    - Thread lain kalah cepat dalam "rebutan lock"
   2. Priority Scheduling
    - Thread prioritas tinggi lebih sering dijalankan
   jika thread high_priority dianggap lebih penting:
    - Scheduler akan terus memilihnya
    - Thread lain makin jarang dapet CPU
   Ini menyebabkan:
    - Starvation pada thread prioritas rendah