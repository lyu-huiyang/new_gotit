# coding=utf-8
from bs4 import BeautifulSoup

html_ = '''



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<HTML lang="gb2312">
	<HEAD>
		<title>现代教学管理信息系统</title><meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7">
		<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
		<meta http-equiv="Content-Language" content="gb2312">
		<meta content="all" name="robots">
		<meta content="作者信息" name="author">
		<meta content="版权信息" name="Copyright">
		<meta content="站点介绍" name="description">
		<meta content="站点关键词" name="keywords">
		<LINK href="style/base/favicon.ico" type="image/x-icon" rel="icon">
			<LINK media="all" href="style/base/jw.css" type="text/css" rel="stylesheet">
				<LINK media="all" href="style/standard/jw.css" type="text/css" rel="stylesheet">
					<!--<script defer>
		function  PutSettings()
			{
			factory.printing.header="";
			factory.printing.footer="";
		    factory.printing.leftMargin="5";
			factory.printing.topMargin="5";
			factory.printing.rightMargin="5";
			factory.printing.bottomMargin="5";
		 }

					</script>-->
					<style> @media Print { .bgnoprint { }
	.noprint { DISPLAY: none }}
	</style>
	</HEAD>
	<BODY>
		<!--<OBJECT id="factory" style="DISPLAY: none" codeBase="ScriptX.cab#Version=5,60,0,360" classid="clsid:1663ed61-23eb-11d2-b92f-008048fdd814"
			VIEWASTEXT>
		</OBJECT>-->
		<form name="xskb_form" method="post" action="xskbcx.aspx?xh=14120905060&amp;xm=%C2%C0%C3%F7%D3%B1&amp;gnmkdm=N121603" id="xskb_form">
<input type="hidden" name="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" value="dDwzOTI4ODU2MjU7dDw7bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwyPjtpPDQ+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE1PjtpPDI0PjtpPDI2PjtpPDI4PjtpPDMwPjtpPDMyPjtpPDM0Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4bjt4bjs+Pjs+O3Q8aTwyPjtAPDIwMTUtMjAxNjsyMDE0LTIwMTU7PjtAPDIwMTUtMjAxNjsyMDE0LTIwMTU7Pj47bDxpPDA+Oz4+Ozs+O3Q8dDw7O2w8aTwxPjs+Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpuWPt++8mjE0MTIwOTA1MDYwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlp5PlkI3vvJrlkJXmmI7popY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpumZou+8muW7uuetkeW3peeoi+WtpumZojs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiT5Lia77ya5Z+O5Lmh6KeE5YiSOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzooYzmlL/nj63vvJrln47op4QxNDAyOz4+Oz47Oz47dDw7bDxpPDE+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+O3Q8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47bDxpPDE+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDA+O2k8MD47bDw+Oz4+Oz47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MT47aTwyPjtpPDI+O2w8Pjs+Pjs+Ozs7Ozs7Ozs7Oz47bDxpPDA+Oz47bDx0PDtsPGk8MT47aTwyPjs+O2w8dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOaAneaDs+aUv+ayu+eQhuiuuuivvuWunui3teaVmeWtpjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86YKT5pmT6Ie7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLjA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIxLTIyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOWxheS9j+W7uuetkeiuvuiuoeWOn+eQhuWPiuiuvuiuoeivvueoi+iuvuiuoShBKTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2Z5aicOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyMC0yMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDA+O2k8MD47bDw+Oz4+Oz47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MT47aTwyPjtpPDI+O2w8Pjs+Pjs+Ozs7Ozs7Ozs7Oz47bDxpPDA+Oz47bDx0PDtsPGk8MT47aTwyPjs+O2w8dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MjAxNS0yMDE2Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmgJ3mg7PmlL/msrvnkIborrror77lrp7ot7XmlZnlraY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmCk+aZk+iHuzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Mi4wOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MjAxNS0yMDE2Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlsYXkvY/lu7rnrZHorr7orqHljp/nkIblj4rorr7orqHor77nqIvorr7orqEoQSk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtmeWonDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MTs+Pjs+Ozs+Oz4+Oz4+Oz4+Oz4+Oz4+Oz4LJ2os/lgzhqcpi82zuj/rZAs15A==" />

<script language="javascript" type="text/javascript">
<!--
	function __doPostBack(eventTarget, eventArgument) {
		var theform;
		if (window.navigator.appName.toLowerCase().indexOf("microsoft") > -1) {
			theform = document.xskb_form;
		}
		else {
			theform = document.forms["xskb_form"];
		}
		theform.__EVENTTARGET.value = eventTarget.split("$").join(":");
		theform.__EVENTARGUMENT.value = eventArgument;
		theform.submit();
	}
// -->
</script>

			<!-- 多功能操作区 -->
			<!-- 内容显示区开始 -->
			<div class="main_box ">
				<div class="mid_box">
					<div class="title noprint">
						<p>
							<!-- 查询得到的数据量显示区域 --></p>
					</div>
					<!-- From内容 --><span class="formbox">
						<TABLE class="formlist noprint" id="Table2" width="100%">
							<TR>
								<TD align="center"><select name="xnd" onchange="__doPostBack('xnd','')" language="javascript" id="xnd">
	<option selected="selected" value="2015-2016">2015-2016</option>
	<option value="2014-2015">2014-2015</option>

</select><span id="Label2"><font size="4">学年第</font></span><select name="xqd" onchange="__doPostBack('xqd','')" language="javascript" id="xqd">
	<option value="1">1</option>
	<option selected="selected" value="2">2</option>
	<option value="3">3</option>

</select><span id="Label1"><font size="4">学期学生个人课程表</font></span></TD>
							</TR>
							<TR class="trbg1">
								<TD><span id="Label5">学号：14120905060</span>|
									<span id="Label6">姓名：吕明颖</span>|
									<span id="Label7">学院：建筑工程学院</span>|
									<span id="Label8">专业：城乡规划</span>|
									<span id="Label9">行政班：城规1402</span>
									&nbsp;&nbsp;&nbsp;&nbsp;<span id="labTS"><font color="Red"></font></span><span id="labTip"><font color="Red"></font></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input name="btnPrint" id="btnPrint" type="button" class="button" style="DISPLAY:none" onclick="window.print();" value="打印课表" />
								</TD>
							</TR>
						</TABLE>
						<br>
						<table id="Table1" class="blacktab" bordercolor="Black" border="0" width="100%">
	<tr>
		<td colspan="2" rowspan="1" width="2%">时间</td><td align="Center" width="14%">星期一</td><td align="Center" width="14%">星期二</td><td align="Center" width="14%">星期三</td><td align="Center" width="14%">星期四</td><td align="Center" width="14%">星期五</td><td class="noprint" align="Center" width="14%">星期六</td><td class="noprint" align="Center" width="14%">星期日</td>
	</tr><tr>
		<td colspan="2">早晨</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td rowspan="4" width="1%">上午</td><td width="1%">第1节</td><td align="Center" rowspan="2" width="7%">建筑结构(A)<br>周一第1,2节{第1-14周}<br>张璐<br>教5103(西)</td><td align="Center" rowspan="2" width="7%">建筑阴影与透视(A)<br>{第1-16周|2节/周}<br>李正军<br>教3311(西)</td><td align="Center" width="7%">&nbsp;</td><td align="Center" rowspan="2" width="7%">建筑阴影与透视(A)<br>{第1-15周|2节/单周}<br>李正军<br>教4406(西)<br><br>居住建筑设计原理及设计(A)<br>周四第1,2节{第1-14周}<br>孙娜<br>教3401(西)</td><td align="Center" width="7%">&nbsp;</td><td class="noprint" align="Center" width="7%">&nbsp;</td><td class="noprint" align="Center" width="7%">&nbsp;</td>
	</tr><tr>
		<td>第2节</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td>第3节</td><td align="Center" rowspan="2">居住建筑设计原理及设计(A)<br>周一第3,4节{第1-14周}<br>孙娜<br>教5302(西)</td><td align="Center" rowspan="2">高级英语口语(B)<br>周二第3,4节{第2-16周|双周}<br>张楠<br>教3308(西)</td><td align="Center" rowspan="2">建筑结构(A)<br>周三第3,4节{第1-14周}<br>张璐<br>教4402(西)</td><td align="Center" rowspan="2">毛泽东思想和中国特色社会主义理论体系概论(B)<br>周四第3,4节{第1-16周}<br>白云<br>教3301(西)</td><td align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td>第4节</td><td align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td rowspan="4" width="1%">下午</td><td>第5节</td><td align="Center" rowspan="2">建筑构造(B)<br>周一第5,6节{第1-15周|单周}<br>杨光杰<br>教5402(西)</td><td align="Center">&nbsp;</td><td align="Center" rowspan="2">建筑构造(B)<br>周三第5,6节{第1-16周}<br>杨光杰<br>教5302(西)</td><td align="Center">&nbsp;</td><td align="Center" rowspan="2">体育(A)Ⅳ<br>周五第5,6节{第1-12周}<br>曹永光<br></td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td>第6节</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td>第7节</td><td align="Center">&nbsp;</td><td align="Center" rowspan="2">毛泽东思想和中国特色社会主义理论体系概论(B)<br>周二第7,8节{第1-16周}<br>白云<br>教3216(西)</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td align="Center" rowspan="2">高级英语口语(B)<br>周五第7,8节{第1-16周}<br>张楠<br>教3308(西)</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td>第8节</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td rowspan="2" width="1%">晚上</td><td>第9节</td><td align="Center" rowspan="2">诉讼与正义<br>周一第9,10节{第10-13周}<br>张波1<br>教5101(西)</td><td align="Center" rowspan="2">服装设计与审美定位<br>周二第9,10节{第7-12周}<br>宋金英<br>教4205(西)</td><td align="Center" rowspan="2">诉讼与正义<br>周三第9,10节{第10-13周}<br>张波1<br>教5101(西)</td><td align="Center" rowspan="2">服装设计与审美定位<br>周四第9,10节{第7-12周}<br>宋金英<br>教4205(西)</td><td align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr><tr>
		<td>第10节</td><td align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td><td class="noprint" align="Center">&nbsp;</td>
	</tr>
</table>
						<br>


						<div class="noprint" align="left">调、停（补）课信息：</div>
						<table class="datelist noprint" cellspacing="0" cellpadding="3" border="0" id="DBGrid" width="100%">
	<tr class="datelisthead">
		<td>编号</td><td>课程名称</td><td>原上课时间地点教师</td><td>现上课时间地点教师</td><td>申请时间</td>
	</tr>
</table>
						<TABLE class="noprint" id="Table3" width="100%">
							<TR>
								<TD align="left">实践课(或无上课时间)信息：</TD>
							</TR>
							<TR>
								<TD valign="top"><table class="datelist" cellspacing="0" cellpadding="3" border="0" id="DataGrid1" width="100%">
	<tr class="datelisthead">
		<td>课程名称</td><td>教师</td><td>学分</td><td>起止周</td><td>上课时间</td><td>上课地点</td>
	</tr><tr>
		<td>思想政治理论课实践教学</td><td>邓晓臻</td><td>2.0</td><td>21-22</td><td>&nbsp;</td><td>&nbsp;</td>
	</tr><tr class="alt">
		<td>居住建筑设计原理及设计课程设计(A)</td><td>孙娜</td><td>1</td><td>20-20</td><td>&nbsp;</td><td>&nbsp;</td>
	</tr>
</table></TD>
							</TR>
							<TR>
								<TD align="left">实习课信息：</TD>
							</TR>
							<TR>
								<TD><table class="datelist" cellspacing="0" cellpadding="3" border="0" id="DBGridYxkc" width="100%">
	<tr class="datelisthead">
		<td>学年</td><td>学期</td><td>课程名称</td><td>实习时间</td><td>模块代号</td><td>先修模块</td><td>实习编号</td>
	</tr>
</table></TD>
							</TR>
							<TR>
								<TD align="left">未安排上课时间的课程：</TD>
							</TR>
							<TR>
								<TD><table class="datelist" cellspacing="0" cellpadding="3" border="0" id="Datagrid2" width="100%">
	<tr class="datelisthead">
		<td>学年</td><td>学期</td><td>课程名称</td><td>教师姓名</td><td>学分</td>
	</tr><tr>
		<td>2015-2016</td><td>2</td><td>思想政治理论课实践教学</td><td>邓晓臻</td><td>2.0</td>
	</tr><tr class="alt">
		<td>2015-2016</td><td>2</td><td>居住建筑设计原理及设计课程设计(A)</td><td>孙娜</td><td>1</td>
	</tr>
</table></TD>
							</TR>
						</TABLE>
					</span>
					<div class="footbox noprint"><em class="footbox_con"><span class="pagination"></span>
							<span class="footbutton"></span>
							<!-- 底部按钮位置 --></em></div>
				</div>
			</div>
		</form>
	</BODY>
</HTML>

'''

