import streamlit as st
import pandas as pd
from Student import Student

# =============================
# 页面配置（前端样式）
# =============================
st.set_page_config(
    page_title="学生管理系统 v2.0",
    layout="wide"
)

# =============================
# 页面标题
# =============================
st.markdown(
    """
    <h2 style="text-align:center;">
        🎓 学生管理系统实践
    </h2>
    """,
    unsafe_allow_html=True
)


# 初始化 session state
def init_session_state():
    # 当前session_id
    if "students" not in st.session_state:
        st.session_state.students = {}
        students = Student.getstudnets()
        st.session_state.students = students


init_session_state()

# =============================
# 左侧边栏（功能菜单）
# =============================
with st.sidebar:
    st.markdown("## 学生管理系统 v2.0")
    st.markdown("---")

    menu = st.radio(
        "请选择操作",
        (
            "1. 添加学员",
            "2. 修改学员",
            "3. 删除学员",
            "4. 查询某个学员",
            "5. 显示所有学员",
            "6. 保存信息",
            "0. 退出系统",
        )
    )

    st.markdown("---")
    st.caption("仅前端展示 · 逻辑待实现")

# =============================
# 主体区域布局
# =============================
left, right = st.columns([2, 3])

# =============================
# 左侧：操作区域（表单样式）
# =============================
with left:
    st.subheader("🛠 操作面板")

    if menu == "1. 添加学员":
        # st.text_input("学号")
        name = st.text_input("姓名")
        age = st.number_input("年龄", 1, 100)
        gender = st.selectbox("性别", ["男", "女"])
        phone = st.text_input("电话")
        desc = st.text_input("描述")
        # st.button("添加学员",key="add_student_button")
        if st.button("添加学员", key="add_student_button"):
            student = Student(name, age, gender,phone, desc)
            # 添加学生
            student.add_student(student)


    elif menu == "2. 修改学员":

        st.subheader("修改学员")

        # ========= 查询输入 =========
        st.text_input("请输入要修改的学员姓名", key="query_name")

        if st.button("查询学员", key="query_student_button2"):
            name = st.session_state.query_name

            if name not in st.session_state.students.keys():
                st.error(f"学员 {name} 不存在，查询失败")
            else:
                student = Student.getstudnetinfo(name)

                # ✅ 查询后：写入 session_state（回显关键）
                st.session_state.edit_name = student["name"]
                st.session_state.edit_age = student["age"]
                st.session_state.edit_gender = student["gender"]
                st.session_state.edit_phone = student["phone"]
                st.session_state.edit_desc = student["desc"]

        # ========= 修改表单（只绑定 key） =========
        if "edit_name" in st.session_state:

            st.text_input("姓名", key="edit_name")
            st.number_input("年龄", 1, 100, key="edit_age")
            st.selectbox("性别", ["男", "女"],key="edit_gender")
            st.text_input("电话", key="edit_phone")
            st.text_input("描述", key="edit_desc")

            st.info(f"当前年龄（实时）：{st.session_state.edit_age}")

            if st.button("确认修改", key="update_student_button"):
                student = Student(
                    st.session_state.edit_name,
                    st.session_state.edit_age,
                    st.session_state.edit_gender,
                    st.session_state.edit_phone,
                    st.session_state.edit_desc
                )
                student.add_student(student)

                st.success(f"学员 {st.session_state.edit_name} 修改成功")


    elif menu == "3. 删除学员":
        name = st.text_input("姓名")
        # st.button("删除学员",key="del_student_button")
        if st.button("删除学员",key="del_student_button"):
            if name not in st.session_state.students.keys():
                st.error(f"学员{name}不存在,删除失败")
            else:
                Student.delete_student(name)
                st.info(f"学员{name}删除成功")

    elif menu == "4. 查询某个学员":
        name = st.text_input("姓名")
        # st.button("查询学员",key="query_student_button")
        if st.button("查询学员",key="query_student_button"):
            if name not in st.session_state.students.keys():
                # st.error(f"学生信息：{st.session_state.students.keys()}")
                st.error(f"学员{name}不存在,查询失败")
            else:
                student = Student.getstudnetinfo(name)
                # st.info(student)
                st.subheader("📋 学员信息")
                # 占位表格（仅样式）
                placeholder_ds = pd.DataFrame(
                    {
                        "姓名": [student["name"]],
                        "年龄": [student["age"]],
                        "性别": [student["gender"]],
                        "电话": [student["phone"]],
                        "描述": [student["desc"]],
                    }
                )
                st.dataframe(
                    placeholder_ds,
                    use_container_width=True
                )

    elif menu == "5. 显示所有学员":
        st.info("右侧显示所有学员信息")

    elif menu == "6. 保存信息":
        if st.button("保存信息",key="save_student_button"):
            Student.save_students()
            st.info("右侧显示所有学员信息")

    elif menu == "0. 退出系统":
        st.warning("关闭浏览器页面即可退出系统")

# =============================
# 右侧：信息展示区域（表格样式）
# =============================
with right:
    st.subheader("📋 学员信息展示区")

    name_list = []
    age_list = []
    gender_list = []
    phone_list = []
    desc_list = []
    for value in st.session_state.students.values():
        name_list.append(value["name"])
        age_list.append(value["age"])
        gender_list.append(value["gender"])
        phone_list.append(value["phone"])
        desc_list.append(value["desc"])

    # 占位表格（仅样式）
    placeholder_df = pd.DataFrame(
        {
            "姓名": name_list,
            "年龄": age_list,
            "性别": gender_list,
            "电话": phone_list,
            "描述": desc_list,
        }
    )

    st.dataframe(
        placeholder_df,
        use_container_width=True
    )
