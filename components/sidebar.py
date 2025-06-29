import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.title("⚙️ Workflow Controls")
        
        workflow_type = st.selectbox(
            "Workflow Type",
            ["Blog Post", "Research Paper", "Social Media"],
            key="workflow_type"
        )
        
        st.subheader("Settings")
        review_cycles = st.slider(
            "Review Cycles", 
            1, 5, 2,
            help="Number of review iterations"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            start_btn = st.button("▶️ Start", type="primary")
        with col2:
            stop_btn = st.button("⏹️ Stop")
        
        st.subheader("Status")
        status = st.empty()
        
        if start_btn:
            st.session_state.running = True
            status.success("Workflow running!")
        elif stop_btn:
            st.session_state.running = False
            status.warning("Workflow stopped")
            
    return {
        "workflow_type": workflow_type,
        "review_cycles": review_cycles,
        "running": st.session_state.get("running", False)
    }