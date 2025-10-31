from tracker import RekapKelas, build_markdown_report, build_html_report, save_text

def main():
    tracker = RekapKelas()

    while True:
        print("\n=== Student Performance Tracker ===")
        print("1) Tambah mahasiswa")
        print("2) Ubah presensi")
        print("3) Ubah nilai")
        print("4) Lihat rekap")
        print("5) Simpan laporan Markdown")
        print("6) Filter nilai < 70 (BONUS)")
        print("7) Keluar")
        print("8) Ekspor laporan HTML (BONUS EKSTRA)")

        choice = input("Pilih menu: ")

        if choice == "1":
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan nama: ")
            tracker.tambah_mahasiswa(nim, nama)
            print("✅ Mahasiswa ditambahkan!")

        elif choice == "2":
            nim = input("NIM: ")
            hadir = float(input("Persentase hadir: "))
            tracker.set_hadir(nim, hadir)
            print("✅ Presensi diperbarui!")

        elif choice == "3":
            nim = input("NIM: ")
            quiz = float(input("Nilai quiz: "))
            tugas = float(input("Nilai tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))
            tracker.set_penilaian(nim, quiz, tugas, uts, uas)
            print("✅ Nilai diperbarui!")

        elif choice == "4":
            print("\n📋 Rekap Nilai:")
            for r in tracker.rekap():
                print(r)
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == "5":
            records = tracker.rekap()
            content = build_markdown_report(records)
            save_text("out/report.md", content)
            print("💾 Laporan tersimpan di out/report.md")
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == "6":
            print("\n🎯 Mahasiswa dengan nilai < 70:")
            low_scores = [r for r in tracker.rekap() if r['nilai'] < 70]
            for r in low_scores:
                print(r)
            print(f"Total: {len(low_scores)} mahasiswa")
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == "8":
            records = tracker.rekap()
            html_content = build_html_report(records)
            save_text("out/report.html", html_content)
            print("🌐 Laporan HTML tersimpan di out/report.html")
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == "7":
            print("👋 Terima kasih sudah menggunakan Student Performance Tracker!")
            break

        else:
            print("⚠️ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
