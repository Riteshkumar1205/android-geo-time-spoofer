# 🔐 Android Geo-Time Spoofer – Manual Location & Time Override Tool (Mobile Browsers)

**⚠️ Legal Disclaimer**
This software is intended strictly for ethical, educational, and authorized cybersecurity research purposes.

Unauthorized usage, including misrepresenting location or time to bypass policies, submit forms deceptively, or commit fraud, is illegal and unethical.

The user assumes full responsibility for any legal or ethical consequences resulting from the use of this software.

# 🧩 Project Overview

Android Geo-Time Spoofer is a Flask-based web tool that allows users to:

Manually set latitude, longitude, and altitude.

Override system time and timezone in mobile browsers (Chrome Android / Safari iOS).

Test forms, apps, or websites in controlled environments with spoofed location and time.

It is designed for educational and research purposes, demonstrating how geolocation and time detection work on mobile browsers.

# ✅ Key Features
**Feature	Description**
Geolocation Spoofing	Override latitude, longitude, and altitude for mobile browsers.
Time & Timezone Spoofing	Change local time to a desired value while keeping timezone consistency.
Mobile Browser Compatibility	Works on Chrome Android and Safari iOS without extensions.
Form Testing	Open Google Forms or other target pages with spoofed location/time.
Educational & Ethical	Intended for learning, testing, and research in authorized contexts.
# 🐧 Installation (Android – Termux / Linux)
Step 1: Install required tools
# Termux (Android)
~~~
pkg update && pkg upgrade -y
pkg install git python -y
~~~
# Linux (Ubuntu / Debian / Kali)
 ~~~
 sudo apt update && sudo apt install git python3 python3-pip python3-venv -y
~~~
Step 2: Clone the repository
~~~
git clone https://github.com/Riteshkumar1205/android-geo-time-spoofer.git
cd android-geo-time-spoofer/web
~~~
Step 3: Create a Python virtual environment
~~~
python3 -m venv venv
source venv/bin/activate
~~~
Step 4: Install dependencies
~~~
pip install -r ../requirements.txt
~~~
# 🚀 Running the Spoofer

Start the Flask server:
~~~
python app.py

~~~
Runs on 0.0.0.0:5000 by default.

On Termux (same device), use http://127.0.0.1:5000.

On LAN, find device IP via ip addr show → http://<IP>:5000.

Open mobile browser (Chrome Android / Safari iOS) and navigate to the Flask URL.

Enter the following:

Latitude / Longitude / Altitude

Time (HH:MM:SS)

Timezone Offset (+/-HH:MM)

Google Form URL / Target page

Click Apply Location & Open Form → location and time are spoofed.

# 📌 Sample Coordinates & Timezone Examples
~~~
Location	              Latitude	    Longitude	        Altitude (m)	   Time	      Timezone Offset
Eiffel Tower, Paris	        48.8584       	2.2945	          324	          15:20       	+02:00
Statue of Liberty, NY	  40.6892	      -74.0445	          93	          10:30	        -04:00
Taj Mahal, India	      27.1751	       78.0421	          171	          18:00        	+05:30
Sydney Opera House	    -33.8568	     151.2153	          65	          08:45	        +10:00

Use these for testing purposes.
~~~
# ⚙️ Configuration & Customization

You can modify:

**Latitude, longitude, and altitude precision**

Time and timezone offsets

Target URLs (forms, test pages)

Flask server port or host IP if needed

Refer to app.py and index.html for additional parameters.

# 📄 Educational & Ethical Purpose

Learning: Understand geolocation and time APIs in browsers.

Testing: Simulate location/time-specific behavior in apps or forms.

Research: Study web-based security checks and how they detect spoofing.

Works fully in mobile environments without rooting the device.
Refreshing the page restores real location and time.

# ⚖️ Legal & Ethical Use Policy

Consent: Only test in environments where you are authorized.

Prohibited Use: Misrepresenting location/time for fraud or unauthorized submission is illegal.

Intended Use Cases:

Ethical hacking education

Penetration testing (authorized)

Academic research

Compliance: Ensure adherence to local laws such as GDPR, IT Act 2000 (India), CFAA (USA), etc.

# 🛡️ Recommended Best Practices

Use virtual environments to isolate dependencies.

Test only in authorized networks and forms.

Document testing activities for accountability.

Refresh browser to restore real location and time after tests.

# 📄 License

MIT License – free for educational, research, and authorized testing purposes.

You are allowed to:

**Use the software for learning, testing, and experimentation in controlled environments.**

**Modify the code for research or educational purposes.**

Distribute it with the original copyright and license information intact.

Restrictions & Responsibilities:

Do not use this software for illegal, fraudulent, or unauthorized activities.

Ensure testing is done in authorized environments only.

The software is provided “as is,” without warranties. Authors are not liable for misuse or legal consequences.

By using this software, you agree to deploy it only in ethical and authorized contexts.
