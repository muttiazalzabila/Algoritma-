# Contoh Perbedaan List dan Tuple

# LIST (mutable — bisa diubah)
buah = ["apel", "jeruk", "mangga"]
print("List awal:", buah)

# Mengubah elemen list
buah[1] = "anggur"
print("List setelah diubah:", buah)

# Menambah elemen list
buah.append("pepaya")
print("List setelah append:", buah)

# TUPLE (immutable — tidak bisa diubah)
warna = ("merah", "biru", "hijau")
print("\nTuple awal:", warna)

# Percobaan mengubah tuple (akan error)
try:
    warna[1] = "kuning"
except TypeError as e:
    print("Error saat mencoba ubah tuple:", e)

# Melihat data dengan loop
print("\nData List:")
for item in buah:
    print("-", item)

print("\nData Tuple:")
for item in warna:
    print("-", item)
