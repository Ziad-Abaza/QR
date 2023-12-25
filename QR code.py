import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import qrcode

def create_qr_codes():
    # الحصول على القيم المدخلة من المستخدم
    input_values = [entry.get() for entry in entry_list]
    
    # إنشاء كائن رمز QR لكل قيمة
    qr_codes = []
    for value in input_values:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5)
        qr.add_data(value)
        qr.make(fit=True)
        qr_codes.append(qr)
    
    # عرض مربع حوار فتح الملف لتحديد مسار الحفظ
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    
    if save_path:
        # حفظ الرموز QR في ملفات صورة في المسار المحدد
        for i, qr in enumerate(qr_codes):
            image = qr.make_image(fill_color="black", back_color="white")
            image.save(f"{save_path}_{i+1}.png")

def open_file_dialog():
    # عرض مربع حوار فتح الملف لاختيار ملف الصورة
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        # إظهار الصورة المحددة في نافذة البرنامج
        image = Image.open(file_path)
        image = image.resize((250, 250), Image.ANTIALIAS)
        qr_image = ImageTk.PhotoImage(image)
        qr_image_label.configure(image=qr_image)
        qr_image_label.image = qr_image
        
        # تحويل الصورة إلى رمز QR وحفظها في ملف
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5)
        qr.add_data(file_path)
        qr.make(fit=True)
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        
        if save_path:
            qr_image = qr.make_image(fill_color="black", back_color="white")
            qr_image.save(save_path)

# إنشاء نافذة البرنامج
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("500x400")

# قائمة لتخزين عناصر الإدخال
entry_list = []

# إضافة مداخل النص أو العناوين
for i in range(3):
    entry = tk.Entry(window)
    entry.pack()
    entry_list.append(entry)

# إضافة زر لتوليد الرموز QR
button = tk.Button(window, text="توليد QR Codes", command=create_qr_codes)
button.pack()

# إضافة زر لاختيار ملف الصورة
file_button = tk.Button(window, text="اختيار ملف صورة", command=open_file_dialog)
file_button.pack()

# إضافة عنصر لعرض الصورة المحددة
qr_image_label = tk.Label(window)
qr_image_label.pack()

# تشغيل البرنامج
window.mainloop()
