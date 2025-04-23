import os

# قائمة الأسماء
names = [
    "ابو ديبو",
    "ابو سعيد",
    "ابو عمار",
    "ابو ابراهيم",
    "ابو احمد",
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

# جمع المدخلات
for index, name in enumerate(names, 1):
    print(f"\n{index}-{name}:")
    for mat in materials:
        while True:
            try:
                value = int(input(f"{mat}: "))
                if value < 0:
                    raise ValueError
                data[name][mat] = value
                break
            except ValueError:
                print("الرجاء إدخال رقم صحيح موجب أو صفر")

# حساب المجاميع (تجاهل الأصفار)
totals = {}
for mat in materials:
    total = 0
    for name in names:
        value = data[name][mat]
        if value > 0:  # تجاهل الأصفار في الجمع
            total += value
    totals[mat] = total

# إنشاء المحتوى للطباعة والحفظ
output = []
for name in names:
    output.append(f"{name}:")
    for mat in materials:
        output.append(f"{mat}: {data[name][mat]}")
    output.append("-" * 45)

output.append("\nالمجاميع النهائية (بدون حساب الأصفار):")
for mat in materials:
    output.append(f"{mat}: {totals[mat]}")

# الطباعة على الشاشة
print("\n" + "\n".join(output))

# حفظ النتائج في ملف
save_path = "/storage/emulated/0/لبن/النتائج.txt"
os.makedirs(os.path.dirname(save_path), exist_ok=True)

with open(save_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print(f"\nتم حفظ النتائج في: {save_path}")
