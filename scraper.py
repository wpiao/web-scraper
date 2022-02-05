from bs4 import BeautifulSoup
import requests
import re

def get_citations_needed_count(url):
    r_content = requests.get(url).content
    soup = BeautifulSoup(r_content, "html.parser")
    citation_needed = soup.find_all("span", title=re.compile("This claim needs references to reliable sources."))
    return len(citation_needed)
    
def get_citations_needed_report(url):
    r_content = requests.get(url).content
    soup = BeautifulSoup(r_content, "html.parser")
    citation_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    count = 1
    results = ""
    for citation in citation_needed:
        paragraph = citation.parent.parent.parent.text.split("[citation needed]")[0]
        results += f"{count}. Citation needed for \"{paragraph}\"\n"
        count += 1
    return results
