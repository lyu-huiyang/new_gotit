# coding=utf-8
from bs4 import BeautifulSoup

html_ = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html lang="gb2312">
<head>
<title>现代教学管理信息系统</title><meta content="IE=EmulateIE7" http-equiv="X-UA-Compatible">
<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
<meta content="gb2312" http-equiv="Content-Language">
<meta content="all" name="robots">
<meta content="作者信息" name="author">
<meta content="版权信息" name="Copyright">
<meta content="站点介绍" name="description">
<meta content="站点关键词" name="keywords">
<link href="style/base/favicon.ico" rel="icon" type="image/x-icon">
<link href="style/base/jw.css" media="all" rel="stylesheet" type="text/css">
<link href="style/standard/jw.css" media="all" rel="stylesheet" type="text/css">
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
</link></link></link></meta></meta></meta></meta></meta></meta></meta></meta></head>
<body>
<!--<OBJECT id="factory" style="DISPLAY: none" codeBase="ScriptX.cab#Version=5,60,0,360" classid="clsid:1663ed61-23eb-11d2-b92f-008048fdd814"
			VIEWASTEXT>
		</OBJECT>-->
<form action="xskbcx.aspx?xh=14110543055&amp;xm=%C2%C0%BB%E6%D1%EE&amp;gnmkdm=N121603" id="xskb_form" method="post" name="xskb_form">
<input name="__EVENTTARGET" type="hidden" value=""/>
<input name="__EVENTARGUMENT" type="hidden" value=""/>
<input name="__VIEWSTATE" type="hidden" value="dDwzOTI4ODU2MjU7dDw7bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwyPjtpPDQ+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE1PjtpPDI0PjtpPDI2PjtpPDI4PjtpPDMwPjtpPDMyPjtpPDM0Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4bjt4bjs+Pjs+O3Q8aTwyPjtAPDIwMTUtMjAxNjsyMDE0LTIwMTU7PjtAPDIwMTUtMjAxNjsyMDE0LTIwMTU7Pj47bDxpPDA+Oz4+Ozs+O3Q8dDw7O2w8aTwxPjs+Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpuWPt++8mjE0MTEwNTQzMDU1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlp5PlkI3vvJrlkJXnu5jmnag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpumZou+8muiuoeeul+acuuenkeWtpuS4juaKgOacr+WtpumZojs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiT5Lia77ya6K6h566X5py656eR5a2m5LiO5oqA5pyv77yI5Lit54ix5ZCI5L2c5Yqe5a2m77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzooYzmlL/nj63vvJrorqHnp5ExNDAyKOS4reWklik7Pj47Pjs7Pjt0PDtsPGk8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtsPGk8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MD47aTwwPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDA+O2k8MD47bDw+Oz4+Oz47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MT47aTwwPjtpPDA+O2w8Pjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MD47aTwwPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+Oz7uJmj9STuRuq3XKP2a1VKuTzgtKw=="/>
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
<table class="formlist noprint" id="Table2" width="100%">
<tr>
<td align="center"><select id="xnd" language="javascript" name="xnd" onchange="__doPostBack('xnd','')">
<option selected="selected" value="2015-2016">2015-2016</option>
<option value="2014-2015">2014-2015</option>
</select><span id="Label2"><font size="4">学年第</font></span><select id="xqd" language="javascript" name="xqd" onchange="__doPostBack('xqd','')">
<option value="1">1</option>
<option selected="selected" value="2">2</option>
<option value="3">3</option>
</select><span id="Label1"><font size="4">学期学生个人课程表</font></span></td>
</tr>
<tr class="trbg1">
<td><span id="Label5">学号：14110543055</span>|
									<span id="Label6">姓名：吕绘杨</span>|
									<span id="Label7">学院：计算机科学与技术学院</span>|
									<span id="Label8">专业：计算机科学与技术（中爱合作办学）</span>|
									<span id="Label9">行政班：计科1402(中外)</span>
									    <span id="labTS"><font color="Red"></font></span><span id="labTip"><font color="Red"></font></span>            <input class="button" id="btnPrint" name="btnPrint" onclick="window.print();" style="DISPLAY:none" type="button" value="打印课表"/>
