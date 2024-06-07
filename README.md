# KEKL
## Kgamepass Explorer Killer Launcher
Nanggung coek masa GEKL

## Table of Contents

- [Installation](#Download)
- [Usage](#usage)
- [Features](#features)

## Download
Versi kompilasi yang dapat dieksekusi:
[Releases · bjdko/KEKL (github.com)](https://github.com/bjdko/KEKL/releases)

Atau
```bash
# Mengkloning repositori ini
git clone https://github.com/bjdko/KEKL.git

# Arahkan ke direktori repositori
cd KEKL

# Jalankan, tidak memerlukan paket pihak ketiga
python3 ./KgamepassExplorerKillerLauncher.py
```

## Penggunaan dan Keterangan

1. Search dan atau pilih game dari list.
2. Setel delay. Sp tw mau buka GameBar dulu, 0 = langsung kill setelah proses muncul.
3. Launch
   - Tombol "fetch":
     1. Nge-refresh list game dari GitHub.
     2. Menyesuaikan versi dengan cara listdir semua game GamePass (Butuh Admin).
     3. Refresh serta tawaran untuk menghapus game invalid.
   - Tombol "launch":
     1. launch dan kill explorer setelah delay yang ditentukan menggunakan PowerShell.
     2. GUI meninggal, biar ga ada proses python.exe sp tw ada anticit rewel lmoA.
   - Tombol "exit":
     1. If you see this, vivon zulul.

Cara menambahkan game sendiri (buat sementara, surely nanti w tambah bill tin feature):
1. **Nama Game**
   - Ga ngaruh, isi anything.
2. **package_name**
   - Cek di `{XboxGamesInstallation}/{Gamename}/appxmanifest.xml`
   - Line #3, contoh: `HelloGames.NoMansSky`

       - `<Identity Name="HelloGames.NoMansSky" Publisher="CN=E17FC9C0-77E1-4CDD-8AE0-E634942431EE" Version="4.72.0.0" ProcessorArchitecture="x64" />`
3. **executable**
   - Cek di `{XboxGamesInstallation}/{Gamename}/Content/Binaries`
   - Atau buka gamenya dan cek di detail Task Manager
```json
{
  "Nama Game": {
    "package_name": "HelloGames.NoMansSky",
    "executable": "MMS.exe"
  },
  "dummy": {
    "package_name": "dummy",
    "executable": "dummy"
  }
}
```

## Features

- Buka GamepassDari sini.
- Otomatis kill explorer untuk menghindari usiran ngontuol
- Add-able ish.

## To-Do / Roadmap / What I Want to Do

Daftar fitur, peningkatan, dan perbaikan bug yang saya rencanakan untuk dikerjakan. (malas)

- [ ] Bill Tin "game adder"
- [ ] Configurable settings
- [ ] ?

---

SNIFFA FOOTER