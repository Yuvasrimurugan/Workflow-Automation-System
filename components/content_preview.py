import streamlit as st

def show_content_preview(state):
    st.header("Content Preview")
    
    # Debug panel (collapsible)
    with st.expander("🔍 Debug State"):
        st.json(state)
    
    tab1, tab2, tab3 = st.tabs(["Ideas", "Research", "Draft"])
    
    with tab1:
        st.subheader("Generated Ideas")
        if not state.get("ideas"):
            st.error("No ideas generated! Try:")
            st.write("1. Click 'Start Workflow'")
            st.write("2. Check terminal for errors")
        else:
            for i, idea in enumerate(state["ideas"], 1):
                st.success(f"{i}. {idea}")
    
    with tab2:
        st.subheader("Research Notes")
        content = state.get("research", "Research not generated yet")
        st.text_area("Research Summary", content, height=200, key="research_area")
    
    with tab3:
        st.subheader("Current Draft")
        content = state.get("draft", "Draft not generated yet") 
        st.text_area("Draft Content", content, height=300, key="draft_area")
    
    # Force refresh button
    if st.button("🔄 Refresh Preview", type="secondary"):
        st.rerun()