</td>
</tr>
</table>
<br>
<table border="0" bordercolor="Black" class="blacktab" id="Table1" width="100%">
<tr>
<td colspan="2" rowspan="1" width="2%">时间</td><td align="Center" width="14%">星期一</td><td align="Center" width="14%">星期二</td><td align="Center" width="14%">星期三</td><td align="Center" width="14%">星期四</td><td align="Center" width="14%">星期五</td><td align="Center" class="noprint" width="14%">星期六</td><td align="Center" class="noprint" width="14%">星期日</td>
</tr><tr>
<td colspan="2">早晨</td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center" class="noprint"> </td><td align="Center" class="noprint"> </td>
</tr><tr>
<td rowspan="4" width="1%">上午</td><td width="1%">第1节</td><td align="Center" rowspan="2" width="7%">软件开发工程<br>周一第1,2节{第1-15周}<br>邵宝民<br>教9211(西)</br></br></br></td><td align="Center" rowspan="2" width="7%">软件测试与检验<br>周二第1,2节{第1-15周}<br>张艳华<br>教9211(西)</br></br></br></td><td align="Center" rowspan="2" width="7%">移动应用程序开发<br>周三第1,2节{第1-15周}<br>李盘靖<br>教9211(西)</br></br></br></td><td align="Center" rowspan="2" width="7%">软件开发工程<br>周四第1,2节{第1-15周}<br>邵宝民<br>教9211(西)</br></br></br></td><td align="Center" rowspan="2" width="7%">数据库系统<br>周五第1,2节{第1-15周}<br>刘树淑<br>教9211(西)</br></br></br></td><td align="Center" class="noprint" width="7%"> </td><td align="Center" class="noprint" width="7%"> </td>
</tr><tr>
<td>第2节</td><td align="Center" class="noprint"> </td><td align="Center" class="noprint"> </td>
</tr><tr>
<td>第3节</td><td align="Center" rowspan="2">计算机网络(A)<br>周一第3,4节{第1-15周}<br>吕昌泰<br>教9211(西)</br></br></br></td><td align="Center"> </td><td align="Center" rowspan="2">离散数学(B)<br>周三第3,4节{第1-13周}<br>方春<br>教9211(西)</br></br></br></td><td align="Center" rowspan="2">软件测试与检验<br>周四第3,4节{第1-15周}<br>张艳华<br>教9211(西)</br></br></br></td><td align="Center" rowspan="2">大学英语读写(A)Ⅳ<br>周五第3,4节{第1-15周|单周}<br>亓凤琴<br>教3409(西)</br></br></br></td><td align="Center" class="noprint" rowspan="2">体育(A)Ⅳ<br>周六第3,4节{第1-12周}<br>刘云午<br/></br></br></td><td align="Center" class="noprint"> </td>
</tr><tr>
<td>第4节</td><td align="Center"> </td><td align="Center" class="noprint"> </td>
</tr><tr>
<td rowspan="4" width="1%">下午</td><td>第5节</td><td align="Center" rowspan="2">离散数学(B)<br>周一第5,6节{第1-13周}<br>方春<br>教9211(西)</br></br></br></td><td align="Center" rowspan="2">大学英语读写(A)Ⅳ<br>周二第5,6节{第1-16周}<br>亓凤琴<br>教3412(西)</br></br></br></td><td align="Center" rowspan="2">数据库系统<br>周三第5,6节{第1-15周}<br>刘树淑<br>教9211(西)</br></br></br></td><td align="Center"> </td><td align="Center" rowspan="2">移动应用程序开发<br>周五第5,6节{第1-15周}<br>李盘靖<br>教9211(西)</br></br></br></td><td align="Center" class="noprint"> </td><td align="Center" class="noprint"> </td>
</tr><tr>
<td>第6节</td><td align="Center"> </td><td align="Center" class="noprint"> </td><td align="Center" class="noprint"> </td>
</tr><tr>
<td>第7节</td><td align="Center"> </td><td align="Center"> </td><td align="Center" rowspan="2">计算机网络(A)<br>周三第7,8节{第1-15周}<br>吕昌泰<br>教9211(西)</br></br></br></td><td align="Center"> </td><td align="Center"> </td><td align="Center" class="noprint"> </td><td align="Center" class="noprint"> </td>
</tr><tr>
<td>第8节</td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center" class="noprint"> </td><td align="Center" class="noprint"> </td>
</tr><tr>
<td rowspan="2" width="1%">晚上</td><td>第9节</td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center" class="noprint"> </td><td align="Center" class="noprint"> </td>
</tr><tr>
<td>第10节</td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center"> </td><td align="Center" class="noprint"> </td><td align="Center" class="noprint"> </td>
</tr>
</table>
<br>
<div align="left" class="noprint">调、停（补）课信息：</div>
<table border="0" cellpadding="3" cellspacing="0" class="datelist noprint" id="DBGrid" width="100%">
<tr class="datelisthead">
<td>编号</td><td>课程名称</td><td>原上课时间地点教师</td><td>现上课时间地点教师</td><td>申请时间</td>
</tr>
</table>
<table class="noprint" id="Table3" width="100%">
<tr>
<td align="left">实践课(或无上课时间)信息：</td>
</tr>
<tr>
<td valign="top"><table border="0" cellpadding="3" cellspacing="0" class="datelist" id="DataGrid1" width="100%">
<tr class="datelisthead">
<td>课程名称</td><td>教师</td><td>学分</td><td>起止周</td><td>上课时间</td><td>上课地点</td>
</tr>
</table></td>
</tr>
<tr>
<td align="left">实习课信息：</td>
</tr>
<tr>
<td><table border="0" cellpadding="3" cellspacing="0" class="datelist" id="DBGridYxkc" width="100%">
<tr class="datelisthead">
<td>学年</td><td>学期</td><td>课程名称</td><td>实习时间</td><td>模块代号</td><td>先修模块</td><td>实习编号</td>
</tr>
</table></td>
</tr>
<tr>
<td align="left">未安排上课时间的课程：</td>
</tr>
<tr>
<td><table border="0" cellpadding="3" cellspacing="0" class="datelist" id="Datagrid2" width="100%">
<tr class="datelisthead">
<td>学年</td><td>学期</td><td>课程名称</td><td>教师姓名</td><td>学分</td>
</tr>
</table></td>
</tr>
</table>
</br></br></span>
<div class="footbox noprint"><em class="footbox_con"><span class="pagination"></span>
<span class="footbutton"></span>
<!-- 底部按钮位置 --></em></div>
</div>
</div>
</form>
</body>
</html>'''

soup = BeautifulSoup(html_, "html5lib")

stu_info = []
stu_id = soup.find_all("span", id="Label5")[0].get_text().strip()
stu_name = soup.find_all("span", id="Label6")[0].get_text().strip()
stu_school = soup.find_all("span", id="Label7")[0].get_text().strip()
stu_zhuanye = soup.find_all("span", id="Label8")[0].get_text().strip()
stu_class = soup.find_all("span", id="Label9")[0].get_text().strip()

stu_info.append(stu_id)
stu_info.append(stu_name)
stu_info.append(stu_school)
stu_info.append(stu_zhuanye)
stu_info.append(stu_class)

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

for i in classes[13].find_all("td", align="Center"):
    class_10_list.append(i.get_text().strip())
    print '10', i.get_text().strip()

all_classes.append(class_12_list)
all_classes.append(class_34_list)
all_classes.append(class_56_list)
all_classes.append(class_78_list)
all_classes.append(class_9_list)
all_classes.append(class_10_list)

return_info = []
return_info.append(stu_info)
return_info.append(all_classes)
