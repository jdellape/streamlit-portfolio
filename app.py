import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(layout="wide")

st.title('John Dellape')

with st.sidebar:
    st.header('Find Me:')
    components.html(
        """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="dark" data-type="VERTICAL" data-vanity="john-dellape" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/john-dellape?trk=profile-badge"></a></div>
        """, height=310
        )
    st.markdown("[GitHub](https://github.com/jdellape)")
st.header('About Me')
st.markdown("I enjoy applying data focused programming while working with others to solve meaningful information coordination problems.\
            My interests and technical competencies cut across the traditional lines of 'data analytics', 'data engineering' and 'data science'.\
            For my current job, I spend a lot of time writing SQL queries against a Redshift datawarehouse and visualizing the results in Looker. \
            Most importantly, I spend a lot of time in communication with colleagues and clients about the questions and problems they face, discussing \
            how a data product can provide a solution for them, and working through cycles of developing a data product, showing it, receiving feedback, \
            and improving the product until we have solved the original problem. \
            I have come to love using streamlit as my primary outlet for developing and deploying data focused applications using python. \
            I genuinely enjoy my line of work and spend a lot of my time outside of my job working on side projects and learning about current developments \
            in the field. This streamlit app serves as a repository of my work and the resources I have learned from.")

st.header('Streamlit Projects')

streamlit_project_df = pd.read_csv('data/streamlit_project_inventory.csv')

streamlit_project_records = streamlit_project_df.to_dict('records')

streamlit_project_length = len(streamlit_project_records)

col_list_one = st.columns((1,1,1))

for col, record in zip(col_list_one, streamlit_project_records[:3]):
    with col:
        st.markdown(f"[{record['Name']}]({record['Link']})", unsafe_allow_html=True)
        with st.expander('Problem Scenario', expanded=False):
            st.write(record['Problem Scenario'])
        with st.expander('App Solution', expanded=False):
            st.write(record['Data App Solution'])

col_list_two = st.columns((1,1,1))

for col, record in zip(col_list_two, streamlit_project_records[3:]):
    with col:
        st.markdown(f"[{record['Name']}]({record['Link']})", unsafe_allow_html=True)
        with st.expander('Problem Scenario', expanded=False):
            st.write(record['Problem Scenario'])
        with st.expander('App Solution', expanded=False):
            st.write(record['Data App Solution'])

st.header('Other Projects')
op_li_one, op_li_two, op_li_three = st.columns((1,1,1))
with op_li_one:
    st.markdown('[Great Requirement Discourse](https://www.grdiscourse.com/)', unsafe_allow_html=True)
    st.write('Framework: Flask')
    with st.expander('Problem Scenario', expanded=False):
        st.write('Blank')
    with st.expander('App Solution', expanded=False):
        st.write('Blank')

with op_li_two:
    st.markdown('[CFB Recruiting Rankings Bump Chart](https://public.tableau.com/app/profile/john.dellape/viz/CollegeFootballRecruitingClassRankingsbyYear/Dashboard1)', unsafe_allow_html=True)
    st.write('Framework: Tableau')
    with st.expander('Problem Scenario', expanded=False):
        st.write('Blank')
    with st.expander('App Solution', expanded=False):
        st.write('Blank')

st.header('Technical Competencies')
tc_li_one, tc_li_two, tc_li_three, tc_li_four, tc_li_five = st.columns((1,1,1,1,1))

with tc_li_one:
    st.subheader('Languages')
    st.button('SQL', disabled=True)
    st.button('Python', disabled=True)
    st.button('Java', disabled=True)

with tc_li_two:
    st.subheader('Data Visualization')
    st.button('Looker', disabled=True)
    st.button('Tableau', disabled=True)
    st.button('Python Libs (i.e. Altair)', disabled=True)

with tc_li_three:
    st.subheader('Cloud Tools')
    st.button('Redshift', disabled=True)
    st.button('BigQuery', disabled=True)

with tc_li_four:
    st.subheader('NoSQL')
    st.button('MongoDB', disabled=True)
    st.button('Neo4j', disabled=True)

with tc_li_five:
    st.subheader('Web Dev')
    st.button('Streamlit', disabled=True)
    st.button('Flask', disabled=True)

st.header('Learning Resources')
lr_pod_col, lr_site_col, lr_other_col = st.columns((1,1,1))
with lr_pod_col:
    st.subheader('Podcasts')

    st.write('https://podcasts.apple.com/us/podcast/the-analytics-engineering-podcast/id1574755368')
    st.write('https://talkpython.fm/episodes/all')
    st.write('https://pythonbytes.fm/')
    st.write('https://www.dataengineeringpodcast.com/')
    st.write('https://twimlai.com/podcast/twimlai/')

with lr_site_col:
    st.subheader('Websites / Blogs')
    st.write('https://applyingml.com/')
    st.write('https://vickiboykis.com/')

with lr_other_col:
    st.subheader('Other')