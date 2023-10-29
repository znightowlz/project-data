# project-data

1. เปิด command prompt แล้วไปที่ folder ที่เก็บไฟล์ project
2. พิมพ์คำสั่ง pip install -r requirements.txt
3. คำสั่งเปิดโปรเจ็ค py manage.py runserver
4. ถ้าไม่มีอะไรผิดปกติจะขึ้นแบบนี้

    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    October 29, 2023 - 23:04:25
    Django version 4.2.6, using settings 'pya.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

5. เอาเลข 127.0.0.1:8000 (บางเครื่องเลขอาจจะไม่ตรง เอาเลขที่ขึ้นบนหน้าจอตัวเอง) ไปใส่ตรงช่อง url ของ webbrowser
