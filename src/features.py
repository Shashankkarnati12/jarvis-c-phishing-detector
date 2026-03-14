# ============================================
# FEATURES.PY - COMPLETE HYBRID FEATURE FILE
# ============================================

import re
import ssl
import socket
import whois
import requests
import base64
from datetime import datetime
from urllib.parse import urlparse


# =====================================================
# 1️⃣ URL FEATURE EXTRACTION (FOR ML MODEL)
# =====================================================

def extract_features(url):

    features = {}

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Basic length features
    features["url_length"] = len(url)
    features["hostname_length"] = len(domain)

    # Special characters
    features["dot_count"] = url.count(".")
    features["dash_count"] = url.count("-")
    features["at_count"] = url.count("@")
    features["question_count"] = url.count("?")
    features["percent_count"] = url.count("%")
    features["equal_count"] = url.count("=")
    features["slash_count"] = url.count("/")
    features["ampersand_count"] = url.count("&")

    # HTTPS
    features["has_https"] = 1 if parsed_url.scheme == "https" else 0

    # IP address in URL
    features["has_ip"] = 1 if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain) else 0

    # Subdomain count
    features["subdomain_count"] = domain.count(".")

    # Suspicious words
    suspicious_words = ["login", "verify", "update", "bank", "secure", "account"]
    features["has_suspicious_word"] = 1 if any(word in url.lower() for word in suspicious_words) else 0

    # Additional engineered features
    features["digit_count"] = sum(c.isdigit() for c in url)
    features["letter_count"] = sum(c.isalpha() for c in url)

    features["shortening_service"] = 1 if any(x in url for x in ["bit.ly", "tinyurl", "goo.gl"]) else 0

    features["double_slash_redirect"] = 1 if url.count("//") > 1 else 0

    features["prefix_suffix"] = 1 if "-" in domain else 0

    features["port_in_url"] = 1 if ":" in domain else 0

    features["https_token"] = 1 if "https" in domain else 0

    # Padding to ensure 24 features
    while len(features) < 24:
        features[f"extra_feature_{len(features)}"] = 0

    return features


# =====================================================
# 2️⃣ DOMAIN AGE CHECK (WHOIS)
# =====================================================

def check_domain_age(url):
    try:
        domain = urlparse(url).netloc
        domain_info = whois.whois(domain)

        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date is None:
            return 0

        # Fix timezone issue
        if hasattr(creation_date, "tzinfo") and creation_date.tzinfo is not None:
            creation_date = creation_date.replace(tzinfo=None)

        age_days = (datetime.now() - creation_date).days

        if age_days < 0:
            return 0

        return age_days

    except:
        return 0


# =====================================================
# 3️⃣ SSL CERTIFICATE CHECK
# =====================================================

def check_ssl_certificate(url):
    try:
        hostname = urlparse(url).netloc
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname):
                return "Valid SSL"

    except:
        return "Invalid SSL"


# =====================================================
# 4️⃣ VIRUSTOTAL API CHECK
# =====================================================

# 🔑 Replace with your real VirusTotal API key
VIRUSTOTAL_API_KEY = "cfab997ac08b915197c408d4d8b9a7f105754bbdfdb532afb2e8d92893f54a2a"


def check_virustotal(url):
    try:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

        headers = {
            "x-apikey": VIRUSTOTAL_API_KEY
        }

        vt_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        response = requests.get(vt_url, headers=headers)

        if response.status_code != 200:
            return {"malicious": 0, "suspicious": 0}

        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]

        return {
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0)
        }

    except:
        return {"malicious": 0, "suspicious": 0}
# ============================================
# FEATURES.PY - COMPLETE HYBRID FEATURE FILE
# ============================================

import re
import ssl
import socket
import whois
import requests
import base64
from datetime import datetime
from urllib.parse import urlparse


# =====================================================
# 1️⃣ URL FEATURE EXTRACTION (FOR ML MODEL)
# =====================================================

def extract_features(url):

    features = {}

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Basic length features
    features["url_length"] = len(url)
    features["hostname_length"] = len(domain)

    # Special characters
    features["dot_count"] = url.count(".")
    features["dash_count"] = url.count("-")
    features["at_count"] = url.count("@")
    features["question_count"] = url.count("?")
    features["percent_count"] = url.count("%")
    features["equal_count"] = url.count("=")
    features["slash_count"] = url.count("/")
    features["ampersand_count"] = url.count("&")

    # HTTPS
    features["has_https"] = 1 if parsed_url.scheme == "https" else 0

    # IP address in URL
    features["has_ip"] = 1 if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain) else 0

    # Subdomain count
    features["subdomain_count"] = domain.count(".")

    # Suspicious words
    suspicious_words = ["login", "verify", "update", "bank", "secure", "account"]
    features["has_suspicious_word"] = 1 if any(word in url.lower() for word in suspicious_words) else 0

    # Additional engineered features
    features["digit_count"] = sum(c.isdigit() for c in url)
    features["letter_count"] = sum(c.isalpha() for c in url)

    features["shortening_service"] = 1 if any(x in url for x in ["bit.ly", "tinyurl", "goo.gl"]) else 0

    features["double_slash_redirect"] = 1 if url.count("//") > 1 else 0

    features["prefix_suffix"] = 1 if "-" in domain else 0

    features["port_in_url"] = 1 if ":" in domain else 0

    features["https_token"] = 1 if "https" in domain else 0

    # Padding to ensure 24 features
    while len(features) < 24:
        features[f"extra_feature_{len(features)}"] = 0

    return features


# =====================================================
# 2️⃣ DOMAIN AGE CHECK (WHOIS)
# =====================================================

def check_domain_age(url):
    try:
        domain = urlparse(url).netloc
        domain_info = whois.whois(domain)

        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date is None:
            return 0

        # Fix timezone issue
        if hasattr(creation_date, "tzinfo") and creation_date.tzinfo is not None:
            creation_date = creation_date.replace(tzinfo=None)

        age_days = (datetime.now() - creation_date).days

        if age_days < 0:
            return 0

        return age_days

    except:
        return 0


# =====================================================
# 3️⃣ SSL CERTIFICATE CHECK
# =====================================================

def check_ssl_certificate(url):
    try:
        hostname = urlparse(url).netloc
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname):
                return "Valid SSL"

    except:
        return "Invalid SSL"


# =====================================================
# 4️⃣ VIRUSTOTAL API CHECK
# =====================================================

# 🔑 Replace with your real VirusTotal API key
VIRUSTOTAL_API_KEY = "cfab997ac08b915197c408d4d8b9a7f105754bbdfdb532afb2e8d92893f54a2a"


def check_virustotal(url):
    try:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

        headers = {
            "x-apikey": VIRUSTOTAL_API_KEY
        }

        vt_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        response = requests.get(vt_url, headers=headers)

        if response.status_code != 200:
            return {"malicious": 0, "suspicious": 0}

        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]

        return {
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0)
        }

    except:
        return {"malicious": 0, "suspicious": 0}