soup = BeautifulSoup(html_, "html5lib", from_encoding="utf-8")
a = soup.find_all("span")[5].get_text().strip()
print a


stu_info = []

stu_id = soup.find_all("span")[3].get_text().strip()
stu_name = soup.find_all("span")[4].get_text().strip()
stu_school = soup.find_all("span")[5].get_text().strip()
stu_zhuanye = soup.find_all("span")[6].get_text().strip()
stu_class = soup.find_all("span")[7].get_text().strip()


stu_info.append(stu_id)
stu_info.append(stu_name)
stu_info.append(stu_school)
stu_info.append(stu_zhuanye)
stu_info.append(stu_class)
print stu_info

all_classes = []
class_12_list = []
class_34_list = []
class_56_list = []
class_78_list = []
class_9_list = []
class_10_list = []

classes = soup.find_all("tr")

for i1 in classes[4].find_all("td", width="7%"):
    print '12', i1.get_text().strip()
    class_12_list.append(i1.get_text().strip())

for i2 in classes[6].find_all("td", align="Center"):
    class_34_list.append(i2.get_text().strip())
    print '34', i2.get_text().strip()

for i in classes[8].find_all("td", align="Center"):
    class_56_list.append(i.get_text().strip())
    print '56', i.get_text().strip()

for i in classes[10].find_all("td", align="Center"):
    class_78_list.append(i.get_text().strip())
    print '78', i.get_text().strip()

for i in classes[12].find_all("td", align="Center"):
    class_9_list.append(i.get_text().strip())
    print '9', i.get_text().strip()



all_classes.append(class_12_list)
all_classes.append(class_34_list)
all_classes.append(class_56_list)
all_classes.append(class_78_list)
all_classes.append(class_9_list)
all_classes.append(class_10_list)

return_info = []
return_info.append(stu_info)
return_info.append(all_classes)
