#元字符
'''
. 匹配除换行符外的任意字符
* 重复前面的子表达式0次或多次
+ 重复前面的子表达式1次或更多次
？重复前面的子表达式0次或一次
^ 匹配字符串的开始
$ 匹配字符串的结束
{n} 重复n次
{n,} 重复n次或更多次
{n,m} 重复n次到m次
\b 匹配单词的开始或结尾即单词的边界，"\b"匹配非单词边界
\d 匹配数字，"\D"匹配任意非数字字符
\s 匹配任意空白符   "\S"匹配任意非空白符
\w 匹配任意字母、数字或下划线的标识符字符，"\W"匹配任意非标识符字符
[a-z] 匹配指定范围内的任意字符 [0-9]
[^a-z]匹配任何不在指定范围内的任意字符
()组成分组，当成整体


匹配实例：
[a-zA-Z]{1,}匹配单词
[0-9]{1,}  或 \d{1,}  匹配数字
\d{1,}\.\d{1,}  匹配浮点数
\d{1,4}(\.\d{1,4}){3} 若不捕获最后的元组 \d{1,4}(?:\.\d{1,4}){3} 匹配IP地址
hello (.*?) haha和hello (.*) haha    hello hi haha hi haha cadcasd hi haha 有?是一种非贪婪的模式，该分组它找到第一个匹配的分组就停止寻找匹配；没有?是一种贪婪模式，该分组会一直寻找匹配直到字符串结尾
\s+ 匹配换行
.*  匹配通用字符串
'''

'''
http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1

href="/en/vnl/2018/women/teams/.*">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>

href="/en/vnl/2018/women/teams/usa-usa">USA</a></figcaption>
                            </figure>
                        </td>
                        <td>15</td>
                        <td class="table-td-bold">13</td>
                        <td class="table-td-rightborder">2</td>
href="/en/vnl/2018/women/teams/srb-serbia">Serbia</a></figcaption>
                            </figure>
                        </td>
                        <td>15</td>
                        <td class="table-td-bold">12</td>
                        <td class="table-td-rightborder">3</td>

'''