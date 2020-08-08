# 
# Example file for retrieving data from the internet
import urllib.request


def main():
          webUrl = urllib.request.urlopen("http://www.google.com")
          print("Status code : {}".format(webUrl.getcode()))
          data = webUrl.read()
          print(data)

if __name__ == "__main__":
  main()
