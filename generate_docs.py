import os
from datetime import datetime

# --- SOZLAMALAR ---

# Loyihaning asosiy papkasi (skript shu papkada bo'lsa, '.' kifoya)
ROOT_DIR = '.'

# Natija yoziladigan fayl nomi
OUTPUT_FILE = 'project_analysis.md'

# Hisobotga qo'shilmaydigan papka va fayllar ro'yxati
# Virtual muhit, kesh fayllar va skriptning o'zini istisno qilamiz
IGNORE_LIST = {
    '.venv',
    '__pycache__',
    '.git',
    '.idea',
    '.vscode',
    'node_modules',
    OUTPUT_FILE,
    os.path.basename(__file__)  # Bu skriptning o'zini ro'yxatga qo'shadi
}

# --- ASOSIY SKRIPT ---

def generate_file_tree(start_path):
    """Loyiha papkasining daraxtsimon ko'rinishini yaratadi."""
    tree_string = ""
    for root, dirs, files in os.walk(start_path, topdown=True):
        # Ignor qilinadigan papkalarni o'tkazib yuborish
        dirs[:] = [d for d in dirs if d not in IGNORE_LIST]
        
        # Daraxt chuqurligini hisoblash
        level = root.replace(start_path, '').count(os.sep)
        indent = '|   ' * (level)
        
        # Papka nomini daraxtga qo'shish
        if os.path.basename(root) != start_path:
             tree_string += f"{indent}|-- 📁 {os.path.basename(root)}/\n"
        
        sub_indent = '|   ' * (level + 1)
        # Fayllarni daraxtga qo'shish
        for f in sorted(files):
            if f not in IGNORE_LIST:
                tree_string += f"{sub_indent}|-- 📄 {f}\n"
    return tree_string

def get_file_contents(start_path):
    """Loyihadagi barcha fayllarning tarkibini o'qib, formatlab beradi."""
    contents_string = ""
    for root, dirs, files in os.walk(start_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in IGNORE_LIST]
        
        for filename in sorted(files):
            if filename in IGNORE_LIST:
                continue

            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, start_path)
            
            # Fayl kengaytmasiga qarab tilni aniqlash
            lang = ""
            if filename.endswith('.py'):
                lang = 'py'
            elif filename.endswith('.json'):
                lang = 'json'
            elif filename.endswith('.md'):
                lang = 'md'
            elif filename.endswith('.env') or filename.endswith('.gitignore'):
                lang = '' # Til ko'rsatilmasa, oddiy matn kabi ko'rinadi

            contents_string += f"### 📄 {relative_path}\n\n"
            contents_string += f"```{lang}\n"
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    contents_string += f.read()
            except Exception as e:
                contents_string += f"Xatolik: Faylni o'qib bo'lmadi - {e}"
            contents_string += "\n```\n\n"
            
    return contents_string

def main():
    """Asosiy funksiya - hisobotni yaratadi."""
    print(f"'{OUTPUT_FILE}' faylini yaratish boshlandi...")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        # 1. Sarlavha va sana
        f.write("# Loyiha Tahlili Hisoboti\n\n")
        f.write(f"Sana: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # 2. Fayl strukturasi
        f.write("## 📁 Fayl Strukturasi\n\n")
        f.write("```\n")
        f.write(generate_file_tree(ROOT_DIR))
        f.write("```\n\n")
        
        # 3. Fayllar tarkibi
        f.write("## 📄 Muhim Fayllar Tarkibi\n\n")
        f.write(get_file_contents(ROOT_DIR))

    print(f"\n✅ Loyiha tahlili muvaffaqiyatli '{OUTPUT_FILE}' fayliga yozildi.")

if __name__ == "__main__":
    main()