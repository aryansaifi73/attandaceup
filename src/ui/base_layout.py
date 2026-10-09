import streamlit as st



def style_background_home():

    st.markdown("""
        <style>
                .stApp {
                    background-color: #030712 !important;
                    background-image: radial-gradient(circle, rgba(255, 255, 255, 0.05) 1px, transparent 1px) !important;
                    background-size: 20px 20px !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #0f172a !important;
                    padding: 2.5rem !important;
                    border-radius: 2rem !important;
                    border: 1px solid #1e293b !important;
                }
        </style>

                """
            ,unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background-color: #030712 !important;
                    background-image: radial-gradient(circle, rgba(255, 255, 255, 0.05) 1px, transparent 1px) !important;
                    background-size: 20px 20px !important;
                }

        </style>

                """
            ,unsafe_allow_html=True)




def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


         /* Hide Top Bar of streamlit */

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top:1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: #FFFFFF !important;
            }


            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color: #FFFFFF !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif;
                color: #FFFFFF;
            }


            button{
                border-radius: 1.5rem !important;
                background-color: #8B5CF6 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #1F1F2E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: 1px solid #2D2D3F !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: transparent !important;
                color: #8B5CF6 !important;
                border: 1px solid #8B5CF6 !important;
                padding: 10px 20px !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05) !important;}
        </style>

                """
            ,unsafe_allow_html=True)
