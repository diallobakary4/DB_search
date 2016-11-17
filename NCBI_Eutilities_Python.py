#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Bakary N'tji Diallo"
__email__ = "diallobakary4@gmail.com"
#NCBI data extraction using Eutilities and Python
# More details "https://www.ncbi.nlm.nih.gov/books/NBK25498/

__author__ = "Bakary N'tji Diallo"
__email__ = "diallobakary4@gmail.com"

import requests

#Eutils search pipeline building
# 7 Eutilies cgi

eutils_base = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"               #base url to access eutils tools
esearch = "esearch.fcgi?"                                                   # ESearch – ESummary/EFetch
efetch = "efetch.fcgi?"                                                     #EFetch to retrieve full records)
elink = "elink.fcgi?"                                                       # ELink – ESummary/Efetch
epost = "epost.fcgi"                                                        # EPost – ELink – ESummary/EFetch
esummary = "esummary.fcgi"
egquery = "egquery.fcgi"
einfo = "einfo.fcgi"
# Goal: Download all Mycobacterium tuberculosis mRNA sequences in FASTA format.

# Solution: First use ESearch to retrieve the GI numbers for these sequences
#     and post them on the History server, then use multiple EFetch calls
#     to retrieve the data (in batch if too much)

# Input:
# Output: A file named "Mtb_mRNAs.fna" containing FASTA data.

param = """db=nuccore&term=(Mycobacterium tuberculosis[Organism]) AND "Mycobacterium tuberculosis"[porgn:__txid1773] """                              #parameters to specify your search

#esearch to have query and webenv params
url = eutils_base + esearch + param +"&usehistory=y"
print url
data = requests.get(url)
query_key = str(data.content[data.content.index("<QueryKey>") + 10 : data.content.index("</QueryKey>")])
webenv = str(data.content[data.content.index("<WebEnv>") + 8 : data.content.index("</WebEnv>")])

# detailled url structure
url = eutils_base + efetch + "db=nuccore" \
      + "&query_key=" + query_key + "&WebEnv=" + webenv + \
      "&retstart=1&retmax=36" + "&rettype=fasta" +	"&retmode=text"\
      +"&email=diallobakary4@gmail.com"

data = requests.get(url)

#Open a .fna file, extract fasta data, and write them in the .fna file.

file_name = "Mtb_mRNAs.fna"
with open(file_name, "w") as file:
    file.write(data.content)


#todo a second example with HIV mRNA