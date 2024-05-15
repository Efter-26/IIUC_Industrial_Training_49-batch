
import os
PYPPETEER_CHROMIUM_REVISION = '1263111'

os.environ['PYPPETEER_CHROMIUM_REVISION'] = PYPPETEER_CHROMIUM_REVISION

from requests_html import HTMLSession

def render_javascript(url):
    
    session = HTMLSession()
    try:
        latest_chromium_url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win_x64%2FLAST_CHANGE%2Fchrome-win.zip?alt=media"
        
        response = session.get(url)
        response.html.render(retries=3, sleep=5, wait=10)  # This will download Chromium if not found
        print("Rendered web page:", response.html.html)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def extract_information(url):
    
    session = HTMLSession()
    try:
        response = session.get(url)
        
        title_tag = response.html.find('h1')
        print(len(title_tag), "title tags found:")
        print("Title: ", title_tag[0].text)

        #datetime_element = response.html.find('time', first=True)
        #datetime = datetime_element.attrs['datetime']
        #print("Datetime attribute: ", datetime)

        # advanced usages of extraction
        #temp = response.html.xpath('div.time-social-share-wrapper > div > time', first=True)
        #print(temp)
        #datetime = temp.attrs['datetime']
        #print(datetime)



        # Example: Extracting all links
        links = response.html.find('a')
        print(len(links), "links found:")
        for link in links:
            print("Link Text: ", link.text, "Link href: ", link.attrs['href'])        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def main():
    """
    Main function to execute the web scraping examples.
    """
    print("Rendering JavaScript on a web page...")
    render_javascript('https://example.com')

    print("\nExtracting information from a web page...")
    extract_information('https://example.com')
    #extract_information('https://www.prothomalo.com/world/usa/xnjy4uqwpv')

if __name__ == "__main__":
    main()
