FROM debian:13


# Create a non-root user with sudo privileges
RUN apt-get update && apt-get install -y sudo git bash-completion vim nano
RUN useradd --create-home --shell /bin/bash dev
RUN usermod -aG sudo dev
RUN echo "dev ALL=(ALL) NOPASSWRD:ALL" | sudo tee /etc/sudoers.d/username

#setup python dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# 3. Install Argos Translate system-wide
RUN pip install --break-system-packages argostranslate

# 4. Pre-download & install English -> French model into the image layer
RUN python3 -c "import argostranslate.package; \
    argostranslate.package.update_package_index(); \
    pkgs = argostranslate.package.get_available_packages(); \
    en_fr = next(filter(lambda x: x.from_code == 'en' and x.to_code == 'fr', pkgs)); \
    argostranslate.package.install_from_path(en_fr.download())"

USER dev