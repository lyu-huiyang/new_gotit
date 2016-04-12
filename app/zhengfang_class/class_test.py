# coding=utf-8
from bs4 import BeautifulSoup

html_ = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="gb2312"><head>
		<title>现代教学管理信息系统</title>
		<meta content="IE=EmulateIE7" http-equiv="X-UA-Compatible"/>
		<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
		<meta content="gb2312" http-equiv="Content-Language"/>
		<meta content="all" name="robots"/>
		<meta content="作者信息" name="author"/>
		<meta content="版权信息" name="Copyright"/>
		<meta content="站点介绍" name="description"/>
		<meta content="站点关键词" name="keywords"/>
		<link href="style/base/favicon.ico" rel="icon" type="image/x-icon"/>
			<link href="style/base/jw.css" media="all" rel="stylesheet" type="text/css"/>
				<link href="style/standard/jw.css" media="all" rel="stylesheet" type="text/css"/>
					<link href="js/extjs/css/ext-all.css" rel="stylesheet" type="text/css"/>
						<script src="js/extjs/ext/ext-base.js" type="text/javascript"></script>
						<script src="js/extjs/ext/ext-all.js" type="text/javascript"></script>
						<script src="js/xtwh.js" type="text/javascript"></script>
						<script language="javascript">
					function showWXKC(t,nr) {
						Ext.Msg.getDialog().setWidth(500);
						Ext.MessageBox.alert(t+"还需修课程",nr);
					}
            function window.onbeforeprint(){
                document.all.tabHidden.style.display = "none"
            }
            function window.onafterprint(){
                document.all.tabHidden.style.display = "block"
            }
           function click() {
                if (event.button==2) {  //改成button==2为禁止右键
					if (language())
					{
						alert('Sorry, this function is forbidden!');
					}
					else
					{
						alert('对不起,禁止使用此功能.');
					}
                }
            }
            document.onmousedown=click

              function SumCxxf(){
               obj=document.getElementById("Datagrid9");
			         intZfy=0.0;
			        intZfy1=0.0;

			        if(obj!=null)
			        {
			          for(i=1;i<obj.rows.length-1;i++)
			          { if (obj.rows[0].cells[5].innerText=="小计"){
			           intZfy=intZfy + parseFloat(obj.rows[i].cells[5].innerText);
			          } else
			          {
			            intZfy=intZfy + parseFloat(obj.rows[i].cells[6].innerText);
			          }

			          }
			           if (obj.rows[0].cells[5].innerText=="小计")
			          obj.rows[obj.rows.length-1].cells[5].innerText=intZfy;
			           else

			          obj.rows[obj.rows.length-1].cells[6].innerText=intZfy;
			        }
            }

            function language()
				{
					var lan=document.getElementById("hidLanguage").value;
					if (lan=="Chinese" || lan=="")
					{
						return false;
					}
					else
					{
						return true;
					}
				}
				function showZyfx()
				{
					document.getElementById("tdzymc").colSpan=1;
					document.getElementById("tdzyfx").style.display="";
				}
						</script>
</head>
	<body onload=" SumCxxf();reMoveCh('Form1','Iframe1');">
		<form action="xscjcx.aspx?xh=14120905060&amp;xm=u'lmy199659'&amp;gnmkdm=N121603" id="Form1" method="post" name="Form1">
