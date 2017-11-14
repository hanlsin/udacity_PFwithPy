import urllib.request

def read_text():
    quotes = open("/Users/yp/study/udacity/udacity_PFwithPy/check_profanity/movie_quotes.txt")
    contents_of_file = quotes.read()
    # print(contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()

def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q=" + text_to_check
    #url = "http://www.wdylike.appspot.com/?q=shit"
    # print(url)
    req = urllib.request.Request(url)
    conn = urllib.request.urlopen(req)
    output = str(conn.read().decode('utf-8').strip())
    # print(output)
    conn.close()

    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("this document has no curse word!")
    else :
        print("could not scan the document properly.")

read_text()