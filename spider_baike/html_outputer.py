#coding:utf8
class HtmlOutputer(object):

    def __init__(self):
        self.datas=[]

    def collect_data(self, data):                               #把每个dict存进去
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=open('spiderBaiduBaike/spider_baike/output.html','w',encoding='utf-8')
        fout.write('<html>')
        fout.write('<head><meta charset="utf-8"></head>')        #防乱码
        fout.write('<body>')
        fout.write('<table>')

        #ascii
        for data in self.datas:
            fout.write('<tr>')
            #fout.write('<td class="tdURL">%s</td>' % data['url'])
            fout.write('<td class="tdTitle">%s</td>' % data['title'])
            fout.write('<td class="tdSummary">%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')