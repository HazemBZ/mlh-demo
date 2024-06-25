# Installs geckodriver
# https://stackoverflow.com/questions/67090130/webdriverexception-process-unexpectedly-closed-with-status-255-selenium-ge

apt update && apt install -y curl wget bzip2 && \
apt install -y libxtst6 libgtk-3-0 libx11-xcb-dev libdbus-glib-1-2 libxt6 libpci-dev && \
wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz && \
tar -zxf geckodriver-v0.34.0-linux64.tar.gz -C /usr/local/bin && \
chmod +x /usr/local/bin/geckodriver && \
rm geckodriver-v0.34.0-linux64.tar.gz && \
\
# Installs firefox
\
FIREFOX_SETUP=firefox-setup.tar.bz2 && \
wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-95.0.1&os=linux64" && \
tar xjf $FIREFOX_SETUP -C /opt/ && \
ln -s /opt/firefox/firefox /usr/bin/firefox && \
rm $FIREFOX_SETUP