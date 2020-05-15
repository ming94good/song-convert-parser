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
def index1():
	return render_template('index1.html')

@app.route('/index2', methods = ['GET','POST'])
def index2():
        return render_template('index2.html')

@app.route('/search1', methods = ['GET','POST'])
def search1():
	website = 'https://song.corp.com.tw/songs.aspx?company=%E9%9F%B3%E5%9C%93&keyword='
	search_by_num = request.args.get('search1')
	print(search_by_num)
	response = requests.get(website + search_by_num)
	soup = BeautifulSoup(response.content)
	divs = soup.findAll("div", {"class": "name"})
	code = soup.findAll("div", {"class": "code"})
	try: 
	    result_name = divs[0].string
	    result_code = code[0].string
	except Exception as e:
	    print(e)
	    result_code = '-100'	      
	
	if int(result_code) != int(search_by_num):
    		print('音圓查無此曲')
    		search_by_name = '音圓查無此曲'
    		result_code = '無法查詢'
	else:
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
		
	return render_template('result1.html', result1=search_by_name, result2=result_code)

@app.route('/search2', methods = ['GET','POST'])
def search2():
	website = 'https://song.corp.com.tw/songs.aspx?company=%E5%BC%98%E9%9F%B3&keyword=' 
	search_by_num = request.args.get('search2')
	print(search_by_num)
	response = requests.get(website + search_by_num)
	soup = BeautifulSoup(response.content)
	divs = soup.findAll("div", {"class": "name"})
	code = soup.findAll("div", {"class": "code"})
	try: 
	    result_name = divs[0].string
	    result_code = code[0].string
	except Exception as e:
	    print(e)
  	    result_code = '-100'

	if int(result_code) != int(search_by_num):
                print('弘音查無此曲')
                search_by_name = '弘音查無此曲'
                result_code = '無法查詢'
        else:	
		print('(弘音)'+ search_by_num +': '+result_name)
		print('轉為音圓號碼...')

		website = 'https://song.corp.com.tw/songs.aspx?company=%E9%9F%B3%E5%9C%93&keyword=' 
		search_by_name = result_name
		response = requests.get(website + search_by_name)
		soup = BeautifulSoup(response.content)
		divs = soup.findAll("div", {"class": "code"})
	
		try:
		    result_code = divs[0].string
	            print('(音圓)'+ search_by_name +': '+result_code)
		except Exception as e:
	    	    print('音圓查無此曲')
	       	    result_code = '音圓查無此曲'
	return render_template('result2.html', result1=search_by_name, result2=result_code)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
