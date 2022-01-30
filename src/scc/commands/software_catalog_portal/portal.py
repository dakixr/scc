import os
from distutils.dir_util import copy_tree
from bs4 import BeautifulSoup

from . import card
from scc import base_dir


def generate(repo_metadata_dir, output):

    global base
    
    # Make output dir
    if not os.path.exists(output):
        os.makedirs(output)

    # Copy all img to destination folder
    copy_tree(f"{base_dir}/assets/img", f"{output}/img")

    # Copy all languague_icons
    copy_tree(f"{base_dir}/assets/language_icons", f"{output}/language_icons")

    # Copy all repo_icons
    copy_tree(f"{base_dir}/assets/repo_icons", f"{output}/repo_icons")

    # Load the template
    with open(f"{base_dir}/assets/template.html") as template:
        soup = BeautifulSoup(template.read(), features="html.parser")

    # Insert cards for each repo
    card.insert_cards(repo_metadata_dir, soup)

    # Save index.html
    with open(f"{output}/index.html", "w") as index:
        index.write(str(soup))




