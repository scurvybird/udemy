import json
import random
import urllib.request
import argostranslate.package
import argostranslate.translate

# 1. Online source for raw English words (~370,000 words)
WORD_LIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

def setup_offline_translator(from_code="en", to_code="fr"):
    """Downloads and installs the offline translation package if not present."""
    print("Checking offline translation package...")
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code,
            available_packages
        ),
        None
    )
    if package_to_install:
        download_path = package_to_install.download()
        argostranslate.package.install_from_path(download_path)
        print("Offline English-to-French model ready.")

def fetch_english_words():
    """Downloads the list of English words into memory."""
    print("Downloading English word list...")
    req = urllib.request.Request(WORD_LIST_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    # Use set to ensure unique words and filter short entries
    return list({w.strip().lower() for w in content.splitlines() if len(w.strip()) >= 2})

def generate_large_json(num_entries, output_filename="en_fr_100k.json"):
    # Setup translator & load words
    setup_offline_translator("en", "fr")
    all_words = fetch_english_words()
    
    if num_entries > len(all_words):
        num_entries = len(all_words)
        
    print(f"Sampling {num_entries:,} words...")
    sampled_words = random.sample(all_words, num_entries)
    
    # Fetch installed translation model
    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang = next(filter(lambda x: x.code == "en", installed_languages))
    to_lang = next(filter(lambda x: x.code == "fr", installed_languages))
    translation_model = from_lang.get_translation(to_lang)
    
    print(f"Translating {num_entries:,} words locally...")
    translation_dict = {}
    
    # Process in memory
    for i, word in enumerate(sampled_words, 1):
        translation_dict[word] = translation_model.translate(word).lower()
        
        # Status update every 10,000 items
        if i % 10000 == 0 or i == num_entries:
            print(f"Processed {i:,} / {num_entries:,} words...")

    # Write single JSON output file
    print(f"Writing output to local file: {output_filename}...")
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(translation_dict, f, ensure_ascii=False, indent=2)

    print(f"Done! {len(translation_dict):,} entries written to {output_filename}")

if __name__ == "__main__":
    count = int(input("Enter number of entries to generate (e.g. 100000): "))
    generate_large_json(count)
