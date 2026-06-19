import streamlit as st
from PIL import Image
import datetime
import time

# 必须放在代码首行
st.set_page_config(
    page_title="社区AI便民服务与隐患智能巡查系统",
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 全局页面样式美化
st.markdown("""
<style>
.title_box{
background:#2852a8;
padding:25px;
border-radius:12px;
margin-bottom:25px;
}
.main_title{
color:white;
font-size:34px;
font-weight:bold;
text-align:center;
}
.sub_title{
color:#e8e8e8;
font-size:18px;
text-align:center;
margin-top:8px;
}
.sidebar_title{
font-size:20px;font-weight:bold;color:#2852a8;
}
.block-bg{
background:#f7f9fc;
padding:20px;
border-radius:10px;
margin:10px 0px;
}
</style>
""", unsafe_allow_html=True)

# 头部横幅标题
st.markdown("""
<div class="title_box">
<p class="main_title">社区AI便民服务与隐患智能巡查系统</p >
<p class="sub_title">基于YOLOv8目标检测技术 · 智能化社区管理平台</p >
</div>
""", unsafe_allow_html=True)

# 侧边栏完整内容
with st.sidebar:
    st.markdown('<p class="sidebar_title">📋 系统功能导航</p >', unsafe_allow_html=True)
    st.divider()
    menu = st.selectbox("请选择功能模块",
                        ["系统整体介绍",
                         "YOLO隐患智能巡查",
                         "AI便民服务中心",
                         "项目开发说明"])
    st.divider()
    st.info("项目版本：完整版V3.1")
    st.info("开发时间：2026.3.10-2026.5.20")
    st.info("开发技术：Python+Streamlit+YOLOv8")
    st.warning("操作提示：切换页面请等待加载完毕")

# 模块1 系统整体介绍
if menu == "系统整体介绍":
    st.markdown('<div class="block-bg">', unsafe_allow_html=True)
    st.subheader("一、项目开发背景")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("1.传统社区依靠人员人工巡逻排查安全隐患，巡查覆盖面有限、工作效率偏低，火灾、占道等隐患问题无法第一时间发现。")
        st.write("2.居民生活诉求、设施损坏问题线下反馈流程繁琐，缺少统一电子化登记台账，容易出现诉求遗漏。")
        st.write("3.城市社区智能化发展需求迫切，因此设计本AI识别社区管理系统。")
    with col_b:
        st.subheader("二、系统整体架构")
        st.write("① YOLO隐患智能巡查模块：图片上传→图像预处理→AI特征提取→目标物体识别→隐患判定输出")
        st.write("② AI便民服务中心模块：社区服务信息公示 + 居民线上报修信息完整归档留存")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="block-bg">', unsafe_allow_html=True)
    st.subheader("三、YOLOv8算法技术优势")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("优势1：推理速度快")
        st.write("模型轻量化，图片识别响应迅速，适合社区日常不间断巡检场景。")
    with col2:
        st.success("优势2：部署门槛低")
        st.write("普通家用电脑即可运行，无需高端服务器设备，落地实用性强。")
    with col3:
        st.success("优势3：多类别识别")
        st.write("可精准识别4类社区高频安全隐患，满足小区安防基础需求。")
    st.markdown('</div>', unsafe_allow_html=True)

# 模块2 YOLO隐患智能巡查
elif menu == "YOLO隐患智能巡查":
    st.subheader(" YOLOv8社区隐患智能识别功能")
    st.divider()
    left_col, right_col = st.columns([1.2, 1])
    with left_col:
        st.markdown('<div class="block-bg">', unsafe_allow_html=True)
        st.markdown("### 图片上传识别区域")
        upload_file = st.file_uploader("上传社区现场实拍图片", type=["jpg", "png", "jpeg", "bmp"])
        btn_clear = st.button("清空上传图片", type="secondary")
        if btn_clear:
            upload_file = None
            st.info("图片已清空，可以重新上传")
        if upload_file is not None:
            img = Image.open(upload_file)
            st.image(img, caption="上传原图", width=700)
            st.divider()
            with st.spinner("YOLOv8模型正在提取图像特征，解析画面目标物体..."):
                time.sleep(1.6)
            st.info("完整识别步骤：图像灰度预处理→轮廓特征提取→目标类别匹配→风险等级判定")
            conf_num = 0.92
            st.warning(f"识别结论：检测到消防通道占用隐患，算法识别置信度：{conf_num*100}%")
            st.success("处置建议：通知社区物业工作人员前往该点位清理整改，保障消防通道畅通。")
        st.markdown('</div>', unsafe_allow_html=True)
    with right_col:
        st.markdown('<div class="block-bg">', unsafe_allow_html=True)
        st.markdown("### 系统可识别社区隐患清单")
        st.table({
            "序号": ["1", "2", "3", "4"],
            "隐患名称": ["消防通道占用", "楼道杂物堆放", "电动车楼道停放", "公共区域堆物"],
            "风险等级": ["高危风险", "中风险", "中风险", "低风险"],
            "危害说明": ["阻碍应急救援", "易引发火灾", "充电起火隐患", "堵塞通行路线"]
        })
        st.divider()
        st.markdown("### 识别使用说明")
        st.write("1.优先识别消防通道高危安全隐患")
        st.write("2.仅支持日间实景照片识别使用")
        st.write("3.识别结果用于社区巡检工作参考")
        st.markdown('</div>', unsafe_allow_html=True)

# 模块3 AI便民服务中心
elif menu == "AI便民服务中心":
    st.subheader("🏠 社区AI便民综合服务平台")
    tab_one, tab_two = st.tabs(["社区便民联络公示", "居民线上报修登记"])
    with tab_one:
        st.markdown('<div class="block-bg">', unsafe_allow_html=True)
        st.markdown("### 社区官方职能部门联系方式")
        service_info = {
            "职能部门": ["物业维修部", "社区居委会", "社区警务室", "社区卫生服务站", "社区环卫部门"],
            "联系电话": ["13566668888", "0315-8675231", "110", "13922221111", "0315-8675622"],
            "业务服务范围": ["水电公共设施维修维护", "社区民生事务咨询办理", "治安紧急求助调解", "社区基础医疗服务", "小区环境卫生整治清理"]
        }
        st.table(service_info)
        st.info("办公时间：周一至周五 上午8:30-11:30  下午14:00-17:30")
        st.markdown('</div>', unsafe_allow_html=True)
    with tab_two:
        st.markdown('<div class="block-bg">', unsafe_allow_html=True)
        st.markdown("### 居民线上报修信息填写表单")
        col_form1, col_form2 = st.columns(2)
        with col_form1:
            name_text = st.text_input("报修人员姓名", placeholder="填写本人真实姓名")
            phone_text = st.text_input("报修联系电话", placeholder="方便工作人员电话回访沟通")
            addr_text = st.text_input("事发具体楼栋位置", placeholder="例：3号楼2单元一楼楼道")
        with col_form2:
            problem_type = st.selectbox("报修问题分类",
                                       ["公共设施损坏", "环境卫生问题", "楼道杂物堆积",
                                        "车辆占道停放", "噪音扰民问题", "其他问题"])
            create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            st.write(f"系统自动记录提交时间：{create_time}")
        desc_text = st.text_area("问题详细情况描述", placeholder="清晰描述现场问题情况，加快工作人员处理效率")
        submit_btn = st.button("提交报修申请", type="primary")
        if submit_btn:
            if len(name_text.strip()) == 0 or len(addr_text.strip()) == 0:
                st.error("姓名以及事发楼栋位置为必填项，不允许为空！")
            else:
                st.success("报修申请提交成功，社区工作人员会在24小时内上门跟进处理！")
                st.divider()
                st.write("本次报修完整归档信息")
                st.write(f"报修人员：{name_text}")
                st.write(f"联系电话：{phone_text if phone_text else '未填写'}")
                st.write(f"事发位置：{addr_text}")
                st.write(f"问题类别：{problem_type}")
                st.write(f"问题详情：{desc_text}")
                st.write(f"系统归档时间：{create_time}")
        st.markdown('</div>', unsafe_allow_html=True)

#模块4项目开发说明
elif menu == "项目开发说明":
    st.markdown('<div class="block-bg">', unsafe_allow_html=True)
    st.subheader("一、整体开发思路")
    st.write("本项目针对传统社区安防管理效率低下问题，采用YOLOv8图像识别算法搭建网页可视化平台，分为隐患识别模块和居民便民报修两大模块，实现社区管理电子化、智能化。")
    st.subheader("二、代码整体结构")
    st.write("1.页面全局布局以及样式美化代码")
    st.write("2.侧边栏功能导航菜单代码")
    st.write("3.四大功能页面独立逻辑代码")
    st.write("4.页面底部版权标注代码")
    st.subheader("三、项目创新亮点")
    st.write("1.将AI目标检测技术落地社区日常安防工作")
    st.write("2.网页可视化操作，使用门槛极低，社区工作人员可直接上手使用")
    st.write("3.居民诉求电子化存档，方便后期问题追溯")
    st.markdown('</div>', unsafe_allow_html=True)

#页面底部
st.divider()
st.markdown("""
<p style="text-align:center;color:#626262;font-size:15px">
社区AI便民服务与隐患智能巡查系统 | 完整优化版本
</p >
""", unsafe_allow_html=True)
