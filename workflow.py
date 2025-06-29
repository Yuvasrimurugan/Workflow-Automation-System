from langgraph.graph import StateGraph, END
from typing import Dict, TypedDict, Literal
import random

class WorkflowState(TypedDict):
    ideas: list[str]
    research: str
    draft: str
    review_count: int
    workflow_type: str

def ideation_node(state: WorkflowState) -> Dict[str, list[str]]:
    print("\n🔥 IDEATION NODE FIRED")  # Debug
    topics = {
        "Blog Post": ["Python", "AI", "Streamlit"],
        "Research Paper": ["LLMs", "Neural Networks"],
        "Social Media": ["Tips", "Trends"]
    }.get(state["workflow_type"], ["Tech"])
    
    ideas = [
        f"{random.randint(3, 10)} Ways to Use {random.choice(topics)}",
        f"{random.choice(topics)} in {random.randint(2024, 2030)}",
        f"{random.choice(topics)} vs {random.choice(topics)}"
    ]
    print(f"Generated ideas: {ideas}")  # Debug
    return {"ideas": ideas}

def research_node(state: WorkflowState) -> Dict[str, str]:
    return {
        "research": f"Research about: {state['ideas'][0]}\n\n" +
        f"- Key Finding 1\n- Key Finding 2\n- Sources"
    }

def writing_node(state: WorkflowState) -> Dict[str, str]:
    return {
        "draft": f"# {state['ideas'][0]}\n\n" +
        f"## Introduction\n## Key Points\n## Conclusion"
    }

def review_node(state: WorkflowState) -> Dict[str, int]:
    return {"review_count": state.get("review_count", 0) + 1}

def should_review(state: WorkflowState) -> Literal["review", "end"]:
    return "review" if state.get("review_count", 0) < 2 else "end"

def create_workflow():
    workflow = StateGraph(WorkflowState)
    
    workflow.add_node("ideation", ideation_node)
    workflow.add_node("research", research_node)
    workflow.add_node("writing", writing_node)
    workflow.add_node("review", review_node)
    
    workflow.set_entry_point("ideation")
    workflow.add_edge("ideation", "research")
    workflow.add_edge("research", "writing")
    workflow.add_edge("writing", "review")
    
    workflow.add_conditional_edges(
        "review",
        should_review,
        {"review": "writing", "end": END}
    )
    
    return workflow