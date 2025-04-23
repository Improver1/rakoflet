import os
from colorama import Fore, Style, init

# تهيئة الألوان للواجهة
init(autoreset=True)

# قائمة الأسماء
names = [
    "ابو ديبو",
    "ابو سعيد",
    "ابو عمار",
    "ابو ابراهيم",
    "و احمد",
    "ابو عزو",
    "النور للتسوق",
    "عبدو السلام",
    "العموري",
    "ابو فيصل",
    "محمود بلال",
    "ابو حسين",
    "ابو بكري",
    "ابو محمود الخضر",
    "محمد الخضر",
    "عبدو الخضر"
]

# المواد
materials = [
    "خليط صغير",
    "خليط كبير",
    "بقر صغير",
    "بقر بوري",
    "غنم اول"
]

# تهيئة بنية التخزين
data = {name: {mat: 0 for mat in materials} for name in names}

def print_bold(text):
    """عرض نص بخط عريض"""
    print(f"\033[1m{text}\033[0m")

def colored_name(text):
    """تلوين الأسماء بالأصفر"""
    return f"{Fore.YELLOW}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def colored_material(text):
    """تلوين المواد بالأبيض"""
    return f"{Fore.WHITE}{text}{Style.RESET_ALL}"

# جمع المدخلات
for index, name in enumerate(names, 1):
    print_bold(f"\n{index}-{colored_name(name)}:")
    for mat in materials:
        while True:
            try:
                value = int(input(colored_material(f"{mat}: ")))
                if value < 0:
                    raise ValueError
                data[name][mat] = value
                break
            except ValueError:
                print(Fore.RED + "الرجاء إدخال رقم صحيح موجب أو صفر")

# حساب المجاميع (تجاهل الأصفار)
totals = {}
for mat in materials:
    total = 0
    for name in names:
        value = data[name][mat]
        if value > 0:
            total += value
    totals[mat] = total

# إنشاء المحتوى للطباعة والحفظ مع زيادة حجم العرض
output = []
for name in names:
    output.append(f"{'='*100}")
    output.append(f"{' '*40}{name}:{' '*40}")
    output.append(f"{'='*100}")
    for mat in materials:
        output.append(f"{' '*30}{mat}: {data[name][mat]}{' '*30}")
    output.append("\n")

output.append(f"{'='*100}")
output.append(f"{' '*30}المجاميع النهائية (بدون حساب الأصفار):{' '*30}")
output.append(f"{'='*100}")
for mat in materials:
    output.append(f"{' '*30}{mat}: {totals[mat]}{' '*30}")
output.append(f"{'='*100}")

# عرض النتائج مع الألوان والحجم الكبير
print("\n\033[1m" + "="*100 + "\033[0m")
for line in output:
    if any(name in line for name in names):
        print(colored_name(line))
    elif any(mat in line.split(':')[0].strip() in materials for mat in materials):
        print(colored_material(line))
    else:
        print_bold(line)

# حفظ النتائج في ملف
save_path = "/storage/emulated/0/لبن/النتائج.txt"
os.makedirs(os.path.dirname(save_path), exist_ok=True)

with open(save_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print_bold(f"\nتم حفظ النتائج في: {save_path}")
