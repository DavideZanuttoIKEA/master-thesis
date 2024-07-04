import streamlit as st
import pandas as pd

# Load data from CSV files
reviews_df = pd.read_csv("artID+reviews.csv", delimiter=';') 
keyphrases_df = pd.read_csv("reviews+keyphrases.csv", delimiter=';')
images_df = pd.read_csv("articles_images.csv", delimiter=',')

# Merge reviews and keyphrases data
merged_df = reviews_df.merge(keyphrases_df, on='Reviews')

# Merge with images data
full_df = merged_df.merge(images_df, on='ArticleID')

# Display logo and title
cola, colb, colc = st.columns([1, 2, 1])
with colb:
    st.image('Ikea_logo.svg.png') 
st.title('Reviews and Keyphrases - Demo')

# Setup for displaying multiple images with pagination
image_data = full_df[['ArticleID', 'Image']].drop_duplicates().reset_index(drop=True)
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
        st.image(row['Image'], width=150, caption=f"Article ID: {row['ArticleID']}")
        if st.button("Select", key=row['ArticleID']):
            st.session_state.selected_article = row['ArticleID']
    index += 1

# Show selected article reviews and keyphrases
if 'selected_article' in st.session_state and st.session_state.selected_article:
    selected_article = st.session_state.selected_article
    article_reviews = full_df[full_df['ArticleID'] == selected_article]
    if not article_reviews.empty:
        st.write(f"Selected Article ID: {selected_article}")
        for _, row in article_reviews.iterrows():
            st.subheader("Review:")
            st.write(row['Reviews'])
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("##### Positive")
            with col2:
                st.markdown("##### Neutral")
            with col3:
                st.markdown("##### Negative")
            keyphrases = str(row['Keyphrases']).split(', ')
            for keyphrase in keyphrases:
                try:
                    phrase, sentiment = keyphrase.split(' - ')
                    if 'positive' in sentiment.lower():
                        with col1:
                            st.markdown(f"<span style='color: green;'><strong> ✔ &nbsp; </strong> {phrase}</span>", unsafe_allow_html=True)
                    elif 'negative' in sentiment.lower():
                        with col3:
                            st.markdown(f"<span style='color: red;'> ✘ &nbsp; {phrase}</span>", unsafe_allow_html=True)
                    elif 'neutral' in sentiment.lower():
                        with col2:
                            st.markdown(f"• &nbsp;{phrase}")
                except ValueError:
                    st.write("")
            st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    else:
        st.write("No reviews found for this article.")
else:
    st.write("Select an article to view reviews and keyphrases.")
