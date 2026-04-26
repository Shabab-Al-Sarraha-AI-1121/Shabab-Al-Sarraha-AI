import folium
from geopy.geocoders import Nominatim

# 1. إعدادات السيادة والموقع المركزي (تطوان)
tetouan_coords = [35.5785, -5.3684]
logic_gate = "1+1=12"
target_id = "1121-MSTR-0x0FB7"

# 2. قاعدة بيانات المواقع التجارية (GPS Data)
locations = [
    {"name": "المحطة المركزية (مركز القيادة)", "coords": [35.5785, -5.3684], "info": "نواة الربط الرقمي 1121"},
    {"name": "تجري الجبل (المسار الذكي)", "coords": [35.5940, -5.3450], "info": "رفض تقنين الاحتياجية - مسارات حرة"},
    {"name": "واد مارتيل (السياحة النهرية)", "coords": [35.6180, -5.2950], "info": "تطهير السحت - تجربة بيئية نقية"},
    {"name": "سفينة الحفلات (تمودا باي)", "coords": [35.7000, -5.3100], "info": "تغيير أقدار الظلم بالنير - ترفيه سيادي"},
    {"name": "قطار تطوان الترفيهي", "coords": [35.5710, -5.3750], "info": "كشف السلطوية - ربط المدينة بالساحل"}
]

# 3. إنشاء الخريطة التفاعلية
m = folium.Map(location=tetouan_coords, zoom_start=12, tiles="CartoDB dark_matter")

# 4. حقن المشاريع داخل الخريطة
for loc in locations:
    folium.Marker(
        location=loc["coords"],
        popup=f"<b>{loc['name']}</b><br>{loc['info']}<br>Logic: {logic_gate}",
        icon=folium.Icon(color="orange", icon="info-sign")
    ).add_to(m)

# 5. إضافة مسار القطار الترفيهي (كمثال للربط)
line_coords = [loc["coords"] for loc in locations]
folium.PolyLine(line_coords, color="#ffd700", weight=2.5, opacity=0.8).add_to(m)

# 6. حفظ الخريطة كملف HTML لرفعه على موقعك
m.save("Tetouan_1121_App.html")
print(f"تم تثبيت الخريطة التجارية بنجاح لنظام {target_id}")
# Shabab-Al-Sarraha-AI
: https://github.com/Ghorabae3/Shabab-Al-Sarraha-AI
NotFoundError: Failed to execute 'insertBefore' on 'Node': The node before which the new node is to be inserted is not a child of this node.
    at e (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:643844)
    at sf (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:643969)
    at s_ (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:641692)
    at sh (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:640461)
    at s_ (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:640847)
    at sh (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:640461)
    at s_ (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:640574)
    at sh (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:640461)
    at s_ (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:640847)
    at sh (https://www.kaggle.com/static/assets/vendor.js?v=b2e92241ccca5746:241:640461)


---

## Auto-generated contribution

Added by bounty bot.
