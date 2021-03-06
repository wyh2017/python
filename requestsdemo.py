#python的requests库的使用

import requests as http
print(dir(http))
# 参照这篇文章：https://blog.csdn.net/pittpakk/article/details/81218566
#用法，http.request(method='post',url = 'http://www.baidu.com',data={name:'wxl',age:'28'},**kwargs) method还可以是get,get的参数使用paramas={}

'''
**kwargs包含如下参数
## 传递cookie
cookies={

}
## 设置请求头
headers={

}
## 设置请求超时的时间
timeout = '10000'

## 设置代理
proxies = {
    'http':120.0.0.1,
    'https':120.0.0.1
}

## 是否对获取的内容进行立即下载
stream = true

## allow_redirects  是否允许对获取的内容进行重定向，默认为true

## auth 元组，用来支持http认证功能

# 返回的结果的api

r.status             //返回的状态码  300，301，400，404，500，200等
r.text               //返回的内容 unicode编码
r.encoding           //设置返回内容的编码
r.apparent_encoding  //从内容中返回内容的编码格式
r.content            //http相应内容的二进制形式
r.reason             
r.url                //请求的url
r.header             //返回的头信息
r.elapsed            //请求的时长

'''
## get请求传递
response = http.get('https://www.baidu.com/s',
        params={
            'wd':'python',
            'pn':'1'
        },
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        }
)
print(response.url)  #返回的结果为:https:www/baidu.com/s?wd='python'&pn=1

## 使用get方法下载一个静态页面
r = http.get('http://www.tomtop.com')
r.encoding='gbk'
with open('os/ss.html','w',encoding='utf-8') as f:
    f.write(r.text)
    f.close()
    print('下载页面成功')  #下载成功，吆喝呀，还做了反爬虫处理

## post请求的方法
r = http.get('https://www.baidu.com/s',
            params={
                'wd':'刘德华',
                'pn':1
            },
            headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
            }
)
print(r.apparent_encoding)
#print(r.text) 

with open('os/baidu.html','w',encoding = r.apparent_encoding) as f:
    f.write(r.text)   #注意cookie问题
    f.close()

## 带cookie

## 带headers参数

## request钩子函数
def  get_key_info(response,*args,**kwargs): #敲代码要认真啊
    '''
    response回调函数

    '''
    print(response.headers['Content-type'])
    print('*'*30)
    print(response.apparent_encoding)
    response.encoding = response.apparent_encoding ## 奇怪啊，为什么要这么设置用一下才不会出现乱码
    with open('os/test.html','w',encoding=response.apparent_encoding) as f:
        f.write(response.text)
        f.close()
        print('加载页面成功。')
    #good,写在钩子函数里面处理请求过来的数据

#hooks是一个回调钩子函数
res = http.get('https://www.baidu.com',hooks=dict(response = get_key_info))

# http认证

