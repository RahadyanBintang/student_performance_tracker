class Penilaian:
    """Kelas menyimpan nilai mahasiswa dan menghitung nilai akhir berbobot."""
    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        self.quiz = quiz
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def _validasi(self, nilai):
        if not (0 <= nilai <= 100):
            raise ValueError("Nilai harus 0–100")

    @property
    def quiz(self): return self._quiz
    @quiz.setter
    def quiz(self, val):
        self._validasi(val)
        self._quiz = val

    @property
    def tugas(self): return self._tugas
    @tugas.setter
    def tugas(self, val):
        self._validasi(val)
        self._tugas = val

    @property
    def uts(self): return self._uts
    @uts.setter
    def uts(self, val):
        self._validasi(val)
        self._uts = val

    @property
    def uas(self): return self._uas
    @uas.setter
    def uas(self, val):
        self._validasi(val)
        self._uas = val

    def nilai_akhir(self):
        return round(self.quiz * 0.15 + self.tugas * 0.25 + self.uts * 0.25 + self.uas * 0.35, 2)
