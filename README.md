# DATN_HoangThuHong_HK2_2024
Đề tài ĐATN: “Nghiên cứu, ứng dụng các mô hình học máy để dự đoán mức độ béo phì”

Trang web truy cập dự đoán mức độ béo phì: https://dudoanbeophi.streamlit.app/

## Tổng quan dự án
Báo cáo này cung cấp cái nhìn tổng quan toàn diện về đồ án Dự đoán mức độ béo phì. Mục tiêu của dự án là nghiên cứu, ứng dụng các mô hình học máy để dự đoán mức độ béo phì, đồng thời triển khai mô hình có độ chính xác cao nhất vào thực tế nhằm đưa ra lời khuyên, khuyến nghị phù hợp cho từng người nhằm giúp họ ngăn ngừa và cải thiện tình trạng sức khỏe.

### Thông tin tập dữ liệu
Tập dữ liệu được sử dụng trong đồ án này chứa thông tin về tên, tuổi, giới tính, chiều cao, cân nặng, thông tin về gia đình, thói quen ăn uống và mức độ hoạt động thể chất. Nó là cơ sở dữ liệu để nghiên cứu các yếu tố ảnh hưởng đến chỉ số cân nặng và sức khỏe, hỗ trợ phân tích và dự đoán tình trạng dinh dưỡng và béo phì dựa trên các thông tin đa dạng về lối sống và thói quen ăn uống của cá nhân.

#### Đặc trưng dữ liệu
Tập dữ liệu bao gồm 18 thuộc tính:

1. **first_name:** Tên của bệnh nhân
2. **Gender:** Giới tính (Male = nam, Female = nữ)
3. **Age:** Tuổi nằm trong khoảng [14, 61]
4. **Height:** Chiều cao đơn vị đo là mét (m), nằm trong khoảng [1.45, 1.98]
5. **Weight:** Cân nặng đơn vị đo là kilogram (kg), nằm trong khoảng [39, 173]
6. **family_history_with_overweight:** Tiền sử gia đình mắc bệnh béo phì (Yes = có, No = không)
7. **FAVC:** Thường xuyên tiêu thụ thực phẩm có hàm lượng calo cao không? (Yes = có, No = không)
8. **FCVC:** Tần suất tiêu thụ rau ( 1 = Không bao giờ, 2 = Thỉnh thoảng, 3 = Luôn luôn)
9. **NCP:** Số bữa ăn chính (1 = Một bữa chính mỗi ngày, 2 = Hai bữa ăn chính trong ngày, 3 = Ba bữa chính mỗi ngày, 4 = Hơn ba bữa)
10. **CAEC:** Tần suất ăn vặt? (No = Không, Sometimes = thỉnh thoảng, Frequently = thường xuyên, Always = luôn luôn)
11. **SMOKE:** Bạn có hút thuốc không? (Yes = có, No = không)
12. **CH2O:** Lượng nước uống hàng ngày (1 = ít hơn 1 lít, 2 =  1 đến 2 lít, 3 = hơn 2 lít)
13. **SCC:** Giám sát tiêu thụ calo (Yes = có, No = không)
14. **FAF:** Tần suất hoạt động thể chất (0 = không, 1 = 1 hoặc 2 (ngày/tuần), 2 = 3 đến 4 (ngày/tuần), 3 = hơn 4 (ngày/tuần))
15. **TUE:** Thời gian sử dụng thiết bị công nghệ (0 = 0 đến 2 (giờ/ngày), 1 = 3 đến 5 (giờ/ngày), 2 = hơn 5 (giờ/ngày))
16. **CALC:** Bạn có thường xuyên uống chất có cồn? (No = Không, Sometimes = thỉnh thoảng, Frequently = thường xuyên, Always = luôn luôn)
17. **MTRANS:** Thường sử dụng phương tiện di chuyển (Automobile = xe hơi, Motorbike = xe máy, Bike = xe đạp, Public_Transportation = xe bus, Walking = đi bộ)
18. **NObeyesdad:** Phân loại mức độ béo phì (Insufficient_Weight = Thiếu cân, Normal_Weight = Bình thường, Overweight_Level_I = Thừa cân cấp 1, Overweight_Level_II = Thừa cân cấp 2, Obesity_Type_I = Béo phì cấp 1, Obesity_Type_II = Béo phì cấp 2, Obesity_Type_III = Béo phì cấp 3)

