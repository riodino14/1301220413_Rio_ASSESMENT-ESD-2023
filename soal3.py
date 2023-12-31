def temukan_pencuri_kue(urutan_kedatangan, foto_xiao):
    
    kebiasaan_teman = {
        "Ningguang": "memeriksa kue",
        "Hutao": "memberikan kado tanpa memperhatikan kue",
        "Xiao": "memotret apa pun yang dia lihat pertama kali",
        "Childe": "membawa air mineral dan meletakkannya di meja"
    }

    
    kue_masih_utuh = "kue" in foto_xiao.lower()

   
    if kue_masih_utuh:
       
        pencuri = next(teman for teman in urutan_kedatangan if kebiasaan_teman[teman] != "memeriksa kue")
    else:
        
        pencuri = next(teman for teman in urutan_kedatangan if kebiasaan_teman[teman] == "memeriksa kue")

    return pencuri


urutan_kedatangan = ["Ningguang", "Hutao", "Xiao", "Childe"]
foto_xiao = "Foto kue masih utuh di meja."


pencuri_kue = temukan_pencuri_kue(urutan_kedatangan, foto_xiao)


print("Berdasarkan informasi yang diberikan, kemungkinan pencuri kue adalah:", pencuri_kue)
