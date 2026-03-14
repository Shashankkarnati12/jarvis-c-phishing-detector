import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import joblib
import pandas as pd
import os
import sys
import winsound

from features import extract_features, check_ssl_certificate, check_domain_age


# =============================
# EXE SAFE PATH
# =============================

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


MODEL_PATH = resource_path(os.path.join("models", "phishing_model.pkl"))
model = joblib.load(MODEL_PATH)


# =============================
# ALERT SOUND
# =============================

def play_alert(is_phishing):
    try:
        if is_phishing:
            winsound.Beep(1200, 200)
            winsound.Beep(900, 200)
        else:
            winsound.Beep(600, 200)
    except:
        pass


# =============================
# THREAT LEVEL
# =============================

def get_threat_level(prob):
    if prob > 80:
        return "HIGH", "red"
    elif prob > 50:
        return "MEDIUM", "orange"
    else:
        return "LOW", "#00ff00"


# =============================
# SCAN FUNCTION
# =============================

def perform_scan():
    url = url_entry.get().strip()

    if url == "":
        messagebox.showwarning("Input Error", "Enter URL")
        return

    loading_label.config(text="Scanning...", fg="yellow")
    progress["value"] = 0

    try:
        for i in range(5):
            time.sleep(0.25)
            progress["value"] += 20
            root.update_idletasks()

        # ML
        features = extract_features(url)
        df_input = pd.DataFrame([features])
        proba = model.predict_proba(df_input)[0]

        phishing_prob = proba[1] * 100

       # SSL
        ssl_data = check_ssl_certificate(url)
        ssl_valid = ssl_data[0]
        days_left = ssl_data[1]

        if not ssl_valid:
              phishing_prob += 15
        else:
               phishing_prob -= 5

        # DOMAIN AGE
        domain_age = check_domain_age(url)
        if domain_age < 180:
            phishing_prob += 20

        phishing_prob = max(0, min(phishing_prob, 100))

        # UI UPDATE
        threat_text, threat_color = get_threat_level(phishing_prob)

        threat_label.config(text=f"Threat Level: {threat_text}", fg=threat_color)
        probability_label.config(text=f"Phishing Probability: {phishing_prob:.2f}%")

        ssl_label.config(
            text=f"SSL Status: {'Valid SSL' if ssl_valid else 'Invalid SSL'}"
        )

        age_label.config(text=f"Domain Age: {domain_age} days")

        if phishing_prob > 50:
            result_label.config(text="⚠ PHISHING WEBSITE DETECTED", fg="red")
            play_alert(True)
        else:
            result_label.config(text="✔ WEBSITE VERIFIED AS SAFE", fg="#00ff00")
            play_alert(False)

    except Exception as e:
        messagebox.showerror("Error", str(e))

    loading_label.config(text="")
    progress["value"] = 0


def start_thread():
    threading.Thread(target=perform_scan, daemon=True).start()


# =============================
# GUI SETUP
# =============================

root = tk.Tk()
root.title("Cybersecurity Phishing Detection System")
root.geometry("780x580")
root.configure(bg="black")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="CYBERSECURITY PHISHING DETECTION SYSTEM",
    font=("Consolas", 20, "bold"),
    bg="black",
    fg="#00ff00"
)
title_label.pack(pady=25)

url_entry = tk.Entry(
    root,
    width=75,
    font=("Consolas", 12),
    bg="black",
    fg="#00ff00",
    insertbackground="#00ff00"
)
url_entry.pack(pady=10, ipady=6)

scan_button = tk.Button(
    root,
    text="START SCAN",
    font=("Consolas", 12, "bold"),
    bg="#002200",
    fg="#00ff00",
    command=start_thread
)
scan_button.pack(pady=10)

progress = ttk.Progressbar(root, length=500)
progress.pack(pady=15)

loading_label = tk.Label(root, text="", bg="black", fg="yellow")
loading_label.pack()

result_label = tk.Label(root, text="", font=("Consolas", 18, "bold"), bg="black")
result_label.pack(pady=20)

threat_label = tk.Label(root, text="Threat Level: -", bg="black", fg="#00ff00")
threat_label.pack()

probability_label = tk.Label(root, text="", bg="black", fg="#00ff00")
probability_label.pack()

ssl_label = tk.Label(root, text="SSL Status: -", bg="black", fg="#00ff00")
ssl_label.pack()

age_label = tk.Label(root, text="Domain Age: -", bg="black", fg="#00ff00")
age_label.pack()

