FROM debian:13


# Create a non-root user with sudo privileges
RUN apt-get update && apt-get install -y sudo git bash-completion vim nano
RUN useradd --create-home --shell /bin/bash dev
RUN usermod -aG sudo dev
RUN echo "dev ALL=(ALL) NOPASSWRD:ALL" | sudo tee /etc/sudoers.d/username

#setup python dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip install --break-system-packages googletrans==3.1.0a0

USER dev