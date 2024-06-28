import streamlit as st
import pandas as pd
import pickle

# Tải mô hình
with open('RandomForest_Model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Tạo ứng dụng web Streamlit
st.title("Dự đoán mức độ Béo phì")

# Các trường đầu vào cho đầu vào của người dùng
st.sidebar.header("Hướng dẫn sử dụng Website")
st.sidebar.markdown(
    """
    **Lưu ý: Dự đoán mức độ béo phì của cá nhân trong độ tuổi từ 14 đến 61, 
    có chiều cao nằm trong khoảng từ 1.45m đến 1.98m và cân nặng từ 39kg đến 173kg. 
    Phạm vi dự đoán không bao gồm các cá nhân nằm ngoài khoảng giá trị này. 
    Chúng tôi sẽ nghiên cứu các giá trị nằm ngoài sau một thời gian tới, hãy quay lại sau.**
    
    ## Bước 1: Nhập thông tin cá nhân
    Bên trái của trang web là một biểu mẫu cho phép bạn nhập thông tin cá nhân của mình. 
    Hãy điền thông tin theo yêu cầu của từng trường dữ liệu. Đảm bảo bạn nhập đầy đủ và chính xác.
    - **Tuổi**: Nằm trong khoảng 14 đến 61.
    - **Chiều cao**: Nằm trong khoảng 1.45 đến 1.98. Đơn vị là m. Vui lòng nhập số thập phân với dấu chấm (.)
    - **Cân nặng**: Nằm trong khoảng 39 đến 173. Đơn vị là kg. Vui lòng nhập số thập phân với dấu chấm (.)
    - **FCVC**: 1 là Không bao giờ, 2 là thỉnh thoảng, 3 là luôn luôn
    - **NCP**: 1 là 1 bữa, 2 là 2 bữa, 3 là 3 bữa, 4 là hơn 3
    - **CH2O**: 1 là ít hơn 1 lít, 2 là từ 1 - 2 lít, 3 là hơn 2 lít (ngày)

    ## Bước 2: Nhấn nút "Dự đoán"
    Sau khi bạn đã nhập đủ thông tin, nhấn nút "Dự đoán" để ứng dụng tính toán và dự đoán mức độ béo phì của bạn dựa trên thông tin đã cung cấp.
    
    ## Bước 3: Xem kết quả
    Kết quả của dự đoán sẽ được hiển thị bên dưới nút "Dự đoán". 
    Bạn sẽ thấy mức độ béo phì được dự đoán cùng với thông điệp hướng dẫn tương ứng.
    
    ## Bước 4: Thử nghiệm lại
    Nếu bạn muốn thử nghiệm với các giá trị khác hoặc thông tin khác, 
    bạn có thể điền lại thông tin vào biểu mẫu và nhấn nút "Dự đoán" một lần nữa.
    #####
    Hãy khám phá và trải nghiệm ứng dụng của chúng tôi để tận hưởng những lợi ích mà nó mang lại. 
    Đừng ngần ngại chia sẻ ý kiến và phản hồi của bạn với chúng tôi để chúng tôi có thể cải thiện dịch vụ. Chúc bạn có một ngày tuyệt vời và đầy ý nghĩa!
    """
)

# Trường nhập
with st.form(key='my_form'):
    col1, _, col2 = st.columns([1, 0.1, 1])  # Thêm một phần tử trống giữa hai cột
    with col1:
        age = st.text_input('**Nhập tuổi của bạn (từ 14 đến 61)**')
        height = st.text_input('**Nhập chiều cao của bạn (từ 1.45 đến 1.98) m**')
        weight = st.text_input('**Nhập cân nặng của bạn (từ 39 đến 173) kg**')
        fcvc = st.slider('**Bạn có thường ăn rau trong bữa ăn của mình không? (FCVC)**', 1, 3)
        ncp = st.slider('**Hàng ngày bạn ăn bao nhiêu bữa chính? (NCP)**', 1, 4)
        ch2o = st.slider('**Lượng nước uống hàng ngày (CH2O)**', 1, 3)
    with col2:
        family_history_with_overweight = st.selectbox('**Có thành viên nào trong gia đình bị thừa cân hoặc béo phì không**', ['không', 'có'])
        favc = st.selectbox('**Bạn có thường xuyên ăn thực phẩm có hàm lượng calo cao không? (FAVC)**', ['không', 'có'])
        calc = st.selectbox('**Bạn có thường xuyên uống chất có cồn? (CALC)**', ['Không (No)', 'Thỉnh thoảng (Sometimes)', 'Thường xuyên (Frequently)', 'Luôn luôn (Always)'])
        smoke = st.selectbox('**Bạn có hút thuốc không? (SMOKE)**', ['không', 'có'])
        mtrans = st.selectbox('**Bạn thường sử dụng phương tiện di chuyển nào? (MTRANS)**', ['Xe hơi (Automobile)', 'Xe máy (Motorbike)', 'Xe đạp (Bike)', 'Xe bus (Public_Transportation)', 'Đi bộ (Walking)'])
    
    # Sử dụng CSS để căn giữa nút
    st.markdown("""
    <style>
    .stButton>button {
        background-color: pink;
        margin: auto;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

    submit_button = st.form_submit_button(label='Dự đoán')

# Mapping 
family_history_mapping = {'không': 0, 'có': 1}
favc_mapping = {'không': 0, 'có': 1}
calc_mapping = {'Không (No)': 0, 'Thỉnh thoảng (Sometimes)': 1, 'Thường xuyên (Frequently)': 2, 'Luôn luôn (Always)': 3}
smoke_mapping = {'không': 0, 'có': 1}
mtrans_mapping = {'Xe hơi (Automobile)': 0, 'Xe máy (Motorbike)': 1, 'Xe đạp (Bike)': 2, 'Xe bus (Public_Transportation)': 3, 'Đi bộ (Walking)': 4}

# Tạo DataFrame với dữ liệu đầu vào của người dùng
user_input_data = pd.DataFrame({
    'Age': [age],
    'Height': [height],
    'Weight': [weight],
    'family_history_with_overweight': [family_history_mapping[family_history_with_overweight]],
    'FAVC': [favc_mapping[favc]],
    'FCVC': [fcvc],
    'NCP': [ncp],
    'SMOKE': [smoke_mapping[smoke]],
    'CH2O': [ch2o],
    'CALC': [calc_mapping[calc]],
    'MTRANS': [mtrans_mapping[mtrans]]
})

# Nút dự đoán
if submit_button:
    try:
        age = int(age)
        height = float(height)
        weight = float(weight)
        
        # Kiểm tra xem tuổi, chiều cao và cân nặng có nằm trong phạm vi hợp lệ không
        if not (14 <= age <= 61):
            st.error("Tuổi phải nằm trong khoảng từ 14 đến 61.")
        elif not (1.45 <= height <= 1.98):
            st.error("Chiều cao phải nằm trong khoảng từ 1.45m đến 1.98m.")
        elif not (39 <= weight <= 173):
            st.error("Cân nặng phải nằm trong khoảng từ 39kg đến 173kg.")
        else:
            # Đưa ra dự đoán bằng cách sử dụng mô hình đã tải
            predicted_obesity_level = model.predict(user_input_data)

            # Ánh xạ nhãn được dự đoán vào danh mục và thông báo tương ứng
            obesity_level_mapping = {
                0: ('Insufficient_Weight', 
                "Bạn đang ở trong tình trạng **thiếu cân** - thường có nguy cơ:\n"
                "1. Suy dinh dưỡng.\n"
                "2. Hệ miễn dịch suy giảm.\n"
                "3. Cơ thể mệt mỏi, gầy yếu.\n"
                "4. Thiếu máu.\n"
                "5. Nguy cơ loãng xương.\n"
                "6. Suy giảm trí nhớ.\n"
                "\nĐể cải thiện tình trạng này, bạn cần tăng cân một cách cẩn thận và lành mạnh. Dưới đây là lời khuyên dành cho bạn:\n"
                "\n**Chế độ ăn uống cân đối**: Hãy đảm bảo bạn tiêu thụ đủ lượng chất dinh dưỡng từ cả bốn nhóm thực phẩm như tinh bột, đạm, béo, và các loại vitamin và khoáng chất. Điều này có thể bao gồm thêm các loại thực phẩm như hạt, dầu hạt, thực phẩm giàu protein như thịt gà, cá, đậu, hạt, và rau cải xanh.\n"
                "\n**Tăng số lượng bữa ăn**: Thay vì ăn ba bữa lớn mỗi ngày, hãy chia nhỏ thành nhiều bữa nhỏ hơn, khoảng 5-6 bữa mỗi ngày. Điều này giúp cung cấp năng lượng liên tục cho cơ thể và tối ưu hóa quá trình tiêu hóa.\n"
                "\n**Luyện tập thể dục thể thao**: Tập thể dục đều đặn không chỉ giúp tăng cân mà còn cải thiện sức khỏe tổng thể. Hãy chọn những hoạt động như tập gym, yoga, hoặc các bài tập sức mạnh để giúp tăng cơ và cân nặng.\n"
                "\n**Nghỉ ngơi hợp lý**: Đảm bảo bạn có đủ giấc ngủ hàng đêm và thực hiện các phương pháp giảm căng thẳng như thiền, yoga, hoặc dành thời gian cho sở thích cá nhân.\n"
                "\n**Bổ sung thêm chất dinh dưỡng**: Nếu cần thiết, bạn có thể sử dụng các sản phẩm bổ sung vitamin, khoáng chất từ các thương hiệu uy tín để giúp bổ sung chất dinh dưỡng cho cơ thể.\n"
                "\n**Đề xuất kiểm tra lại cân nặng của bạn mỗi hai tháng một lần để theo dõi tiến triển và đảm bảo rằng cân nặng của bạn đang trong trạng thái sức khỏe ổn định hơn.**"),
                1: ('Normal_Weight', 
                    "Trọng lượng cơ thể của bạn nằm trong khoảng **bình thường**, đây là một dấu hiệu tích cực cho sức khỏe. "
                    "Để duy trì trạng thái này, điều quan trọng là bạn tiếp tục duy trì các thói quen lành mạnh, bao gồm chế độ ăn uống cân đối và hoạt động vận động đều đặn. "
                    "Đề xuất kiểm tra sức khỏe của bạn mỗi hai tháng một lần để đảm bảo rằng bạn vẫn duy trì được trạng thái cân nặng và sức khỏe ổn định."),
                2: ('Overweight_Level_I', 
                    "Bạn đang ở mức độ **thừa cân cấp độ I**, điều này đòi hỏi sự chú ý đối với chế độ dinh dưỡng và hoạt động thể chất hàng ngày. "
                    "Để cải thiện tình trạng này, bạn chỉ cần tuân thủ các phương pháp giảm cân an toàn. Dưới đây là lời khuyên dành cho bạn:\n"
                    "- Việc kiểm soát khẩu phần ăn và tăng cường hoạt động vận động có thể giúp cải thiện tình trạng này.\n"
                    "- Đề xuất kiểm tra lại cân nặng của bạn mỗi hai tháng một lần để theo dõi tiến triển và đảm bảo rằng bạn vẫn đang tiến vào hướng của một trạng thái sức khỏe ổn định hơn."),
                3: ('Overweight_Level_II', 
                    "Bạn đang ở mức độ **thừa cân cấp độ II**, điều này đòi hỏi sự chú ý và hành động quyết liệt hơn đối với việc điều chỉnh chế độ ăn uống và lối sống.\n"
                    "Để cải thiện tình trạng này, bạn chỉ cần tuân thủ các phương pháp giảm cân an toàn. Dưới đây là lời khuyên dành cho bạn:\n"
                    "- Tối ưu hóa khẩu phần dinh dưỡng bằng việc tăng cường tiêu thụ protein và chất xơ, đồng thời hạn chế đường và tinh bột trong các bữa ăn hàng ngày. Tránh đồ ăn giàu dầu mỡ và các sản phẩm chế biến sẵn để giảm lượng calo dư thừa.\n"
                    "- Thực hiện các hoạt động thể chất đều đặn để tăng cường đốt cháy năng lượng và loại bỏ mỡ thừa trong cơ thể.\n"
                    "- Loại bỏ thói quen ăn vặt và ăn khuya để kiểm soát lượng calo tiêu thụ hàng ngày. Tránh kiêng cử quá mức, tránh tình trạng mệt mỏi và kích thích cơ thể thích ứng dần với thay đổi.\n"
                    "- Đề xuất kiểm tra cân nặng của bạn mỗi hai tháng một lần để đo lường tiến triển và đảm bảo rằng bạn đang đi đúng hướng về sức khỏe và cân nặng. Vì nó thường dễ mắc các bệnh lý:\n"),
                4: ('Obesity_Type_I', 
                    "Bạn đang ở mức độ **béo phì loại I**, đây là một trạng thái sức khỏe cần được chú ý đặc biệt và đòi hỏi các biện pháp can thiệp tích cực. Những bệnh lý thường gặp như:\n"
                    "1. Tiểu đường, mỡ máu, gan nhiễm mỡ, cao huyết áp hoặc một số bệnh lý về tim mạch, mạch vành và xương khớp.\n"
                    "2. Nguy cơ mắc ung thư cao.\n"
                    "3. Bệnh liên quan đến đường tiêu hoá, đường hô hấp.\n"
                    "4. Bị rối loạn nội tiết tố, nguy cơ vô sinh cao.\n"
                    "5. Dễ bị tai biến hay đột quỵ gây tử vong so với người bình thường.\n"
                    "\nBéo phì không chỉ đe dọa sức khỏe mà còn ảnh hưởng đến tâm lý bởi ngoại hình quá khổ, khiến bạn cảm thấy tự ti, trở nên ngại giao tiếp và xuất hiện trước đám đông. Nó gây ra nhiều trở ngại trong cuộc sống hàng ngày và công việc.\n"
                    "\n**Dưới đây là lời khuyên dành cho bạn:**\n"
                    "- Để cải thiện và duy trì tình trạng sức khỏe ở mức bình thường, hãy điều chỉnh chế độ ăn uống bằng cách giảm lượng chất béo tiêu thụ và tránh ăn kiêng quá mức, để tránh tình trạng mệt mỏi do cơ thể không kịp thích ứng.\n"
                    "- Hãy phát triển thói quen ăn uống lành mạnh bằng cách kiểm soát việc ăn vặt và không ăn vào buổi tối. Kết hợp với việc tập luyện thể dục thường xuyên để đẩy nhanh quá trình đốt cháy mỡ thừa trong cơ thể.\n"
                    "- Tăng cường uống nước và hạn chế sử dụng đồ ăn chế biến sẵn, thay vào đó tập trung vào thực phẩm tươi ngon và giàu dinh dưỡng.\n"
                    "- Việc hỗ trợ từ các chuyên gia dinh dưỡng và bác sĩ là cần thiết để đề ra kế hoạch giảm cân an toàn và hiệu quả. "
                    "Đề xuất kiểm tra cân nặng và tình trạng sức khỏe của bạn thường xuyên hơn, có thể là hàng tháng hoặc theo chỉ dẫn của chuyên gia y tế, "
                    "để theo dõi tiến triển và đảm bảo bạn đang nhận được sự hỗ trợ và chăm sóc phù hợp trong quá trình giảm cân.\n"
                    "\n**Lưu ý**: Trong quá trình giảm cân, hãy tuân thủ phương pháp an toàn và không nên hoảng loạn. Tránh những lời quảng cáo hứa hẹn giảm cân nhanh chóng và chọn những sản phẩm có nguồn gốc rõ ràng. Tìm đến các chuyên gia uy tín để được tư vấn và lựa chọn phương pháp phù hợp nhất cho sức khỏe của bạn."),
                5: ('Obesity_Type_II', 
                    "Bạn đang ở mức độ **béo phì loại II**, đây là một trạng thái sức khỏe nghiêm trọng và đòi hỏi các biện pháp can thiệp ngay lập tức và tích cực.\n"
                    "1. Tiểu đường, mỡ máu, gan nhiễm mỡ, cao huyết áp hoặc một số bệnh lý về tim mạch, mạch vành và xương khớp.\n"
                    "2. Nguy cơ mắc ung thư cao.\n"
                    "3. Bệnh liên quan đến đường tiêu hoá, đường hô hấp.\n"
                    "4. Dễ bị tai biến hay đột quỵ gây tử vong so với người bình thường.\n"
                    "\nBéo phì không chỉ đe dọa sức khỏe mà còn ảnh hưởng đến tâm lý bởi ngoại hình quá khổ, khiến bạn cảm thấy tự ti, trở nên ngại giao tiếp và xuất hiện trước đám đông. Nó gây ra nhiều trở ngại trong cuộc sống hàng ngày và công việc.\n"
                    "\nDưới đây là lời khuyên dành cho bạn:\n"
                    "- Điều chỉnh chế độ ăn uống và tăng cường hoạt động vận động là rất quan trọng để giảm cân và cải thiện sức khỏe.\n"
                    "- Việc hỗ trợ từ các chuyên gia dinh dưỡng, bác sĩ, hoặc các chuyên gia sức khỏe là cần thiết để đề ra kế hoạch giảm cân an toàn và hiệu quả,"
                    " có thể bao gồm cả việc điều trị y tế và tư vấn tâm lý.\n"
                    "- Đề xuất kiểm tra cân nặng và tình trạng sức khỏe của bạn thường xuyên hơn, có thể là hàng tháng hoặc theo chỉ dẫn của chuyên gia y tế, "
                    "để theo dõi tiến triển và đảm bảo bạn đang nhận được sự hỗ trợ và chăm sóc phù hợp trong quá trình giảm cân và quản lý béo phì.\n"
                    "\n**Lưu ý**: Trong quá trình giảm cân, hãy tuân thủ phương pháp an toàn và không nên hoảng loạn. Tránh những lời quảng cáo hứa hẹn giảm cân nhanh chóng và chọn những sản phẩm có nguồn gốc rõ ràng. Tìm đến các chuyên gia uy tín để được tư vấn và lựa chọn phương pháp phù hợp nhất cho sức khỏe của bạn."),
                6: ('Obesity_Type_III', 
                    "Bạn đang ở trạng thái **Béo phì cấp độ III**, đây là một trạng thái sức khỏe cực kỳ nghiêm trọng và đe dọa tính mạng. Những bệnh lý thường gặp:\n"
                    "1. Tiểu đường, mỡ máu, gan nhiễm mỡ, cao huyết áp hoặc một số bệnh lý về tim mạch, mạch vành và xương khớp.\n"
                    "2. Nguy cơ mắc ung thư cao.\n"
                    "3. Bệnh liên quan đến đường tiêu hoá, đường hô hấp.\n"
                    "4. Dễ bị tai biến hay đột quỵ gây tử vong so với người bình thường.\n"
                    "\nĐối với những người ở mức độ này, việc giảm cân không chỉ là một mục tiêu sức khỏe mà còn là một **vấn đề y tế cấp bách**. Các **biện pháp can thiệp** phải được thực hiện **ngay lập tức** và dựa trên một kế hoạch chăm sóc toàn diện.\n"
                    "Điều chỉnh chế độ ăn uống, tăng cường hoạt động thể chất và có thể cần sự can thiệp y tế, bao gồm cả phẫu thuật giảm cân.\n"
                    "Việc hỗ trợ từ các chuyên gia y tế, bao gồm cả bác sĩ, bác sĩ dinh dưỡng, và chuyên gia tâm lý, là cực kỳ quan trọng trong quá trình này.\n"
                    "**Đề xuất kiểm tra cân nặng và tình trạng sức khỏe thường xuyên kết hợp theo dõi chặt chẽ tiến triển dưới sự hướng dẫn của các chuyên gia y tế để đảm bảo an toàn và hiệu quả trong quá trình điều trị.**\n"
                    "\n**Lưu ý**: Trong quá trình giảm cân, hãy tuân thủ phương pháp an toàn và không nên hoảng loạn. Tránh những lời quảng cáo hứa hẹn giảm cân nhanh chóng và chọn những sản phẩm có nguồn gốc rõ ràng. Tìm đến các chuyên gia uy tín để được tư vấn và lựa chọn phương pháp phù hợp nhất cho sức khỏe của bạn.")
            }
            # Hiển thị kết quả dự đoán
            st.subheader("Kết quả dự đoán")
            predicted_label, message = obesity_level_mapping[predicted_obesity_level[0]]
            st.write(f"Mức độ béo phì dự đoán: {predicted_label}")
            st.write(message)
    except ValueError:
        st.error("Vui lòng nhập đầy đủ số hợp lệ cho Tuổi, Chiều cao và Cân nặng. Và nhập số thập phân với dấu chấm (.)")

# Thông tin tác giả
st.sidebar.markdown("---")
st.sidebar.markdown("### Thông tin liên hệ")
st.sidebar.markdown("Tác giả: Hoàng Thu Hồng")
st.sidebar.markdown("MSV: 2051060528")
st.sidebar.markdown("Gmail: hoanghong4505@gmail.com")
st.sidebar.markdown("Version 19.03.02")
