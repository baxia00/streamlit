import streamlit as st
import streamlit.components.v1 as components
from get_rel_url import *


#隐藏 ainMenu footer按钮
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#左边栏
with st.sidebar:
    st.header("杨柏大峡谷")
    st.markdown("""杨柏大峡谷位于山西省晋城市阳城县河北镇境内。一条秋川河顺峡谷静静流淌，经久不息。峡谷，两侧山崖陡峭，从谷底往上望去，高约700余米的山崖倾之势，嶙刚的怪石，苍莽的草木,使这里的景色显得颇为壮观。
距阳城县城42公里的河北镇，一条主峡和十几条附峡组成一个峡谷群,各个峡谷常年流水淙淙,一幅独特的太行山水风貌。杨柏大峡谷植被茂盛,草木种类丰富,可与蟒河自然保护区相比,杨柏大峡谷所处的西南山系,以析城山为主,无论是自然风光,地质构造还是植被方面,都有很高的价值。
杨柏大峡谷是析城山景区的一部分，分为：大峡谷，后龛庙、灵泉洞、析城山、五斗峰等。五斗峰又名五指山、五斗山，位于阳城县河北镇后龛村，其环周奇峰耸立，绝壁如削，乔木遍布，灌木丛生，顶峰海拔1772米，比号称王屋山主峰的天坛山极顶还高57米。灵泉洞
原名白连洞。位于县城南43公里的河北镇杨柏村南悬崖绝壁间。洞口由茂密林木遮蔽。欲人洞，需艰辛攀援，披荆押棘。灵泉洞为石灰岩洞，长500米。由10多个深广不一，景象各异的小洞相连。洞内的石笋和石钟乳玲珑剔透，洁白晶莹，造型似狮似猴，类虎类犬，姿态各异，栩栩如生。
        """)

#右边

link = get_rel_url("https://v.qq.com/x/page/g3116qm34rs.html")
if link:
    st.text("杨柏山大峡谷横拍视频，加载成功")
else:
     st.text("杨柏山大峡谷横拍视频，加载失败---")
components.iframe(link,height=512, width=750)