root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import joblib
import pandas as pd
import os
import sys
import winsound

from features import extract_features, check_ssl_certificate, check_domain_age


# =============================
# EXE SAFE PATH
# =============================

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


MODEL_PATH = resource_path(os.path.join("models", "phishing_model.pkl"))
model = joblib.load(MODEL_PATH)


# =============================
# ALERT SOUND
# =============================

def play_alert(is_phishing):
    try:
        if is_phishing:
            winsound.Beep(1200, 200)
            winsound.Beep(900, 200)
        else:
            winsound.Beep(600, 200)
    except:
        pass


# =============================
# THREAT LEVEL
# =============================

def get_threat_level(prob):
    if prob > 80:
        return "HIGH", "red"
    elif prob > 50:
        return "MEDIUM", "orange"
    else:
        return "LOW", "#00ff00"


# =============================
# SCAN FUNCTION
# =============================

def perform_scan():
    url = url_entry.get().strip()

    if url == "":
        messagebox.showwarning("Input Error", "Enter URL")
        return

    loading_label.config(text="Scanning...", fg="yellow")
    progress["value"] = 0

    try:
        for i in range(5):
            time.sleep(0.25)
            progress["value"] += 20
            root.update_idletasks()

        # ML
        features = extract_features(url)
        df_input = pd.DataFrame([features])
        proba = model.predict_proba(df_input)[0]

        phishing_prob = proba[1] * 100

       # SSL
        ssl_data = check_ssl_certificate(url)
        ssl_valid = ssl_data[0]
        days_left = ssl_data[1]

        if not ssl_valid:
              phishing_prob += 15
        else:
               phishing_prob -= 5

        # DOMAIN AGE
        domain_age = check_domain_age(url)
        if domain_age < 180:
            phishing_prob += 20

        phishing_prob = max(0, min(phishing_prob, 100))

        # UI UPDATE
        threat_text, threat_color = get_threat_level(phishing_prob)

        threat_label.config(text=f"Threat Level: {threat_text}", fg=threat_color)
        probability_label.config(text=f"Phishing Probability: {phishing_prob:.2f}%")

        ssl_label.config(
            text=f"SSL Status: {'Valid SSL' if ssl_valid else 'Invalid SSL'}"
        )

        age_label.config(text=f"Domain Age: {domain_age} days")

        if phishing_prob > 50:
            result_label.config(text="⚠ PHISHING WEBSITE DETECTED", fg="red")
            play_alert(True)
        else:
            result_label.config(text="✔ WEBSITE VERIFIED AS SAFE", fg="#00ff00")
            play_alert(False)

    except Exception as e:
        messagebox.showerror("Error", str(e))

    loading_label.config(text="")
    progress["value"] = 0


def start_thread():
    threading.Thread(target=perform_scan, daemon=True).start()


# =============================
# GUI SETUP
# =============================

root = tk.Tk()
root.title("Cybersecurity Phishing Detection System")
root.geometry("780x580")
root.configure(bg="black")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="CYBERSECURITY PHISHING DETECTION SYSTEM",
    font=("Consolas", 20, "bold"),
    bg="black",
    fg="#00ff00"
)
title_label.pack(pady=25)

url_entry = tk.Entry(
    root,
    width=75,
    font=("Consolas", 12),
    bg="black",
    fg="#00ff00",
    insertbackground="#00ff00"
)
url_entry.pack(pady=10, ipady=6)

scan_button = tk.Button(
    root,
    text="START SCAN",
    font=("Consolas", 12, "bold"),
    bg="#002200",
    fg="#00ff00",
    command=start_thread
)
scan_button.pack(pady=10)

progress = ttk.Progressbar(root, length=500)
progress.pack(pady=15)

loading_label = tk.Label(root, text="", bg="black", fg="yellow")
loading_label.pack()

result_label = tk.Label(root, text="", font=("Consolas", 18, "bold"), bg="black")
result_label.pack(pady=20)

threat_label = tk.Label(root, text="Threat Level: -", bg="black", fg="#00ff00")
threat_label.pack()

probability_label = tk.Label(root, text="", bg="black", fg="#00ff00")
probability_label.pack()

ssl_label = tk.Label(root, text="SSL Status: -", bg="black", fg="#00ff00")
ssl_label.pack()

age_label = tk.Label(root, text="Domain Age: -", bg="black", fg="#00ff00")
age_label.pack()

root.mainloop()