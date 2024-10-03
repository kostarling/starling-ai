import streamlit as st

from st_paywall import add_auth

"Hello in paywall page"

add_auth(required=True)

#after authentication, the email and subscription status is stored in session state
st.write(st.session_state.email)
st.write(st.session_state.user_subscribed)

st.text("hello")