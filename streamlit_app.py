import streamlit as st


st.logo("avatar.png")
st.title("STARLING AI")
st.write(
    "Welcome to my personal website, where I showcase a portfolio of experiments exploring the cutting-edge potential of artificial intelligence. Here, you’ll find projects that push the boundaries of AI technologies, spanning various applications and industries. Each experiment reflects a hands-on approach to innovation, combining creativity with advanced technical insight. Dive in to discover how AI can transform ideas into powerful solutions."
)
st.sidebar.image("avatar.png", width=150)
st.sidebar.title("S.T.A.R.L.I.N.G. AI")


from st_paywall import add_auth

"Hello in paywall page"

add_auth(required=True)

#after authentication, the email and subscription status is stored in session state
st.write(st.session_state.email)
st.write(st.session_state.user_subscribed)

st.text("hello")

text1, exampl1 = st.columns(2)
text1.markdown( """
# YouTube Shorts generator
A YouTube Shorts generator uses neural networks to create short-form video content based on a given title. The AI generates a script, visuals, and converts text to speech. Additionally, it produces the video’s title, description, and relevant keywords for better discoverability. This automated process streamlines video creation, making it easier for users to produce engaging content efficiently.
""" )
exampl1.video(".temp/test.mp4", start_time=3)