from flask import Flask, render_template,request
import os
import subprocess
app = Flask(__name__)
app.debug=True

@app.route('/')
def homePage():
	return render_template('index.html')

@app.route('/welcome',methods = ['POST', 'GET'])
def finalPage():
	if request.method == 'POST':
		result =request.form
	print(result)
	return render_template('welcome.html')


if __name__ == '__main__':
	# os.chdir("C://Users//Ekansh PC//Desktop//Scrapy//FindingFeeds//FindingFeeds")
	# print(os.getcwd())
	# subprocess.call("scrapy crawl getFeedUrls_2")
	app.run()