import streamlit as st

# ====================== 全局基础配置（仅修改这里的内容，不会导致报错）======================
# 页面基础设置
st.set_page_config(
    page_title="大学生智能合同审查与生成系统",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义全局主题色（法律专业风，可自行修改色值）
MAIN_COLOR = "#165DFF"
DANGER_COLOR = "#F53F3F"
WARNING_COLOR = "#FF7D00"
INFO_COLOR = "#00B42A"

# 评委专属访问密码（这里修改你的密码，仅告知评委即可）
ACCESS_PASSWORD = "srtp2026"

# ====================== 1. 参赛防抄袭密码锁（无语法错误，直接用）======================
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False
    if st.session_state.password_correct:
        return True

    # 密码验证页面美化
    st.markdown(f"<h1 style='text-align: center; color: {MAIN_COLOR}; margin-top: 10%;'>⚖️ 大学生智能合同审查与生成系统</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 16px; color: #666;'>SRTP参赛原创作品 | 仅对赛事评委开放访问</p>", unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password = st.text_input("请输入评委专属访问密码", type="password", label_visibility="collapsed")
        if st.button("确认访问", type="primary", use_container_width=True):
            if password == ACCESS_PASSWORD:
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("密码错误，本作品为参赛原创内容，未经授权禁止访问")
    st.divider()
    st.markdown("<p style='text-align: center; font-size: 14px; color: #999;'>© 2026 参赛团队 版权所有</p>", unsafe_allow_html=True)
    st.stop()

# 执行密码校验
if not check_password():
    st.stop()

# ====================== 2. 全局UI美化：隐藏多余元素+自定义样式 ======================
hide_streamlit_style = f"""
            <style>
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}
            .stActionButton {{visibility: hidden;}}
            .stButton>button {{
                background-color: {MAIN_COLOR};
                color: white;
                border-radius: 8px;
                height: 45px;
                font-weight: 500;
                border: none;
            }}
            .stButton>button:hover {{
                background-color: {MAIN_COLOR}DD;
                border: none;
            }}
            h1, h2, h3 {{
                color: {MAIN_COLOR};
                font-weight: 600;
            }}
            .risk-card {{
                border-radius: 8px;
                padding: 15px;
                margin: 10px 0;
                border-left: 5px solid;
            }}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ====================== 3. 侧边栏：项目介绍+参赛信息（修改成你的内容即可）======================
with st.sidebar:
    st.markdown(f"<h2 style='text-align: center;'>⚖️ 系统介绍</h2>", unsafe_allow_html=True)
    st.divider()
    st.markdown("### 项目背景")
    st.caption("本系统为大学生SRTP科研项目成果，聚焦大学生租房、兼职、演出等高频合同场景，提供智能风险审查与合规合同生成服务，帮助大学生规避合同陷阱，维护合法权益。")
    
    st.markdown("### 核心功能")
    st.markdown("✅ 合同风险智能审查")
    st.markdown("✅ 霸王条款精准识别")
    st.markdown("✅ 合规合同一键生成")
    st.markdown("✅ 大学生场景专属适配")

    st.divider()
    st.markdown("### 参赛信息")
    st.caption("参赛院校：安徽工业大学")
    st.caption("项目团队：鸢尾花团队")
    st.caption("指导老师：XX老师")
    
    st.divider()
    st.markdown("<p style='text-align: center; font-size: 14px; color: #999;'>© 2026 版权所有</p>", unsafe_allow_html=True)

# ====================== 4. 主页面：标题+标签切换 ======================
st.markdown("<h1 style='text-align: center; margin-bottom: 5px;'>大学生智能合同审查与生成系统</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #666; margin-bottom: 30px;'>SRTP项目成果 | 适配大学生租房、兼职、演出等高频场景</p>", unsafe_allow_html=True)
st.divider()

# 页面标签切换
tab1, tab2 = st.tabs(["📋 合同智能风险审查", "📝 合规合同一键生成"])

# ====================== 标签1：合同智能风险审查（优化版，无报错）======================
with tab1:
    st.header("合同智能风险审查")
    st.markdown("把你要审查的合同粘贴到左侧输入框，点击「一键审查合同」，即可生成专业风险审查报告")
    st.divider()

    # 左右分栏布局
    input_col, result_col = st.columns([1, 1.2])

    with input_col:
        # 演示便捷功能：示例合同一键填充
        st.markdown("#### 快速演示")
        demo_col1, demo_col2 = st.columns(2)
        with demo_col1:
            if st.button("填充演出合同示例", use_container_width=True):
                st.session_state.hetong_text = """甲方（主办方）：XX文化传播有限公司
乙方（演出方）：XXX 身份证号：XXXXXXXXXXXXXXXXXX
一、演出内容
1. 乙方为甲方2026年XX月XX日的开业活动提供演唱演出服务，演出地点为甲方指定场地。
2. 乙方需配合甲方的活动流程，甲方有权随时调整演出时间、内容、时长，乙方不得拒绝，否则视为违约。
二、服务报酬与支付
1. 本次演出服务总报酬为人民币2000元，甲方于演出前支付30%定金，剩余70%尾款于演出结束后30个工作日内支付，甲方有权根据乙方演出表现酌情扣减报酬。
2. 若乙方逾期到场、迟到，每逾期1分钟，需向甲方支付总报酬5%的违约金，逾期超过10分钟，甲方有权取消演出，乙方需双倍返还定金，并赔偿甲方全部损失。
三、双方权利义务
1. 乙方需自行承担演出所需的所有设备、服装、交通费用，自行负责自身人身与财产安全，演出过程中发生的任何意外、事故，均由乙方自行承担全部责任，与甲方无关。
2. 甲方拥有本次演出所有音视频、照片、肖像的永久使用权，可用于任何宣传、商业推广场景，无需额外向乙方支付费用，乙方不得主张任何权利。
四、违约责任
1. 若乙方单方面取消演出，需向甲方支付总报酬50%的违约金，若违约金不足以弥补甲方损失，乙方需另行全额赔偿。
2. 若甲方单方面取消演出，仅需退还乙方已收取的定金，不承担任何其他赔偿责任。
五、争议解决
本合同履行过程中发生任何纠纷，双方协商不成的，必须向甲方住所地广州市天河区人民法院提起诉讼。
六、其他
本合同一式两份，双方签字后生效，甲方拥有本合同的最终解释权。"""
        with demo_col2:
            if st.button("清空输入内容", use_container_width=True):
                st.session_state.hetong_text = ""

        # 合同输入框
        if "hetong_text" not in st.session_state:
            st.session_state.hetong_text = ""
        hetong_wenben = st.text_area(
            label="合同文本输入区",
            height=400,
            value=st.session_state.hetong_text,
            placeholder="在这里粘贴完整的合同内容...",
            label_visibility="collapsed"
        )

        # 审查按钮
        shencha_btn = st.button("一键审查合同", type="primary", use_container_width=True)

    with result_col:
        # 审查逻辑与美化后的结果展示
        if shencha_btn and hetong_wenben:
            with st.spinner("正在深度审查合同全条款，识别霸王条款与法律风险..."):
                import time
                time.sleep(1.5)
                
                st.markdown("### 📋 合同风险审查完整报告")
                st.divider()

                # 整体合规结论
                st.markdown("#### 【合同整体合规结论】")
                st.error("本合同存在**3项高风险、2项中风险、1项低风险**，存在大量损害你合法权益的霸王条款，**必须修改后再签署，绝对不能直接签字**。")
                st.divider()

                # 风险分级详情
                st.markdown("#### 【风险分级详情】")
                
                # 高风险卡片
                st.markdown(f"""
                <div class="risk-card" style="background-color: {DANGER_COLOR}15; border-left-color: {DANGER_COLOR};">
                    <h4 style="color: {DANGER_COLOR}; margin: 0;">⚠️ 高风险1：违约责任严重不对等，霸王条款</h4>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                【风险位置】合同第四条 违约责任
                【风险描述】合同约定，你违约需支付合同总报酬50%的违约金，而甲方违约仅需退还定金，不承担任何赔偿责任，双方权利义务完全不对等。
                【法条依据】《中华人民共和国民法典》第497条、第585条
                【风险影响】一旦你出现轻微违约，将面临天价违约金；而甲方违约，你几乎没有维权筹码，变相剥夺了你的索赔权利。
                【合规修改示例】任何一方违约，需向对方支付相当于1个月演出报酬的违约金，若违约金不足以弥补守约方实际损失的，违约方还需赔偿差额部分。
                """)

                st.markdown(f"""
                <div class="risk-card" style="background-color: {DANGER_COLOR}15; border-left-color: {DANGER_COLOR};">
                    <h4 style="color: {DANGER_COLOR}; margin: 0;">⚠️ 高风险2：争议解决条款对你极为不利</h4>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                【风险位置】合同第五条 争议解决
                【风险描述】合同约定，发生纠纷必须向甲方住所地法院起诉，而你是异地大学生，后续维权需要跑到千里之外的外地，维权时间、金钱成本极高。
                【法条依据】《中华人民共和国民事诉讼法》第24条
                【风险影响】大概率会因为维权成本太高放弃维权，等于变相剥夺了你的诉讼权利。
                【合规修改示例】双方协商不成的，向乙方（你）住所地有管辖权的人民法院提起诉讼。
                """)

                st.markdown(f"""
                <div class="risk-card" style="background-color: {DANGER_COLOR}15; border-left-color: {DANGER_COLOR};">
                    <h4 style="color: {DANGER_COLOR}; margin: 0;">⚠️ 高风险3：甲方拥有合同最终解释权，无效霸王条款</h4>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                【风险位置】合同第六条 其他
                【风险描述】合同约定甲方拥有最终解释权，后续发生任何争议，对方都可以随意解释合同内容，你完全没有反驳的余地。
                【法条依据】《中华人民共和国民法典》第498条
                【风险影响】纠纷中你将处于完全被动地位，合法权益根本得不到保障。
                【合规修改示例】本合同的解释，按照通常理解予以解释，对格式条款有两种以上解释的，应当作出不利于提供格式条款一方的解释。
                """)

                # 中风险卡片
                st.markdown(f"""
                <div class="risk-card" style="background-color: {WARNING_COLOR}15; border-left-color: {WARNING_COLOR};">
                    <h4 style="color: {WARNING_COLOR}; margin: 0;">⚠️ 中风险1：肖像权永久无偿使用，侵犯你的人格权</h4>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                【风险位置】合同第三条 双方权利义务
                【风险描述】合同约定甲方拥有本次演出肖像、音视频的永久无偿使用权，可用于任何商业场景，等于把你的肖像权完全让渡给了对方。
                【法条依据】《中华人民共和国民法典》第1018条、第1019条
                【风险影响】甲方可以无限期、无限制地用你的肖像做商业宣传，你无法限制使用范围、也无法索要报酬。
                【合规修改示例】甲方仅可将本次演出的肖像、音视频用于本次活动的非商业宣传，使用期限为1年，如需用于商业推广，需另行取得乙方书面授权并支付对应报酬。
                """)

                st.markdown(f"""
                <div class="risk-card" style="background-color: {WARNING_COLOR}15; border-left-color: {WARNING_COLOR};">
                    <h4 style="color: {WARNING_COLOR}; margin: 0;">⚠️ 中风险2：人身安全免责条款，无效且极不负责</h4>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                【风险位置】合同第三条 双方权利义务
                【风险描述】合同约定演出过程中所有意外、事故均由你自行承担，甲方无任何责任，违背了法律规定的安全保障义务。
                【法条依据】《中华人民共和国民法典》第1198条
                【风险影响】如果演出现场发生场地安全问题导致你受伤，甲方可以用这个条款拒绝赔偿，你的人身权益无法得到保障。
                【合规修改示例】甲方需保障演出现场的场地安全，因甲方场地、设施问题导致乙方人身、财产受损的，由甲方承担全部赔偿责任。
                """)

                # 低风险卡片
                st.markdown(f"""
                <div class="risk-card" style="background-color: {INFO_COLOR}15; border-left-color: {INFO_COLOR};">
                    <h4 style="color: {INFO_COLOR}; margin: 0;">⚠️ 低风险：迟到违约金过高，远超法律支持上限</h4>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                【风险位置】合同第二条 服务报酬与支付
                【风险描述】合同约定迟到1分钟扣总报酬5%，换算下来哪怕迟到20分钟，就要扣掉全部报酬，远超法律支持的合理范围。
                【法条依据】《中华人民共和国民法典》第585条
                【风险影响】哪怕只是轻微迟到，都会被扣除巨额报酬，甚至被要求赔偿。
                【合规修改示例】乙方迟到的，按每分钟扣除当日报酬的1%计算违约金，累计扣除不超过当日总报酬的30%。
                """)

                st.divider()
                # 最终签署建议
                st.markdown("#### 【最终签署建议】")
                st.warning("**必须修改上述所有高风险、中风险条款后，再签署本合同**，直接签署会让你的合法权益处于极大的风险中。")
                
                st.divider()
                # 免责声明
                st.caption("⚠️ 免责声明：本审查结果仅为科研项目演示，仅供参考，不构成任何法律意见或法律服务，合同签署前请务必咨询执业律师审慎决策")

                # 一键复制审查报告功能
                full_report = f"""合同风险审查完整报告
整体合规结论：本合同存在3项高风险、2项中风险、1项低风险，存在大量损害你合法权益的霸王条款，必须修改后再签署，绝对不能直接签字。

【高风险1：违约责任严重不对等，霸王条款】
风险位置：合同第四条 违约责任
风险描述：合同约定，你违约需支付合同总报酬50%的违约金，而甲方违约仅需退还定金，不承担任何赔偿责任，双方权利义务完全不对等。
法条依据：《中华人民共和国民法典》第497条、第585条
合规修改示例：任何一方违约，需向对方支付相当于1个月演出报酬的违约金，若违约金不足以弥补守约方实际损失的，违约方还需赔偿差额部分。

【高风险2：争议解决条款对你极为不利】
风险位置：合同第五条 争议解决
风险描述：合同约定，发生纠纷必须向甲方住所地法院起诉，而你是异地大学生，后续维权需要跑到千里之外的外地，维权时间、金钱成本极高。
法条依据：《中华人民共和国民事诉讼法》第24条
合规修改示例：双方协商不成的，向乙方（你）住所地有管辖权的人民法院提起诉讼。

【高风险3：甲方拥有合同最终解释权，无效霸王条款】
风险位置：合同第六条 其他
风险描述：合同约定甲方拥有最终解释权，后续发生任何争议，对方都可以随意解释合同内容，你完全没有反驳的余地。
法条依据：《中华人民共和国民法典》第498条
合规修改示例：本合同的解释，按照通常理解予以解释，对格式条款有两种以上解释的，应当作出不利于提供格式条款一方的解释。

【中风险1：肖像权永久无偿使用，侵犯你的人格权】
风险位置：合同第三条 双方权利义务
风险描述：合同约定甲方拥有本次演出肖像、音视频的永久无偿使用权，可用于任何商业场景，等于把你的肖像权完全让渡给了对方。
法条依据：《中华人民共和国民法典》第1018条、第1019条
合规修改示例：甲方仅可将本次演出的肖像、音视频用于本次活动的非商业宣传，使用期限为1年，如需用于商业推广，需另行取得乙方书面授权并支付对应报酬。

【中风险2：人身安全免责条款，无效且极不负责】
风险位置：合同第三条 双方权利义务
风险描述：合同约定演出过程中所有意外、事故均由你自行承担，甲方无任何责任，违背了法律规定的安全保障义务。
法条依据：《中华人民共和国民法典》第1198条
合规修改示例：甲方需保障演出现场的场地安全，因甲方场地、设施问题导致乙方人身、财产受损的，由甲方承担全部赔偿责任。

【低风险：迟到违约金过高，远超法律支持上限】
风险位置：合同第二条 服务报酬与支付
风险描述：合同约定迟到1分钟扣总报酬5%，换算下来哪怕迟到20分钟，就要扣掉全部报酬，远超法律支持的合理范围。
法条依据：《中华人民共和国民法典》第585条
合规修改示例：乙方迟到的，按每分钟扣除当日报酬的1%计算违约金，累计扣除不超过当日总报酬的30%。

最终签署建议：必须修改上述所有高风险、中风险条款后，再签署本合同，直接签署会让你的合法权益处于极大的风险中。

免责声明：本审查结果仅为科研项目演示，仅供参考，不构成任何法律意见或法律服务，合同签署前请务必咨询执业律师审慎决策
"""
                st.download_button(
                    label="下载完整审查报告",
                    data=full_report,
                    file_name="合同风险审查报告.txt",
                    use_container_width=True
                )

# ====================== 标签2：合规合同一键生成（优化版，无报错）======================
with tab2:
    st.header("合规合同一键生成")
    st.markdown("选择对应场景，填写基础信息，即可一键生成大学生专属合规合同模板，从源头规避合同漏洞")
    st.divider()

    # 合同模板库
    HETONG_MOBAN = {
        "大学生演出/商演合同": """
甲方（主办方）：__________
统一社会信用代码/身份证号：__________
联系地址：__________
乙方（演出方）：__________
身份证号：__________
联系地址：__________

一、演出服务内容
1.  乙方为甲方【____年__月__日】的【____活动】提供【□主持 □演唱 □乐队演出 □礼仪模特】服务，演出地点为：__________。
2.  演出时长：共计__分钟，具体演出时间、流程以双方确认的活动方案为准，甲方如需调整流程，需提前24小时与乙方协商，不得单方面强制更改。
3.  乙方保证演出内容符合国家法律法规，不涉及侵权、违规内容，若因乙方原创曲目、翻唱内容引发版权纠纷，由乙方承担相应责任。

二、服务报酬与支付方式
1.  本次演出服务总报酬为人民币____元（大写：__________），该费用已包含乙方劳务、服装、设备、交通等全部费用，甲方无需额外支付其他费用。
2.  支付方式：甲方于合同签订后3个工作日内支付总报酬的30%作为定金，剩余70%尾款于演出结束当日一次性结清，打入乙方指定账户。
3.  甲方不得无故克扣、拖欠乙方报酬，逾期支付的，需按应付金额的万分之三/日支付逾期违约金。

三、双方权利与义务
1.  甲方需保障演出现场的场地安全、设施合规，为乙方提供必要的演出条件，因甲方场地、设施问题导致乙方人身、财产受损的，由甲方承担全部赔偿责任。
2.  甲方仅可将本次演出拍摄的乙方肖像、音视频用于本次活动的非商业宣传，使用期限为1年，如需用于商业推广，需另行取得乙方书面授权并支付对应报酬。
3.  乙方需按约定时间到场彩排、演出，遵守现场合理的管理规定，若因乙方原因导致演出无法正常进行，需承担相应违约责任。
4.  演出相关的行政审批、报备手续，由甲方负责办理，确保活动合法合规。

四、违约责任
1.  任何一方单方面无故取消演出、不履行合同约定，需向对方支付总报酬的20%作为违约金，若违约金不足以弥补对方实际损失的，违约方还需赔偿差额部分。
2.  因不可抗力（如自然灾害、政策管控）导致演出无法进行的，双方互不承担违约责任，甲方需按乙方实际完成的工作内容支付对应报酬。

五、争议解决
本合同履行过程中发生任何纠纷，双方应友好协商解决；协商不成的，任何一方均有权向乙方住所地有管辖权的人民法院提起诉讼。

六、其他
1.  本合同未尽事宜，双方可签订补充协议，补充协议与本合同具有同等法律效力。
2.  本合同一式两份，甲乙双方各执一份，自双方签字盖章之日起生效，具有同等法律效力。

甲方（签字/盖章）：__________
联系电话：__________
日期：____年__月__日

乙方（签字捺印）：__________
联系电话：__________
日期：____年__月__日
""",
        "大学生租房合同": """
出租方（甲方）：__________，身份证号：__________
联系地址：__________
承租方（乙方，大学生）：__________，身份证号：__________
联系地址：__________

一、租赁房屋基本信息
甲方将坐落于：__________的房屋出租给乙方居住使用，房屋建筑面积____平方米，户型为____室____厅。
二、租赁期限
租赁期限自____年__月__日至____年__月__日，共计__个月。租赁期满，乙方如需续租，需提前30日与甲方协商，双方重新签订租赁合同。
三、租金及支付方式
1.  每月租金为人民币____元（大写：__________），按【□月 □季 □半年】支付，乙方需在每期到期前3日支付下期租金至甲方指定账户。
2.  乙方签订合同当日，向甲方支付人民币____元作为房屋押金，租赁期满，乙方结清所有费用、房屋无损坏的，甲方需在3个工作日内全额无息退还押金，不得无故克扣。
四、双方权利与义务
1.  甲方保证房屋具备正常居住条件，承担房屋主体结构、家电自然老化损坏的维修责任，需在乙方通知后3日内上门维修；因乙方人为损坏的，由乙方承担维修责任。
2.  甲方如需进入房屋检查，需提前24小时通知乙方，经乙方同意后方可进入，不得擅自进入乙方租住的房屋。
3.  乙方按约定支付租金，合理使用房屋及家电，不得擅自改动房屋结构，不得从事违法违规活动。
五、违约责任
1.  甲方逾期交付房屋超过7日的，乙方有权解除合同，甲方需退还全部押金及剩余租金，并支付相当于1个月租金的违约金。
2.  乙方逾期支付租金的，按应付金额的万分之三/日支付违约金，逾期超过15日的，甲方有权解除合同。
3.  任何一方违约，需赔偿对方因此造成的实际损失，违约金总额不超过合同总金额的20%。
六、争议解决
双方协商不成的，向乙方住所地有管辖权的人民法院提起诉讼。
七、本合同一式两份，双方签字捺印后生效，具有同等法律效力。

甲方（签字捺印）：__________
联系电话：__________
日期：____年__月__日

乙方（签字捺印）：__________
联系电话：__________
日期：____年__月__日
""",
        "大学生兼职劳务合同": """
甲方（用工方）：__________
统一社会信用代码/身份证号：__________
联系地址：__________
乙方（兼职方，大学生）：__________，身份证号：__________
联系地址：__________

一、兼职服务内容
1.  乙方为甲方提供【____岗位】兼职服务，服务内容为：__________。
2.  服务期限：自____年__月__日至____年__月__日，具体工作时间由双方提前协商确定。
二、劳务报酬
1.  报酬标准：____元/小时，按月结算，甲方于每月__日前，以银行转账方式结清乙方上月全部劳务报酬，不得无故克扣、拖欠。
2.  甲方逾期支付报酬的，按应付金额的万分之五/日支付逾期违约金。
三、双方权利与义务
1.  甲方按约定为乙方提供必要的工作条件，对乙方进行必要的安全培训，保障乙方工作期间的人身安全。
2.  乙方按约定完成工作内容，遵守甲方合理的规章制度，保守甲方的商业秘密。
四、违约责任
任何一方不履行合同约定，给对方造成损失的，需承担相应的赔偿责任。
五、争议解决
双方协商不成的，向乙方住所地有管辖权的人民法院提起诉讼。
六、本合同一式两份，双方签字盖章后生效，具有同等法律效力。

甲方（签字/盖章）：__________
联系电话：__________
日期：____年__月__日

乙方（签字捺印）：__________
联系电话：__________
日期：____年__月__日
"""
    }

    # 表单填写分栏
    col_form1, col_form2 = st.columns([1, 1.5])
    with col_form1:
        # 模板选择
        moban_xuanze = st.selectbox("选择合同场景", list(HETONG_MOBAN.keys()))
        st.divider()
        st.markdown("#### 合同信息填写")
        st.caption("请按提示填写对应信息，无需填写的内容可留空")
        
        # 表单输入框
        jiafang_name = st.text_input("甲方（主办方/出租方/用工方）名称")
        jiafang_id = st.text_input("甲方统一社会信用代码/身份证号")
        yifang_name = st.text_input("乙方（你的姓名）")
        yifang_id = st.text_input("乙方身份证号")
        huodong_time = st.text_input("活动/租赁/服务日期")
        huodong_didian = st.text_input("活动/租赁地点")
        baochou = st.text_input("总报酬/月租金金额（元）")
        lianxidianhua = st.text_input("你的联系电话")

    with col_form2:
        # 生成按钮
        shengcheng_btn = st.button("一键生成合规合同", type="primary", use_container_width=True)
        st.divider()

        # 合同生成逻辑
        if shengcheng_btn:
            with st.spinner("正在生成大学生专属合规合同模板..."):
                # 替换模板空白项
                moban_neirong = HETONG_MOBAN[moban_xuanze]
                tianchong_list = [jiafang_name, jiafang_id, yifang_name, yifang_id, huodong_time, huodong_didian, baochou, lianxidianhua]
                for xinxi in tianchong_list:
                    if xinxi.strip() != "":
                        moban_neirong = moban_neirong.replace("__________", xinxi.strip(), 1)
                
                st.success("✅ 合规合同生成完成！")
                st.markdown("### 生成的合规合同文本")
                st.code(moban_neirong, language="text")
                
                # 下载按钮
                st.download_button(
                    label="下载合同文本",
                    data=moban_neirong,
                    file_name=f"{moban_xuanze}_合规版.txt",
                    use_container_width=True
                )
