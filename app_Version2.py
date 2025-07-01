import streamlit as st
import datetime

st.set_page_config(page_title="Alarm App", page_icon="⏰")

st.title("⏰ Streamlit Alarm App")
st.write("Setel waktu alarm. Aplikasi harus terbuka agar alarm bisa berbunyi.")

col1, col2 = st.columns(2)

with col1:
    alarm_time = st.time_input("Waktu Alarm", value=(datetime.datetime.now() + datetime.timedelta(minutes=1)).time())
with col2:
    set_alarm = st.button("Set Alarm")

if "alarm_set" not in st.session_state:
    st.session_state["alarm_set"] = False
if "alarm_time" not in st.session_state:
    st.session_state["alarm_time"] = None
if "ring" not in st.session_state:
    st.session_state["ring"] = False

if set_alarm:
    st.session_state["alarm_set"] = True
    st.session_state["alarm_time"] = alarm_time
    st.session_state["ring"] = False
    st.success(f"Alarm disetel ke {alarm_time.strftime('%H:%M:%S')}")

if st.session_state["alarm_set"]:
    now = datetime.datetime.now().time()
    st.info(f"Waktu sekarang: {now.strftime('%H:%M:%S')}")
    st.info(f"Alarm disetel pada: {st.session_state['alarm_time'].strftime('%H:%M:%S')}")
    # Cek jika jam dan menit sama, detik = 0 (alarm hanya bunyi sekali di waktu tersebut)
    if (now.hour == st.session_state["alarm_time"].hour and
        now.minute == st.session_state["alarm_time"].minute and
        now.second == 0 and not st.session_state["ring"]):
        st.session_state["ring"] = True
        st.warning("⏰ Waktunya Alarm! ⏰")
        st.audio("https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg")
    elif st.session_state["ring"]:
        st.warning("⏰ Waktunya Alarm! ⏰")
        st.audio("https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg")
    else:
        st.write("Alarm belum berbunyi.")

st.caption("Aplikasi alarm ini berjalan di Streamlit. Silakan biarkan halaman ini tetap terbuka untuk memastikan alarm berbunyi.")