## Tiền xử lý dữ liệu
1. **Trích chọn dữ liệu:** Lựa chọn các thuộc tính quan trọng 
2. **Làm sạch dữ liệu:** Kiểm tra và xử lý giá trị ngoại lai, đồng thời cũng kiểm tra và xử lý giá trị thiếu thiếu. Ở đây, thì lựa chọn cách xử lý phù hợp. Đảm bảo tính nhất quán trong các kiểu dữ liệu.
3. **Chia dữ liệu:** Chia tập dữ liệu thành các tập huấn luyện và kiểm tra để đánh giá mô hình.

## Xây dựng mô hình

1. **Lựa chọn mô hình:** Chọn thuật toán học máy thích hợp để phân loại mức độ béo phì. Các lựa chọn phổ biến bao gồm K-hàng xóm gần nhất (KNN), Phân loại rừng ngẫu nhiên (DTC), Phân loại rừng ngẫu nhiên (RFC).
2. **Đào tạo mô hình:** Huấn luyện mô hình đã chọn trên dữ liệu huấn luyện.
3. **Đánh giá mô hình:** Đánh giá hiệu suất của mô hình bằng cách sử dụng các số liệu thích hợp như accuracy, precision, recall và F1-score trên dữ liệu thử nghiệm.

## Triển khai mô hình
1. **Tuần tự hóa mô hình:** Tuần tự hóa mô hình đã đào tạo thành tệp tin lưu trữ mô hình tốt nhất (`RandomForest_Model.pkl`) để sử dụng trong tương lai.
2. **Ứng dụng web Streamlit:** Tạo một ứng dụng web Streamlit tải mô hình và cung cấp giao diện người dùng để dự đoán mức độ béo phì.

## Ứng dụng web Streamlit
1. **Giao diện người dùng:** Tạo giao diện thân thiện với người dùng với các trường nhập để người dùng nhập thông tin của họ.
2. **Tải mô hình:** Tải mô hình đã đào tạo (`RandomForest_Model.pkl`) trong ứng dụng Streamlit.
3. **Xử lý đầu vào của người dùng:** Chấp nhận đầu vào của người dùng, xử lý trước chúng và đưa chúng vào mô hình để dự đoán.
4. **Dự đoán:** Hiển thị kết quả dự đoán mức độ béo phì và đưa ra lời khuyên cho người dùng.
5. **Phản hồi:** Cho phép người dùng tương tác với ứng dụng, cung cấp phản hồi và đưa ra dự đoán dựa trên thông tin đầu vào của họ.

## Phần kết luận
Đồ án "Nghiên cứu, ứng dụng các mô hình học máy để dự đoán mức độ béo phì" bao gồm quá trình tiền xử lý dữ liệu, xây dựng mô hình và triển khai mô hình học máy tốt nhất để dự đoán mức độ béo phì. Ứng dụng web Streamlit cung cấp giao diện thân thiện với người dùng để người dùng đưa ra dự đoán dựa trên thông tin của họ.

## Hướng phát triển
1. Nghiên cứu thêm các thuật toán học máy mới và các phương pháp tiền xử lý dữ liệu, cũng như tinh chỉnh các tham số để cải thiện hiệu suất mô hình.
2. Mở rộng phạm vi nghiên cứu, các yếu tố như độ tuổi, chiều cao và cân nặng để mô hình có thể áp dụng rộng rãi hơn, và hỗ trợ nhiều người hơn trong việc duy trì và phát triển sức khỏe.

## Tài liệu tham khảo
   - Streamlit: https://docs.streamlit.io/
   - Python: https://www.python.org/
   - Các tài liệu liên quan khác.