<input name="__EVENTTARGET" type="hidden" value=""/>
<input name="__EVENTARGUMENT" type="hidden" value=""/>
<input name="__VIEWSTATE" type="hidden" value="dDw2NDI3MTcwOTk7dDxwPGw8U29ydEV4cHJlcztzZmRjYms7ZGczO2R5YnlzY2o7U29ydERpcmU7eGg7c3RyX3RhYl9iamc7Y2pjeF9sc2I7enhjamN4eHM7PjtsPGtjbWM7XGU7YmpnO1xlO2FzYzsxNDEyMDkwNTA2MDt6Zl9jeGNqdGpfMTQxMjA5MDUwNjA7OzA7Pj47bDxpPDE+Oz47bDx0PDtsPGk8ND47aTwxMD47aTwxOT47aTwyND47aTwzMj47aTwzND47aTwzNj47aTwzOD47aTw0MD47aTw0Mj47aTw0ND47aTw0Nj47aTw0OD47aTw1Mj47aTw1ND47aTw1Nj47PjtsPHQ8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxYTjtYTjs+Pjs+O3Q8aTwzPjtAPFxlOzIwMTUtMjAxNjsyMDE0LTIwMTU7PjtAPFxlOzIwMTUtMjAxNjsyMDE0LTIwMTU7Pj47Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8a2N4em1jO2tjeHpkbTs+Pjs+O3Q8aTw1PjtAPOW/heS/ruivvjvpgInkv67or7475YWs6YCJ6K++O+Wunui3teeOr+iKgjtcZTs+O0A8MDE7MDI7MDM7MDY7XGU7Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFxlOz4+Oz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOWtpuWPt++8mjE0MTIwOTA1MDYwO288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w85aeT5ZCN77ya5ZCV5piO6aKWO288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w85a2m6Zmi77ya5bu6562R5bel56iL5a2m6ZmiO288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w85LiT5Lia77yaO288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w85Z+O5Lmh6KeE5YiSO288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS4k+S4muaWueWQkTrml6DmlrnlkJE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w86KGM5pS/54+t77ya5Z+O6KeEMTQwMjtvPHQ+Oz4+Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+Oz47Ozs7Ozs7Ozs7Pjs7Pjt0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47aTw5PjtpPDEzPjtpPDE1PjtpPDE5PjtpPDIxPjtpPDIyPjtpPDIzPjtpPDI1PjtpPDI3PjtpPDI5PjtpPDMxPjtpPDMzPjtpPDQxPjtpPDQ3PjtpPDQ5PjtpPDUwPjs+O2w8dDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+O3A8bDxzdHlsZTs+O2w8RElTUExBWTpub25lOz4+Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8O2w8aTwxMz47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOiHs+S7iuacqumAmui/h+ivvueoi+aIkOe7qe+8mjtvPHQ+Oz4+Oz47Oz47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MT47aTwxPjtsPD47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOmJsb2NrOz4+Pjs7Ozs7Ozs7Ozs+O2w8aTwwPjs+O2w8dDw7bDxpPDE+Oz47bDx0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPEcxMjA2MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85bu6562R6Zi05b2x5LiO6YCP6KeGKEEpOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlv4Xkv67or747Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMuMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NTcuODs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtwPGw8c3R5bGU7PjtsPERJU1BMQVk6bm9uZTs+Pj47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOm5vbmU7Pj4+Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOm5vbmU7Pj4+Ozs7Ozs7Ozs7Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+O3A8bDxzdHlsZTs+O2w8RElTUExBWTpub25lOz4+Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+O3A8bDxzdHlsZTs+O2w8RElTUExBWTpub25lOz4+Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtwPGw8c3R5bGU7PjtsPERJU1BMQVk6bm9uZTs+Pj47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDtAMDw7O0AwPHA8bDxIZWFkZXJUZXh0Oz47bDzliJvmlrDlhoXlrrk7Pj47Ozs7PjtAMDxwPGw8SGVhZGVyVGV4dDs+O2w85Yib5paw5a2m5YiGOz4+Ozs7Oz47QDA8cDxsPEhlYWRlclRleHQ7PjtsPOWIm+aWsOasoeaVsDs+Pjs7Ozs+Ozs7Pjs7Ozs7Ozs7Oz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOacrOS4k+S4muWFsTY35Lq6O288Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFNEVVQ7Pj47Pjs7Pjt0PHA8cDxsPEltYWdlVXJsOz47bDwuL2V4Y2VsLzE0MTIwOTA1MDYwLmpwZzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwzPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjs+Pjs+Pjs+/rYDT1sI3SBRtoO0U+ZIkPQiSQg="/>

<script language="javascript" type="text/javascript">
<!--
	function __doPostBack(eventTarget, eventArgument) {
		var theform;
		if (window.navigator.appName.toLowerCase().indexOf("microsoft") > -1) {
			theform = document.Form1;
		}
		else {
			theform = document.forms["Form1"];
		}
		theform.__EVENTTARGET.value = eventTarget.split("$").join(":");
		theform.__EVENTARGUMENT.value = eventArgument;
		theform.submit();
	}
// -->
</script>

			<input id="hidLanguage" name="hidLanguage" type="hidden"/>
			<div class="toolbox" id="tabHidden">
				<!-- 按钮 -->
				<div class="buttonbox"></div>
				<!-- 按钮 -->
				<!-- 过滤条件开始 -->
				<div class="searchbox">
					<p class="search_con"><span id="Label1">学年:</span><select id="ddlXN" name="ddlXN">
	<option value=""></option>
	<option value="2015-2016">2015-2016</option>
	<option value="2014-2015">2014-2015</option>

</select><font face="宋体"> 
						</font>
						<span id="Label2">学期</span><select id="ddlXQ" name="ddlXQ">
	<option value=""></option>
	<option value="1">1</option>
	<option value="2">2</option>
	<option value="3">3</option>

</select>  
						<span id="Label3">课程性质</span><select id="ddl_kcxz" name="ddl_kcxz">
	<option value="01">必修课</option>
	<option value="02">选修课</option>
	<option value="03">公选课</option>
	<option value="06">实践环节</option>
	<option selected="selected" value=""></option>

