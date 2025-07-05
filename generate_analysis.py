import os
from datetime import datetime

# --- SOZLAMALAR ---
# Loyihaning asosiy papkasi (shu skript turgan joy)
PROJECT_ROOT = '.' 
# Natija yoziladigan fayl nomi
OUTPUT_FILE = 'project_analysis.md'

# Tahlilga qo'shiladigan papkalar ro'yxati
# Agar biror papkani qo'shish yoki olib tashlash kerak bo'lsa, shu yerni o'zgartiring
INCLUDE_DIRECTORIES = ['app', 'constructor', 'components', 'lib', 'types'] 

# Tahlildan chiqarib tashlanadigan papkalar va fayllar
EXCLUDE = [
    'node_modules', '.next', '.venv', 'venv', '__pycache__', 
    'package-lock.json', 'yarn.lock', '.DS_Store',
    # Bu skriptning o'zini ham qo'shmaymiz
    'generate_analysis.py',
    # Natija faylini ham qo'shmaymiz
    OUTPUT_FILE 
]

# Qaysi kengaytmali fayllarni tahlil qilish kerak
FILE_EXTENSIONS = [
    '.py', '.tsx', '.ts', '.js', '.jsx', '.json', 
    '.css', '.md', '.mjs', '.env', '.gitignore'
]
# ------------------

def generate_project_analysis():
    """Loyihadagi fayllarni o'qib, bitta .md fayliga jamlaydi."""
    
    markdown_content = []
    markdown_content.append(f"# Loyiha Tahlili Hisoboti")
    markdown_content.append(f"\nSana: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Barcha fayllarni to'plash
    file_paths_to_include = []
    for root, dirs, files in os.walk(PROJECT_ROOT, topdown=True):
        # Keraksiz papkalarni o'tkazib yuborish
        dirs[:] = [d for d in dirs if d not in EXCLUDE]
        
        # Faqat belgilangan papkalar ichidagini olish
        # Agar bu qismni olib tashlasangiz, butun loyiha skanerdan o'tadi
        if not any(root.startswith(os.path.join(PROJECT_ROOT, d)) for d in INCLUDE_DIRECTORIES) and root != PROJECT_ROOT:
            continue

        for file in files:
            if file not in EXCLUDE and any(file.endswith(ext) for ext in FILE_EXTENSIONS):
                file_paths_to_include.append(os.path.join(root, file))

    # Fayl strukturasini qo'shish
    markdown_content.append("## 📁 Fayl Strukturasi\n")
    markdown_content.append("```")
    # Bu yerga fayl strukturasini chiqaradigan logikani qo'shsa bo'ladi,
    # lekin hozircha soddalashtiramiz.
    markdown_content.append("... Fayl strukturasi bu yerda bo'ladi ...")
    markdown_content.append("```\n")

    markdown_content.append("## 📄 Muhim Fayllar Tarkibi\n")

    # Fayllarni o'qib, kontentni qo'shish
    for file_path in sorted(file_paths_to_include):
        relative_path = os.path.relpath(file_path, PROJECT_ROOT).replace('\\', '/')
        file_extension = os.path.splitext(file_path)[1][1:]

        markdown_content.append(f"### 📄 {relative_path}\n")
        markdown_content.append(f"```{file_extension}")
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                markdown_content.append(content)
        except Exception as e:
            markdown_content.append(f"Xatolik: Faylni o'qib bo'lmadi - {e}")
        
        markdown_content.append("```\n")

    # Natijani faylga yozish
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write("\n".join(markdown_content))
        print(f"✅ Tahlil fayli muvaffaqiyatli yaratildi: '{OUTPUT_FILE}'")
    except Exception as e:
        print(f"❌ Xatolik: Natijani faylga yozib bo'lmadi - {e}")


if __name__ == '__main__':
    generate_project_analysis()