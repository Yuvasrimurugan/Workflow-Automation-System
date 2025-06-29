import streamlit as st
import graphviz

def show_workflow(state):
    st.header(f"{state.get('workflow_type', '')} Workflow")
    
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR')
    graph.attr('node', shape='box', style='rounded')
    
    # Add nodes
    nodes = ["ideation", "research", "writing", "review"]
    for node in nodes:
        graph.node(node, node.capitalize())
    
    # Add edges
    graph.edge("ideation", "research")
    graph.edge("research", "writing")
    graph.edge("writing", "review")
    
    # Conditional edge
    if state.get("review_count", 0) > 0:
        graph.edge("review", "writing", label=f"Cycle {state['review_count']}")
    
    st.graphviz_chart(graph)
    
    # Status indicators
    cols = st.columns(4)
    status = [
        "✓" if state.get("ideas") else "◯",
        "✓" if state.get("research") else "◯",
        "✓" if state.get("draft") else "◯",
        str(state.get("review_count", 0)) + "✓" if state.get("review_count", 0) > 0 else "◯"
    ]
    
    for col, node, stat in zip(cols, nodes, status):
        col.metric(node.capitalize(), stat)