from bs4 import BeautifulSoup
import requests,csv

csv_file = open("coreyms.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title","Content","Video link"])

for page_num in range(1,3):
	source = requests.get(f"https://coreyms.com/page/{page_num}").text
	soup = BeautifulSoup(source, "lxml")
	
	for article in soup.find_all("article"):
		headline = article.header.h2.a.text
		print(headline)

		summary = article.find("div", class_ = "entry-content").p.text
		print(summary)


		try:
			vid_src = article.find("iframe", class_="youtube-player")["src"]
			vid_id = vid_src.split("/")[4]
			vid_id = vid_id.split("?")[0]
			yt_link = f"https://youtu.be/{vid_id}"

		except Exception as e:
			yt_link = None
		
		print(yt_link)

		print()

		csv_writer.writerow([headline, summary, yt_link])
		
csv_file.close()

