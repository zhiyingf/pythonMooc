'''
新闻标题是新闻的主旨，从新闻标题中可以进行多种内容的挖掘，比如说可以爬取一段时间内的新闻进行分析，获得热点词
“从新闻标题中寻找热点词并且绘制词云”
有些用ajax技术（动态生成网页）渲染的网页怎样爬取数据
ajax技术不需要加载整个页面就可以更新部分网页内容
'''
import requests
r=requests.get('https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.7179944734364818&callback=jQuery1112002684082856709402_1570817462616&_=1570817462620')
print(r.status_code)
x=r.text.encode('utf-8').decode('unicode-escape')
print(x)


