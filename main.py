import streamlit as st
from components.sidebar import show_sidebar
from components.workflow_visualizer import show_workflow
from components.content_preview import show_content_preview
from workflow import create_workflow

def main():
    st.set_page_config(
        page_title="Content Workflow Automation",
        page_icon="📝",
        layout="wide"
    )
    
    # Initialize session state
    if 'workflow_state' not in st.session_state:
        st.session_state.workflow_state = {
            "ideas": [],
            "research": "",
            "draft": "",
            "review_count": 0,
            "workflow_type": "Blog Post"
        }
    
    # Get settings from sidebar
    settings = show_sidebar()
    st.session_state.workflow_state["workflow_type"] = settings["workflow_type"]
    
    # Execute workflow when started
    if settings['running']:
        st.session_state.workflow_state.update({
            "ideas": [],  # Reset on each run
            "research": "",
            "draft": "",
            "review_count": 0
        })
        workflow = create_workflow()
        app = workflow.compile()
        new_state = app.invoke(st.session_state.workflow_state)
        st.session_state.workflow_state.update(new_state)
        st.rerun()
    
    # Main UI layout
    col1, col2 = st.columns([2, 1])
    with col1:
        show_workflow(st.session_state.workflow_state)
    with col2:
        show_content_preview(st.session_state.workflow_state)

if __name__ == "__main__":
    main()