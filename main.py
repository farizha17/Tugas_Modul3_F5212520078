print("=" * 50)
print("SISTEM VERIFIKASI PENDAFTARAN SEMINAR MAHASISWA")
print("=" * 50)

nama = input("Masukkan nama mahasiswa    : ")
nim = input("Masukkan NIM               : ")
prodi = input("Masukkan program studi     : ")

try:
    semester = int(input("Masukkan semester          : "))
except ValueError:
    print("Error: Semester harus berupa angka!")
    exit()

pembayaran = input("Sudah membayar? (ya/tidak) : ").lower()

print("\n" + "=" * 50)
print("HASIL VERIFIKASI PENDAFTARAN")
print("=" * 50)

print(f"Nama          : {nama}")
print(f"NIM           : {nim}")
print(f"Program Studi : {prodi}")
print(f"Semester      : {semester}")

if semester >= 2 and pembayaran == "ya":
    print("Status        : PENDAFTARAN DITERIMA")
    print("Keterangan    : Persyaratan terpenuhi.")
else:
    print("Status        : PENDAFTARAN DITOLAK")

    if semester < 2:
        print("Keterangan    : Minimal mahasiswa semester 2.")

    if pembayaran != "ya":
        print("Keterangan    : Pembayaran belum dilakukan.")

print("=" * 50)
