from .mahasiswa import Mahasiswa
from .penilaian import Penilaian

class RekapKelas:
    """Mengelola daftar mahasiswa dan penilaiannya."""
    def __init__(self):
        self.data = {}

    def tambah_mahasiswa(self, nim, nama):
        self.data[nim] = {'mhs': Mahasiswa(nim, nama), 'nilai': Penilaian()}

    def set_hadir(self, nim, persen):
        self.data[nim]['mhs'].hadir_persen = persen

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        self.data[nim]['nilai'] = Penilaian(quiz, tugas, uts, uas)

    def predikat(self, nilai):
        if nilai >= 85: return "A"
        elif nilai >= 70: return "B"
        elif nilai >= 60: return "C"
        elif nilai >= 50: return "D"
        else: return "E"

    def rekap(self):
        hasil = []
        for nim, item in self.data.items():
            mhs = item['mhs']
            nilai_obj = item['nilai']
            nilai_akhir = nilai_obj.nilai_akhir()
            hasil.append({
                'nim': nim,
                'nama': mhs.nama,
                'hadir': mhs.hadir_persen,
                'nilai': nilai_akhir,
                'predikat': self.predikat(nilai_akhir)
            })
        return hasil
