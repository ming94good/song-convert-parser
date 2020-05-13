#!/usr/bin/env python
#coding=utf-8
from flask import Flask, render_template, Response, request, redirect, url_for 
from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app=Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/search', methods = ['GET','POST'])
def search():
	website = 'https://song.corp.com.tw/songs.aspx?company=%E9%9F%B3%E5%9C%93&keyword='
	search_by_num = request.args.get('search')
	print(search_by_num)
	response = requests.get(website + search_by_num)
	soup = BeautifulSoup(response.content)
	divs = soup.findAll("div", {"class": "name"})
	try: 
	    result_name = divs[0].string
	except Exception as e:
	    print(e)  
	    
	print('(音圓)'+ search_by_num +': '+result_name)

	print('轉為弘音號碼...')

	website = 'https://song.corp.com.tw/songs.aspx?company=%E5%BC%98%E9%9F%B3&keyword=' 
	search_by_name = result_name
	response = requests.get(website + search_by_name)
	soup = BeautifulSoup(response.content)
	divs = soup.findAll("div", {"class": "code"})
	
	try:
	    result_code = divs[0].string
	    print('(弘音)'+ search_by_name +': '+result_code)
	except Exception as e:
	    print('弘音查無此曲')
	    result_code = '弘音查無此曲'
	return render_template('result.html', result1=search_by_name, result2=result_code)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
