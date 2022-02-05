from scraper import get_citations_needed_count, get_citations_needed_report
import pytest

URL = "https://en.wikipedia.org/wiki/History_of_China"

def test_get_citations_needed_count():
    assert get_citations_needed_count(URL) == 4

def test_get_citations_needed_report():
    expected = """1. Citation needed for "Archaeological evidence, such as oracle bones and bronzes, and transmitted texts attest to the historical existence of the Shang dynasty (c. 1600–1046 BC). Findings from the earlier Shang period comes from excavations at Erligang, near present day Zhengzhou, and Shangcheng. Findings from the later Shang or Yin (殷) period, were found in profusion at Anyang, in modern-day Henan, [29] the last of the Shang's nine capitals (c. 1300–1046 BC)."
2. Citation needed for "The king of Zhou at this time invoked the concept of the Mandate of Heaven to legitimize his rule, a concept that was influential for almost every succeeding dynasty."
3. Citation needed for "The Imperial China Period can be divided into three sub-periods: Early, Middle, and Late."
4. Citation needed for "Historians often refer to the period from the Qin dynasty to the end of the Qing dynasty as Imperial China."
"""
    assert get_citations_needed_report(URL) == expected