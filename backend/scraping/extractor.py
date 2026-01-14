import re
from typing import List, Dict


EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
PHONE_REGEX = r"\+?\d[\d\s().-]{7,}"
SOCIAL_REGEX = {
    "linkedin": r"https?://(www\.)?linkedin\.com/[^\s\"']+",
    "twitter": r"https?://(www\.)?(twitter|x)\.com/[^\s\"']+",
    "facebook": r"https?://(www\.)?facebook\.com/[^\s\"']+",
    "instagram": r"https?://(www\.)?instagram\.com/[^\s\"']+"
}


def extract_all(pages: List[Dict]) -> Dict:
    """
    Extract emails, phone numbers, and social links
    from scraped page content.
    """

    emails = set()
    phones = set()
    socials = set()

    for page in pages:
        content = page.get("content", "")

        # Emails
        emails.update(re.findall(EMAIL_REGEX, content))

        # Phones
        phones.update(re.findall(PHONE_REGEX, content))

        # Social links
        for regex in SOCIAL_REGEX.values():
            socials.update(re.findall(regex, content))

    return {
        "emails": list(emails),
        "phones": list(phones),
        "socials": list(socials)
    }
