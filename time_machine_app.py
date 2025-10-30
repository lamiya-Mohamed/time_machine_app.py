import streamlit as st

st.title("⏳ آلة الزمن - Time Machine")
st.subheader("جربي تدخلين كود الزمن الصحيح لتشغيل الآلة 🔮")

# إعداد الحالة (Session State)
if "energy" not in st.session_state:
    st.session_state.energy = 3
if "done" not in st.session_state:
    st.session_state.done = False
if "message" not in st.session_state:
    st.session_state.message = ""

time_code = 3025

# لو الآلة لسه شغالة
if not st.session_state.done and st.session_state.energy > 0:
    code = st.number_input("💡 ادخلي كود الزمن:", min_value=0, max_value=9999, step=1)

    if st.button("تشغيل الآلة 🚀"):
        if code == time_code:
            st.session_state.done = True
            st.success("✅ الآلة اشتغلت! تم السفر إلى المستقبل!")
            st.balloons()
        else:
            st.session_state.energy -= 1
            st.session_state.message = f"⚠️ الكود خاطئ، تم الرجوع 10 سنوات للخلف!\n🔋 الطاقة المتبقية: {st.session_state.energy}"

# عرض الرسائل
if st.session_state.message:
    st.warning(st.session_state.message)

# لو الطاقة خلصت
if st.session_state.energy == 0 and not st.session_state.done:
    st.error("💥 انتهت الطاقة! الآلة تعطلت نهائيًا")

# زر لإعادة التشغيل
if st.session_state.done or st.session_state.energy == 0:
    if st.button("🔁 إعادة المحاولة"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
