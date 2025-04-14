# TESTING_SELENIUM: DemoQA Login/Logout Test Automation

Project này thực hiện kiểm thử tự động cho chức năng đăng nhập và đăng xuất của trang web DemoQA ([https://demoqa.com/login](https://demoqa.com/login)) sử dụng Selenium WebDriver với Python.

## Các công nghệ sử dụng

- **Python:** Ngôn ngữ lập trình chính.
- **Selenium WebDriver:** Thư viện tương tác với trình duyệt web.
- **Pytest:** Framework chạy test và quản lý fixture.
- **Webdriver Manager:** Tự động quản lý (tải/cập nhật) các driver cho trình duyệt (chromedriver, geckodriver).
- **Page Object Model (POM):** Mẫu thiết kế giúp tách biệt code tương tác trang web khỏi logic của test case, tăng khả năng bảo trì.
- **Factory Design Pattern:** Sử dụng để tạo các đối tượng WebDriver cho nhiều trình duyệt khác nhau một cách linh hoạt.

## Cấu trúc thư mục
