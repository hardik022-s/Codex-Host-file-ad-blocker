import os
import streamlit as st

# Codex Theme Toggle
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"], index=1)

# Sidebar style (applies to both themes)
st.markdown(
    """
    <style>
    /* Sidebar General */
    section[data-testid="stSidebar"] {
        background-color: #1E1E2F;
        padding: 20px;
    }
    .sidebar-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 15px;
        display: block;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown('<div class="sidebar-title">Codex Theme Settings</div>', unsafe_allow_html=True)

# Theme-specific global styles
if theme == "Dark":
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #0E1117;
            color: #FAFAFA !important;
        }
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: #FAFAFA !important;
        }
        .stButton>button {
            background-color: #1E1E1E;
            color: #FAFAFA;
            border-radius: 10px;
            border: 1px solid #4F8BF9;
            padding: 0.6em 1.2em;
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #4F8BF9;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:  # Light theme
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #FFFFFF;
            color: #1A1A1A !important;
        }
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: #1A1A1A !important;
        }
        .stButton>button {
            background-color: #E7E9EB;
            color: #000000;
            border-radius: 10px;
            border: 1px solid #4F8BF9;
            padding: 0.6em 1.2em;
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #4F8BF9;
            color: white;
        }
        section[data-testid="stSidebar"] {
            background-color: #F2F3F5;
        }
        .sidebar-title {
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
# CONFIG 
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
BACKUP_PATH = r"C:\Users\devil\Desktop\python\Codex\hosts_backup"

# Ad-block list 
BLOCK_LIST = [
    # Google Ads & Trackers
    "pagead2.googlesyndication.com",
    "partner.googleadservices.com",
    "googlesyndication.com",
    "googletagservices.com",
    "googletagmanager.com",
    "google-analytics.com",
    "adservice.google.com",
    "ad.doubleclick.net",
    "ads.google.com",

    # Facebook 
    "ads.facebook.com",
    "connect.facebook.net",
    "graph.facebook.com",
    "pixel.facebook.com",

    # Twitter / X
    "ads-api.twitter.com",
    "analytics.twitter.com",

    # YouTube Ads
    "ads.youtube.com",
    "s.youtube.com",
    "www.googleadservices.com",

    # Spotify (Web tracking only)
    "ads.spotify.com",
    "analytics.spotify.com",
    "log.spotify.com",

    # Microsoft Ads
    "ads.msn.com",
    "ads1.msn.com",
    "ads2.msads.net",
    "adnxs.com",

    # Amazon Ads
    "aax.amazon-adsystem.com",
    "amazon-adsystem.com",

    # Common Ad Networks
    "doubleclick.net",
    "scorecardresearch.com",
    "zedo.com",
    "adnxs.com",
    "serving-sys.com",
    "moatads.com",
    "contextweb.com",
    "advertising.com",
    "adform.net",
    "criteo.com",
    "rubiconproject.com",

    # Common Trackers / Analytics
    "stats.g.doubleclick.net",
    "quantserve.com",
    "optimizely.com",
    "omtrdc.net",
    "hotjar.com",
    "segment.io",
    "clicktale.net",
    "mathtag.com",

    # News Site Ads
    "ads.yahoo.com",
    "adserver.snapads.com",
    "adroll.com",
    "taboola.com",
    "outbrain.com",

    # Miscellaneous
    "tracking-protection.cdn.mozilla.net",
    "cdn.taboola.com",
    "cdn.doubleverify.com",
    "bttrack.com",
    "teads.tv",
    "fwmrm.net",

    # Instagram / Meta
    "ads.instagram.com",
    "graph.instagram.com",
    "business.instagram.com",
    "edge-mqtt.facebook.com",

    # Reddit Ads & Analytics
    "events.redditmedia.com",
    "ads.reddit.com",
    "rereddit.com",
    "pixel.reddit.com",

    # Snapchat
    "ads.snapchat.com",
    "tr.snapchat.com",
    "analytics.snapchat.com",
    "app-analytics.snapchat.com",

    # Pinterest
    "ads.pinterest.com",
    "log.pinterest.com",
    "trk.pinterest.com",
    "analytics.pinterest.com",

    # Apple Tracking & Ads
    "ads.apple.com",
    "iad.apple.com",
    "metrics.apple.com",
    "apptrailers.apple.com",

    # Adobe / Marketing Cloud
    "omtrdc.net",
    "demdex.net",
    "adobedtm.com",
    "2o7.net",

    # AppNexus / Xandr
    "adnxs.com",
    "ib.adnxs.com",
    "cdn.adnxs.com",
    "xandr.com",

    # Misc. Big Trackers
    "mathtag.com",
    "bluekai.com",
    "chartbeat.net",
    "revcontent.com",
    "adroll.com",
    "rubiconproject.com",
    "spotxchange.com",
]

# FUNCTIONS
def backup_hosts():
    """Create a backup of the original hosts file."""
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)
    os.system(f'copy "{HOSTS_PATH}" "{BACKUP_PATH}\\hosts_backup" >nul')

def is_blocking_enabled():
    """Check if Codex lines exist in hosts file."""
    try:
        with open(HOSTS_PATH, "r") as file:
            content = file.read()
            return "# Codex test line" in content
    except Exception:
        return False

def enable_blocking():
    """Append ad-block entries to hosts file."""
    try:
        backup_hosts()
        with open(HOSTS_PATH, "a") as file:
            file.write("\n# Codex test line\n")
            for site in BLOCK_LIST:
                file.write(f"127.0.0.1 {site}\n")
        return True
    except PermissionError:
        return False
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return False

def disable_blocking():
    """Remove Codex ad-block entries from hosts file."""
    try:
        with open(HOSTS_PATH, "r") as file:
            lines = file.readlines()
        with open(HOSTS_PATH, "w") as file:
            for line in lines:
                if "# Codex test line" not in line and not any(site in line for site in BLOCK_LIST):
                    file.write(line)
        return True
    except PermissionError:
        return False
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return False


# STREAMLIT UI 
st.set_page_config(page_title="Codex Ad Blocker", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
        body {
            background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
            color: #e0e0e0;
        }
        .main {
            background: rgba(15, 15, 30, 0.7);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 0 25px rgba(0, 255, 255, 0.2);
            backdrop-filter: blur(12px);
        }
        .stButton>button {
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            font-weight: 600;
            border-radius: 12px;
            padding: 10px 25px;
            border: none;
            transition: 0.3s ease;
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.6);
        }
        .status-light {
            width: 15px;
            height: 15px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 10px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 5px rgba(0,255,0,0.4); }
            50% { box-shadow: 0 0 20px rgba(0,255,0,1); }
            100% { box-shadow: 0 0 5px rgba(0,255,0,0.4); }
        }
        .header {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 10px rgba(0,255,255,0.3);
        }
        .info {
            text-align: center;
            color: #b0b0b0;
        }
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #00c6ff, transparent);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header'>🧠 Codex Ad Blocker</h1>", unsafe_allow_html=True)
st.markdown("<p class='info'>Next-Gen Ad Blocking Console</p>", unsafe_allow_html=True)

blocking_enabled = is_blocking_enabled()

st.markdown("<hr>", unsafe_allow_html=True)

# STATUS SECTION
if blocking_enabled:
    st.markdown("<span class='status-light' style='background:lime;'></span> <b>Ad Blocking is Active</b>", unsafe_allow_html=True)
else:
    st.markdown("<span class='status-light' style='background:red; animation:none;'></span> <b>Ad Blocking is Inactive</b>", unsafe_allow_html=True)

st.metric("Domains Blocked", len(BLOCK_LIST))

# TOGGLE SWITCH
toggle = st.toggle("Activate Ad Blocking", value=blocking_enabled)

if toggle != blocking_enabled:
    if toggle:
        if enable_blocking():
            st.success("✅ Ad blocking enabled successfully.")
            st.session_state["status"] = True
        else:
            st.error("⚠ Permission denied. Please run as Administrator.")
    else:
        if disable_blocking():
            st.warning("🛑 Ad blocking disabled.")
            st.session_state["status"] = False
        else:
            st.error("⚠ Permission denied. Please run as Administrator.")
    st.rerun() 
    
