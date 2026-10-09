import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#13131A; border-left: 8px solid #8B5CF6; padding:25px; border-radius: 20px; border: 1px solid #1F1F2E; margin-bottom:20px;">
        <h3 style="margin:0; color: #FFFFFF; font-size: 1.5rem ">{name}</h3>
        <p style="color:#9CA3AF; margin:10px 0;">Code : <span style="background:#8B5CF622; color:#8B5CF6; padding:2px 8px; border-radius:5px; border: 1px solid #8B5CF644;">{code} </span> | Section : {section}</p>

        """

    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #8B5CF618; color: #E0E7FF; padding:5px 12px; border-radius:12px; font-size:0.9rem; border: 1px solid #8B5CF633;">{icon} <b>{value}</b> {label} </div>'

        html+= "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