</select></p>
					<p class="search_title"><em></em></p>
				</div>
				<div class="searchbox" style="WIDTH: 100%; CLEAR: both">
					<p class="search_con"><input class="button" id="btn_xq" name="btn_xq" type="submit" value="学期成绩"/><input class="button" id="btn_xn" name="btn_xn" type="submit" value="学年成绩"/><input class="button" id="btn_zcj" name="btn_zcj" type="submit" value="历年成绩"/><input class="button" id="btn_zg" name="btn_zg" type="submit" value="课程最高成绩"/><input class="button" id="Button2" name="Button2" type="submit" value="未通过成绩"/><input class="button" id="Button1" name="Button1" type="submit" value="成绩统计"/><input class="button" id="btn_dy" name="btn_dy" onclick="window.print();" type="button" value=" 打印 "/>


					</p>
					<p class="search_title"><em></em></p>
				</div>
				<!-- 过滤条件结束 -->
				<p class="toolbox_fot"><em></em></p>
			</div>
			<!-- 多功能操作区 -->
			<!-- 内容显示区开始 -->
			<div class="main_box">
				<div class="mid_box">
					<div class="title">
						<p>
							<!-- 查询得到的数据量显示区域 --></p>
					</div>
					<!-- From内容 -->
					<span class="formbox" style="OVERFLOW: hidden">
						<table cellpadding="3" cellspacing="0" class="formlist" id="Table1" width="100%">
							<tbody><tr>
								<td align="center" colspan="4" height="29"><span id="lbl_bt"><b><font size="4"></font></b></span></td>
							</tr>
							<tr>
								<td height="5"><span id="lbl_xh">学号：14120905060</span></td>
								<td height="5"><span id="lbl_xm">姓名：吕明颖</span></td>
								<td colspan="2" height="5"><span id="lbl_xy">学院：建筑工程学院</span></td>
							</tr>
							<tr>
								<td colspan="2" id="tdzymc"><span id="lbl_zy">专业：</span>
									<span id="lbl_zymc">城乡规划</span></td>
								<td id="tdzyfx"><span id="lbl_zyfx">专业方向:无方向</span></td>
								<td><span id="lbl_xzb">行政班：城规1402</span></td>
							</tr>
							<tr>
								<td colspan="4"></td>
							</tr>
						</tbody></table>

						<div id="divNotPs">

							<br/>

							<br/>

							<div align="left"><span id="lbl_grid3"><b>至今未通过课程成绩：</b></span></div>
							<table border="0" cellpadding="3" cellspacing="0" class="datelist" id="Datagrid3" style="DISPLAY:block" width="100%">
	<tbody><tr class="datelisthead">
		<td>课程代码</td><td><a href="javascript:__doPostBack('Datagrid3$_ctl1$_ctl0','')">课程名称</a></td><td>课程性质</td><td>学分</td><td>最高成绩值</td><td>课程归属</td>
	</tr><tr>
		<td>G12060</td><td>建筑阴影与透视(A)</td><td>必修课</td><td>3.0</td><td>57.8</td><td> </td>
	</tr>
</tbody></table>

							<table class="formlist" width="100%">
								<tbody><tr>
									<td colspan="2" width="400"></td>
									<td colspan="2">

									</td>
								</tr>
								<tr>
									<td colspan="2" width="400"></td>
									<td colspan="2"> </td>
								</tr>
								<tr>
									<td colspan="4"></td>
								</tr><tr>
									<td colspan="2" width="400"></td>
									<td colspan="2"></td>
								</tr>
								<tr>
									<td colspan="2"></td>
								</tr>
								<tr>
									<td></td>
									<td>

										<span id="pjxfjd_ffx"><b></b></span>
										<span id="pjxfjd_fx"><b></b></span>
									</td>
									<td>
										<span id="pjxfjd_xf"><b></b></span>
										           

										<span id="xfjdzh_ffx"><b></b></span>
										<span id="xfjdzh_fx"><b></b></span>
									</td>
									<td></td>
								</tr>
								<tr>
									<td align="right" colspan="4"><img alt="学生条形码" border="0" id="Image1" src="./excel/14120905060.jpg"/></td>
								</tr>
							</tbody></table>
						</div>
						<div id="divPs">
							<fieldset>
								<legend>
									<span id="lblpsts"><b></b></span>
								</legend>

							</fieldset>
						</div>
					</span>
					<div class="footbox"><em class="footbox_con"><span class="pagination"></span><span class="footbutton"></span>
							<!-- 底部按钮位置 --></em></div>
				</div>
			</div>
		</form>
</body></html>"""

soup = BeautifulSoup(html_, "html5lib", from_encoding="utf-8")

stu_info = []

stu_id = soup.find_all("span", id="Label5")[0].get_text().strip()
print stu_id
stu_name = soup.find_all("span", id="Label6")[0].get_text().strip()
print stu_name
stu_school = soup.find_all("span", id="Label7")[0].get_text().strip()
print stu_school
stu_zhuanye = soup.find_all("span", id="Label8")[0].get_text().strip()
print stu_zhuanye
stu_class = soup.find_all("span", id="Label9")[0].get_text().strip()
print stu_class

stu_info.append(stu_id)
stu_info.append(stu_name)
stu_info.append(stu_school)
stu_info.append(stu_zhuanye)
stu_info.append(stu_class)
#print stu_info

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
