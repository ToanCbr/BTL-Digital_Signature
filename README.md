<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
<h2 align="center">
   XÂY DỰNG HỆ THỐNG KÝ VÀ XÁC THỰC TÀI LIỆU ĐIỆN TỬ BẰNG CHỮ KÝ SỐ
</h2>
<div align="center">
    <p align="center">
        <img src="picture/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="picture/fitdnu_logo.png" alt="AIoTLab Logo" width="180"/>
        <img src="picture/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

## 📖 1. Giới thiệu hệ thống 

📌 Hệ thống này được xây dựng nhằm **ký và xác thực tài liệu điện tử** một cách an toàn, đảm bảo tính toàn vẹn và chống giả mạo dữ liệu.  

📌 Người dùng có thể tải lên tài liệu, ký số bằng khóa riêng và xác thực chữ ký bằng khóa công khai. 

📌 Hệ thống phù hợp cho các tài liệu PDF, TXT và các giao dịch điện tử có tính pháp lý.

🖥️ Chức năng chính:

👉 Ký số tài liệu điện tử.

👉 Tạo chữ ký riêng.

👉 Xác thực tính hợp lệ và toàn vẹn của tài liệu.

👉 Quản lý danh sách lịch sử tài liệu đã ký.

👉 Giao diện trực quan, thân thiện với người dùng.


## 2. Công nghệ sử dụng

- **Frontend:** ReactJS, TailwindCSS  
- **Backend:** NodeJS, ExpressJS  
- **Cơ sở dữ liệu:** SQLite 
- **Mã hóa và bảo mật:**  
  - Thuật toán RSA (ký số và sinh cặp khóa)  
  - Hàm băm SHA-256  
- **Ngôn ngữ:** Python, HTML, CSS


## 3. Một số hình ảnh của hệ thống

 🖥️ Giao diện Trang chủ
 <img width="1913" height="887" alt="Home" src="https://github.com/user-attachments/assets/9bb50152-0a22-435d-afb5-6dee79bfddfb" />

 🖥️ Giao diện Ký số file
 <img width="1526" height="980" alt="Ky so file" src="https://github.com/user-attachments/assets/5ec7f072-6c77-43ea-91fc-2fb2747dfbda" />

 🖥️ Giao diện Tạo chữ ký 
 <img width="1464" height="987" alt="Tao chu ky" src="https://github.com/user-attachments/assets/8c128f5d-59c4-415a-9918-82801e0dddab" />

 🖥️ Giao diện Kiểm tra & xác thực
 <img width="1299" height="980" alt="Kiem tra   xac thuc" src="https://github.com/user-attachments/assets/946a4ee3-dcac-4e1a-9ffd-870d43ffa67c" />

 🖥️ Giao diện Lịch sử file đã ký
 <img width="1286" height="929" alt="Lich su file da ky" src="https://github.com/user-attachments/assets/11d3d85e-4a94-46e4-a2ce-9f3a0d6f2fbc" />


## 4. Các bước cài đặt
🔧 Bước 1. Chuẩn bị môi trường

    Cài đặt Visual Studio Code.

    Cài đặt Python 3.13.9

    Cài đặt SQLite.

 🗄️ Bước 2. Tạo bảng trong SQLite

    - Tạo database digital_signature.
    - Ứng dụng dùng SQLite và hàm init_db() trong app.py sẽ tạo file digital_signature.db.
    - Khởi tạo database bằng cách chạy:
      .\.venv\Scripts\python app.py
    - Kiểm tra file digital_signature.db xuất hiện trong thư mục dự án.

📦 Bước 3. Chuẩn bị cấu hình thêm và quyền thư mục

    - Đảm bảo thư mục lưu file upload có quyền ghi (mặc định uploads). Nếu cần tạo thủ công:
      mkdir uploads
    - Thiết lập SECRET_KEY an toàn thay vì dùng chuỗi mặc định trong app.py.
    - (Tùy chọn) Điều chỉnh MAX_CONTENT_LENGTH và UPLOAD_FOLDER trong app.py nếu cần.

⚙️ Bước 4. Cấu hình kết nối

    - Mặc định app dùng SQLite với đường dẫn 'digital_signature.db'. Để thay đổi:
      Sửa trực tiếp các lần gọi sqlite3.connect('digital_signature.db') sang đường dẫn tuyệt đối hoặc sang biến môi trường.
    - Ví dụ dùng biến môi trường (thêm vào app.py):
      # DATABASE_PATH = os.environ.get('DATABASE_PATH', 'digital_signature.db')
      # conn = sqlite3.connect(DATABASE_PATH)
    - Nếu chuyển sang DB khác (Postgres/MySQL), cần cài driver tương ứng và sửa toàn bộ logic kết nối.


  
▶️ Bước 5. Chạy hệ thống

- Chạy trực tiếp (dev, debug on):
  .\.venv\Scripts\python app.py
- (Ứng dụng sẽ gọi init_db() và chạy trên http://127.0.0.1:5000 theo mặc định.)
- Hoặc dùng Flask CLI:
  set FLASK_APP=app.py
  set FLASK_ENV=development
  .\.venv\Scripts\flask run --host=0.0.0.0 --port=5000
- Dừng server: Ctrl+C trong terminal.
- Lưu ý: Trên môi trường production, dùng WSGI server (gunicorn/uvicorn) và tắt chế độ debug.


## 5. Contact me

    Nguyễn Minh Đức CNTT 16-01

    Khoa: Công nghệ thông tin - Trường Đại học Đại Nam 

    SĐT: 0372334278

    Email: duc1608204@gmail.com


    
