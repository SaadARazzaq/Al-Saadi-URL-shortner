import streamlit as st
import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    try:
        return s.tinyurl.short(url)
    except pyshorteners.exceptions.ShorteningErrorException as e:
        return str(e)

def is_valid_url(url):
    import re
    url_pattern_secured = re.compile(r'^https?://\S+$') 
    url_pattern_unsecured = re.compile(r'^http?://\S+$')
    return bool(url_pattern_secured.match(url) or url_pattern_unsecured.match(url))

def main():
    st.title("Al-Saadi URL Shortener")
    url = st.text_input("Enter URL:", "")
    if st.button("Shorten"):
        if is_valid_url(url):
            shortened_url = shorten_url(url)
            if shortened_url.startswith("Error"):
                st.error("Error: Unable to shorten the URL.")
            else:
                st.success("Shortened URL: " + shortened_url)
        else:
            st.warning("Please enter a valid URL.")
if __name__ == "__main__":
    main()
