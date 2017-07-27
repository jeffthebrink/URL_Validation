import httplib

if __name__ == "__main__":

    def validate_url(host, path="/"):
        try:
                connection = httplib.HTTPSConnection(url)
                connection.request("GET", "/")
                response = connection.getresponse()
                if response.status == 200:
                    print "URL is valid"
                    print ""
                else:
                    print "Not a valid URL"
                    print response.reason
                    print ""
        except IOError:
                print "IO Error Exception thrown"
                print "Was the spelling for the URL correct?"
                print ""

    while True:

        url = raw_input("Enter a URL to check: ")
        print ""

        if url[:4] != "www.":
            url = "www." + url
            print "* NOTE: www. added before URL"
            print ""

        validate_url(url)
