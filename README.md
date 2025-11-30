Codex Hosts File–Based Ad Blocker

Codex Ad Blocker is a lightweight, system-level ad blocking tool built using Python and Streamlit.
Instead of relying on browser extensions, it modifies the Windows hosts file to block advertisements and tracking domains by redirecting them to 127.0.0.1, preventing ads from loading across all browsers.

The app includes a modern UI, theme customization, instant toggling, automatic backup, and a highly optimized block list.

Features
🔹 System-Wide Ad Blocking

Blocks ads and trackers across Chrome, Edge, Firefox, Brave, and all other apps.

🔹 Hosts File Redirection

Maps hundreds of ad-serving domains to 127.0.0.1, effectively blocking them.

🔹 One-Click On/Off Switch

Easily enable or disable ad blocking with a single toggle.

🔹 Automatic Backup

Creates a backup of the original hosts file before making any changes.

🔹 Dark & Light Theme Support

Choose between a sleek dark theme or a clean light theme.

🔹 Modern Streamlit UI

Gradient backgrounds, glowing status indicators, and a glassmorphism design.



How It Works

The app loads a predefined list of ad and tracking domains.

When activated, it appends the domains to the Windows hosts file:

127.0.0.1 domain.com


Any browser request to those domains fails instantly.

When deactivated, the app removes all entries it inserted.

The original hosts file is backed up to ensure safety.



Technologies Used

Python

Streamlit for the UI

HTML + CSS for custom styling

Windows Hosts File for blocking logic



Disclaimer

This tool modifies system files.
Use it responsibly and only on systems you own.
