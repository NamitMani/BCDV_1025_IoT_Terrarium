import streamlit as st
import requests
import json
import pandas as pd

BASE_URL = "http://4.204.190.172:3000"


def submit_transaction(identity, function, device_id, owner):
    url = BASE_URL + "/submitTx"
    payload = {
        "identity": identity,
        "function": function,
        "deviceID": device_id,
        "owner": owner
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()


def query_all_devices(identity):
    url = BASE_URL + "/queryAllDevices"
    payload = {
        "identity": identity,
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()


def main():
    st.title("Terrarium - App")

    menu = ["Query All Devices", "Submit Transaction"]
    choice = st.sidebar.selectbox("Choose Action", menu)

    if choice == "Query All Devices":
        st.subheader("Query All Devices")
        identity = st.text_input("Identity", "User1@org1.example.com")

        if st.button("Query All Devices"):
            response = query_all_devices(identity)

            try:
                response_json = json.loads(response)
                df = pd.json_normalize(response_json)
                st.dataframe(df)
            except json.JSONDecodeError:
                st.write("Error: The response is not in the expected format.")

    elif choice == "Submit Transaction":
        st.subheader("Submit a Transaction")
        identity = st.text_input("Identity", "User1@org1.example.com")
        function = st.text_input("Function", "createDevice")
        device_id = st.text_input("Device ID", "device123")
        owner = st.text_input("Owner", "John")

        if st.button("Submit Transaction"):
            response = submit_transaction(identity, function, device_id, owner)
            st.write(response)


if __name__ == "__main__":
    main()
