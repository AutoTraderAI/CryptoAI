import { page } from 'node-html-parser';

var url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20201102&page=1"+date+ "&page="+page;
var result = ReadWebData(url, Encoding.Default);

String checkPage=GetMiddleString(result, "<div class=\"paging\">", "</string>");
checkPage = checkPage.Substring(checkPage.IndexOf("<strong")+ 8).Trim();

if(page.ToString() != checkPage)
{
    AddLog("해당 날짜의 탐색 페이지가 끝났습니다.");
    break;
}
else    
    AddLog("진행중 페이지 : " + page);

ParsingHtml(result, url);
page++;