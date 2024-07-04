import streamlit as st
import pandas as pd

# Load data from CSV files
topics_df = pd.read_csv("artID+topics.csv", delimiter=';')
reviews_df = pd.read_csv("final_topic_reviews_word080.csv", delimiter=',')
images_df = pd.read_csv("articles_images.csv", delimiter=',')

# Filter images_df to only include ArticleIDs present in topics_df
valid_article_ids = topics_df['ArticleID'].unique()
filtered_images_df = images_df[images_df['ArticleID'].isin(valid_article_ids)]

# Display logo and title
cola, colb, colc = st.columns([1, 2, 1])
with colb:
    st.image('Ikea_logo.svg.png')
st.title('Reviews and Topics - Demo')

# Setup for displaying multiple images with pagination
image_data = filtered_images_df[['ArticleID', 'Image']].drop_duplicates().reset_index(drop=True)
images_per_page = 6  # Number of images per page
total_pages = len(image_data) // images_per_page + (1 if len(image_data) % images_per_page > 0 else 0)

# Initialize or get the current page from the session state
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 0
current_page = st.session_state['current_page']

# Navigation buttons with aligned columns
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    if st.button('Previous'):
        if current_page > 0:
            st.session_state['current_page'] -= 1
            st.rerun()
with col3:
    if st.button('Next'):
        if current_page < total_pages - 1:
            st.session_state['current_page'] += 1
            st.rerun()

# Calculate start and end indices of the images to display
start_idx = current_page * images_per_page
end_idx = start_idx + images_per_page

# Display images for the current page
cols = st.columns(3)
index = 0
for i in range(start_idx, min(end_idx, len(image_data))):
    row = image_data.iloc[i]
    with cols[index % 3]:
        if st.button(f"Select", key=row['ArticleID']):
           
            if 'selected_article' in st.session_state:
                if st.session_state['selected_article'] != row['ArticleID']:
                    st.session_state['selected_topic'] = None  # Reset the selected topic
            st.session_state['selected_article'] = row['ArticleID']
            st.rerun()
        st.image(row['Image'], width=150, caption=f"Article ID: {row['ArticleID']}")
    index += 1

# Add a double line separator
st.markdown("""<hr style="height:9px;border-top:2px solid black;border-bottom:2px solid black;" />""", unsafe_allow_html=True)

# Show selected article topics and allow selection of a topic to view reviews
if 'selected_article' in st.session_state and st.session_state.selected_article:
    selected_article = st.session_state.selected_article
    filtered_df = topics_df[topics_df['ArticleID'] == selected_article]
    if not filtered_df.empty:
        topics_string = filtered_df['Topics'].iloc[0]
        topics_list = topics_string.split(', ')

        if 'selected_topic' not in st.session_state:
            st.session_state['selected_topic'] = None

        cols = st.columns(4)
        for i, topic in enumerate(topics_list):
            with cols[i % 4]:
                if st.button(topic, key=f"topic_{i}"):
                    st.session_state['selected_topic'] = topic

        # Display reviews for the selected topic
        if st.session_state.selected_topic:
            reviews = reviews_df[(reviews_df['ArticleID'] == selected_article) & (reviews_df['Topic'] == st.session_state.selected_topic)]
            if not reviews.empty and isinstance(reviews.iloc[0]['Reviews'], str):
                st.subheader(f"Reviews for '{st.session_state.selected_topic}':")
                review_text = reviews.iloc[0]['Reviews']
                # Check if there are multiple reviews separated by "|"
                if '|' in review_text:
                    review_list = review_text.split('| ')
                else:
                    review_list = [review_text]  # Treat the entire string as one review if no delimiter
                for review in review_list:
                    st.write(review)
            else:
                st.write("No reviews found for this topic.")
    else:
        st.write("No topics found for this article.")
else:
    st.write("Select an article to view topics and reviews.")
