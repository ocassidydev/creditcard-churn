import streamlit as st

class MultiPage:
    """
    Creates the multipage streamlit UI
    Taken from Walkthrough Project 02 - Churnometer

    Attributes:
        pages: a list that has dictionaries containing the page names and page body functions
                appended to it before running the app
        app_name: the name to display in the browser tab

    Methods:
        add_page: appends a page to pages, storing its name and display function
        run: displays the dashboard app
    """
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🍄")

        
    def add_page(self, title, func) -> None:
        """
        Adds page to the pages list
        Taken from Walkthrough Project 02 - Churnometer

        Args:
            title: the page title
            func: the page display function
        
        Returns:
            None
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Displays the streamlit app
        Taken from Walkthrough Project 02 - Churnometer

        Args:
            None
        
        Returns:
            None
        """
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()