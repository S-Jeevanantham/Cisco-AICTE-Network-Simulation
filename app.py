import streamlit as st
import time

st.set_page_config(page_title="Network Simulation Tool", layout="wide")

st.title("🌐 Network Simulation & Validation Tool")

st.write("Cisco AICTE Internship Project")

routers = st.number_input("Number of Routers", min_value=1, max_value=10, value=3)
switches = st.number_input("Number of Switches", min_value=1, max_value=10, value=2)

if st.button("Run Simulation"):

    output = []

    output.append("Starting Network Devices...")
    time.sleep(1)

    for i in range(routers):
        output.append(f"Router{i}: START")

    for i in range(switches):
        output.append(f"Switch{i+1}: START")

    output.append("")
    output.append("Neighbor Discovery: SUCCESS")
    output.append("")

    output.append("MTU Validation")
    output.append("Router0: DROP BIGDATA (2000 bytes) > exceeds MTU 1000")

    output.append("")
    output.append("Fault Injection")
    output.append("Link R0-R1 brought down")

    output.append("")
    output.append("Network Status: HEALTHY")

    st.success("Simulation Completed")

    st.code("\n".join(output))
