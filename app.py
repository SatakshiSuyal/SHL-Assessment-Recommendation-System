import streamlit as st
from recommender_api import SHLRecommender
import time

def main():
    st.set_page_config(
        page_title="SHL- Assessment Recommender System",
        page_icon="📊",
        layout="wide"
    )
    
    # Initialize recommender
    try:
        recommender = SHLRecommender()
    except Exception as e:
        st.error(f"Failed to initialize recommender: {str(e)}")
        st.stop()
    
    # Sidebar filters
    st.sidebar.title("Filters")
    category = st.sidebar.selectbox(
        "Assessment Category",
        options=["All"] + recommender.get_categories()
    )
    duration_filter = st.sidebar.slider(
        "Maximum Duration (minutes)", 
        min_value=15, 
        max_value=120, 
        value=60,
        step=5
    )
    
    # Main interface
    st.title("SHL Assessment Recommendation System")
    st.write("Find the perfect SHL assessment for your hiring needs")
    
    # Search query
    query = st.text_area(
        "Describe your needs:",
        placeholder="e.g., We need a cognitive test for software engineers under 45 minutes",
        height=150
    )
    
    if st.button("Get Recommendations"):
        if not query.strip():
            st.warning("Please enter a description of your needs")
        else:
            with st.spinner("Finding the best assessments..."):
                try:
                    start_time = time.time()
                    recommendations = recommender.recommend(
                        query,
                        category=None if category == "All" else category,
                        duration_max=duration_filter
                    )
                    elapsed = time.time() - start_time
                    
                    if not recommendations:
                        st.warning("No matching assessments found. Try broadening your filters.")
                    else:
                        st.success(f"Found {len(recommendations)} recommendations in {elapsed:.2f} seconds")
                        
                        for i, rec in enumerate(recommendations, 1):
                            with st.expander(f"{i}. {rec['name']} (Score: {rec['score']:.2f})"):
                                cols = st.columns([1, 3])
                                with cols[0]:
                                    st.markdown(f"**Test Link**: {rec['url']}")
                                    st.markdown(f"**Category**: {rec['category']}")
                                    st.markdown(f"**Duration**: {rec['duration']}")
                                    st.markdown(f"**Remote**: {'Yes' if rec['remote'] else 'No'}")
                                    st.markdown(f"**Adaptive**: {'Yes' if rec['adaptive'] else 'No'}")
                                
                                with cols[1]:
                                    st.markdown(f"**Description**: {rec['description']}")
                                    if rec.get('skills_tested'):
                                        st.markdown(f"**Skills Tested**: {', '.join(rec['skills_tested'])}")
                                    if rec.get('use_cases'):
                                        st.markdown(f"**Best For**: {', '.join(rec['use_cases'])}")
                                    
                                    st.markdown(f"[View Details]({rec['url']})")
                
                except Exception as e:
                    st.error(f"Error generating recommendations: {str(e)}")

if __name__ == "__main__":
    main()