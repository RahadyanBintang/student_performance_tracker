class Mahasiswa:
    """Kelas merepresentasikan data mahasiswa dengan atribut dasar dan kehadiran."""
    def __init__(self, nim, nama, hadir_persen=0):
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0
        self.hadir_persen = hadir_persen  # gunakan setter

    @property
    def hadir_persen(self):
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        if 0 <= value <= 100:
            self._hadir_persen = value
        else:
            raise ValueError("Persentase hadir harus antara 0-100")

    def info(self):
        return f"{self.nim} - {self.nama} (Hadir: {self.hadir_persen}%)"
