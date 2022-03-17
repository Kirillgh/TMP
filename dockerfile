FROM python:3.7
WORKDIR /usr/src/myapp
COPY requirements.txt ./
COPY setup.py /usr/src/myapp
COPY main.py /usr/src/myapp
COPY project_utils/. /usr/src/myapp/project_utils
COPY tasks/. /usr/src/myapp/tasks
RUN pip install --no-cache-dir -r requirements.txt && apt update && apt upgrade -y \
&& apt-get install ffmpeg zlib* libjpeg* python3-setuptools -y && apt-get install snapd -y\
&& /usr/local/bin/python -m pip install --upgrade pip && pip3 install --user wheel && pip3 install --user gif-for-cli\
&& pip3 install --user gif-for-cli \
&& echo "if [ "$BASH" ]; if [ -f ~/.bashrc ];. ~/.bashrc fi if [ -d "$HOME/.local/bin" ] ; PATH="$HOME/.local/bin:$PATH" fi fi" > ~/.profile 
