---
#Frontmatter
layout: post
title: Hospital Lab
---

# My Process
### Main Steps I Took
1. Query the server to generte a CSV with raw data.
2. Clean and standarize the data so I can find what I'm looking for: which county in NY state has the most hospital beds per person. This meant that I wanted to convert XHAB to 1HAB for each county, and then I want to find the max value in the beds column of the cleaned CSV. 
3. I then did an analysis of the cleaned CSV as described above to find which county in NY state has the most hospital beds per person.  

### The How & Setbacks
I knew that I had to access the API using similar techniques as the weather API classwork, so I approached this lab with the same techniques. There were two differences: 1) I had to get the "id"th row from the API that was accomplished with my getRow function and 2) I tested the data retreval with the status code 200, which indicates the request has succeeded otherwise it throws an error. Figuring out how to get the "id"th row rather than just inputting a known datapoint like in the weather API took me a minute to figure out, but I eventually got it during class. 

Now since I could access the data, I wanted to put it into a CSV. However, I realized that the data was plain text and not json like the weather API shown down below. So, I had to create a function I called rewrite to convert the plain text into a list, so then I could start cleaning and analyzing the raw data.

#### Plain Text 
![](plaintext.png)

#### JSON
![](json.png)

### Results 
I ended up finding that New York county has the most hospital beds per person. Not surprising :(

### Logistics 
In terms of who I worked with, I worked through code and errors in a breakout room with Alex, David, Lucca, and Ethan on Thursday. I asked Harry questions and checked my final answer for the county with the most hospital beds with him as well. I answered a few of Aidan's questions about creating the csv file.