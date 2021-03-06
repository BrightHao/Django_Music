$(function () {
    /*歌曲列表效果*/
    $(".songList").hover(function () {
        $(this).find(".more").show();
        $(this).find(".dele").show();
    }, function () {
        $(this).find(".more").hide();
        $(this).find(".dele").hide();
    });
    /*自定义滚动条*/
    $(".songUL").rollbar({zIndex: 80});
    //$("#lyr").rollbar({zIndex:80});
    /*复选框*/
    $(".checkIn").click(function () {
        var s = $(this).attr("select");
        if (s == 0) {
            $(this).css("background-position", "-37px -710px");
            $(this).attr("select", "1");
        }
        ;
        if (s == 1) {
            $(this).css("background-position", "");
            $(this).attr("select", "0");
        }
        ;
    });
    $(".checkAll").click(function () {
        var s = $(this).attr("select");
        if (s == 0) {
            $(this).css("background-position", "-37px -710px");
            $(".checkIn[select='0']").css("background-position", "-37px -710px");
            $(".checkIn[select='0']").attr("select", "1");
            $(this).attr("select", "1");
        }
        ;
        if (s == 1) {
            $(this).css("background-position", "");
            $(".checkIn[select='1']").css("background-position", "");
            $(".checkIn[select='1']").attr("select", "0");
            $(this).attr("select", "0");
        }
        ;

    });
    /*点击列表播放按钮*/
    $(".start em").click(function () {
        /*开始放歌*/
        var sid = $(this).attr("sonN");
        songIndex = sid;
        $("#audio").attr("src", 'http://music.163.com/song/media/outer/url?id=' + songIndex + '.mp3');	// 获得歌曲资源
        audio = document.getElementById("audio");//获得音频元素

        /*显示歌曲总长度*/
        if (audio.paused) {
            audio.play();
        } else
            audio.pause();
        audio.addEventListener('timeupdate', updateProgress, false);

        audio.addEventListener('play', audioPlay, false);
        audio.addEventListener('pause', audioPause, false);
        audio.addEventListener('ended', audioEnded, false);
        /*播放歌词*/
        getReady(songIndex);//准备播放
        mPlay();//显示歌词
        //对audio元素监听pause事件
        /*外观改变*/
        var html = "";
        $(".start em").css({
            "background": "",
            "color": ""
        });
        // $(".manyou").remove();
        $(".songList").css("background-color", "#f5f5f5");
        $(this).css({
            "background": 'url("../../static/songlist/css/images/T1X4JEFq8qXXXaYEA_-11-12.gif") no-repeat',
            "color": "transparent"
        });

        /*底部显示歌曲信息*/
        var songName = $(this).parent().parent().find(".colsn").html();
        var singerName = $(this).parent().parent().find(".colcn").html();
        var songpic = $(this).parent().parent().find(".pic").html();
        $(".songName").html(songName);
        $(".songPlayer").html(singerName);
        /*换右侧图片*/
        $("#canvas1").attr("src", songpic);
        $("#canvas1").load(function () {
            loadBG();
        });
        //setTimeout('loadBG()',100);
        $(".blur").css("opacity", "0");
        $(".blur").animate({opacity: "1"}, 1000);

    });
    /*双击播放*/
    $(".songList").dblclick(function () {
        var sid = $(this).find(".start em").attr("sonN");
        songIndex = sid;
        $(".start em[sonN=" + songIndex + "]").click();
    });
    /*底部进度条控制*/
    $(".dian").draggable({
        containment: ".pro2",
        drag: function () {
            var l = $(".dian").css("left");
            var le = parseInt(l);
            audio.currentTime = audio.duration * (le / 678);
        }
    });
    /*音量控制*/
    $(".dian2").draggable({
        containment: ".volControl",
        drag: function () {
            var l = $(".dian2").css("left");
            var le = parseInt(l);
            audio.volume = (le / 80);
        }
    });
    /*底部播放按钮*/
    $(".playBtn").click(function () {
        var p = $(this).attr("isplay");
        if (p == 0) {
            $(this).css("background-position", "0 -30px");
            $(this).attr("isplay", "1");
        }
        ;
        if (p == 1) {
            $(this).css("background-position", "");
            $(this).attr("isplay", "0");
        }
        ;
        if (audio.paused)
            audio.play();
        else
            audio.pause();

    });
    $(".mode").click(function () {
    });
    /*切歌*/
    $(".prevBtn").click(function () {
        var present_id = parseInt(songIndex);
        var present_num = $(".start em[sonN=" + present_id + "]").html();
        var sid = parseInt(present_num) - 1;
        $(".start em[id=" + sid + "]").click();
    });
    $(".nextBtn").click(function () {
        var present_id = parseInt(songIndex);
        var present_num = $(".start em[sonN=" + present_id + "]").html();
        var sid = parseInt(present_num) + 1;
        $(".start em[id=" + sid + "]").click();
    });
});

/*首尾模糊效果*/
function loadBG() {
    // alert();
    // stackBlurImage('canvas1', 'canvas', 60, false);
    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");
    var img = document.getElementById("canvas1");
    ctx.drawImage(img, 45, 45, 139, 115, 0, 0, 1366, 700);
    stackBlurCanvasRGBA('canvas', 0, 0, 1366, 700, 60);
}

function calcTime(time) {
    var hour;
    var minute;
    var second;
    hour = String(parseInt(time / 3600, 10));
    if (hour.length == 1) hour = '0' + hour;
    minute = String(parseInt((time % 3600) / 60, 10));
    if (minute.length == 1) minute = '0' + minute;
    second = String(parseInt(time % 60, 10));
    if (second.length == 1) second = '0' + second;
    return minute + ":" + second;
}

function updateProgress(ev) {
    /*显示歌曲总长度*/
    var songTime = calcTime(Math.floor(audio.duration));
    $(".duration").html(songTime);
    /*显示歌曲当前时间*/
    var curTime = calcTime(Math.floor(audio.currentTime));
    $(".position").html(curTime);
    /*进度条*/
    var lef = 678 * (Math.floor(audio.currentTime) / Math.floor(audio.duration));
    var llef = Math.floor(lef).toString() + "px";
    $(".dian").css("left", llef);
}

function audioPlay(ev) {
    $(".iplay").css("background", 'url("../../static/songlist/css/images/T1oHFEFwGeXXXYdLba-18-18.gif") 0 0');
    $(".playBtn").css("background-position", "0 -30px");
    $(".playBtn").attr("isplay", "1");
}

function audioPause(ev) {
    $(".iplay").css("background", "");

}

function audioEnded(ev) {
    var present_id = parseInt(songIndex);
    var present_num = $(".start em[sonN=" + present_id + "]").html();
    var sid = parseInt(present_num) + 1;
    $(".start em[id=" + sid + "]").click();
}


/*显示歌词部分*/
var scrollt = 0;
var tflag = 0;//存放时间和歌词的数组的下标
var lytext = new Array();//放存汉字的歌词
var lytime = new Array();//存放时间
var delay = 10;
var line = 0;
var scrollh = 0;
var songIndex = 2;


function getLy(s)//取得歌词
{
    lytext=[];
    lytime=[];
    var ly = " ";
    $.ajax({
    type: 'POST',
    url: "/lyric/search/",
    data: {sid: s},
    async: false,
    success: function (res) {
        ly = res;
    },
    error: function(){
        ly = "[00:00]该音乐暂无歌词";
    }}
    );
    return ly;
}

function show(t)//显示歌词
{
    var div1 = document.getElementById("lyr");//取得层
    document.getElementById("lyr").innerHTML = " ";//每次调用清空以前的一次
    if (t < lytime[lytime.length - 1])//先舍弃数组的最后一个
    {
        for (var k = 0; k < lytext.length; k++) {
            if (lytime[k] <= t && t < lytime[k + 1]) {
                scrollh = k * 25;//让当前的滚动条的顶部改变一行的高度
                div1.innerHTML += "<font color=#f60 style=font-weight:bold>" + lytext[k] + "</font><br>";
            } else if (t < lytime[lytime.length - 1])//数组的最后一个要舍弃
                div1.innerHTML += lytext[k] + "<br>";
        }
    } else//加上数组的最后一个
    {
        for (var j = 0; j < lytext.length - 1; j++)
            div1.innerHTML += lytext[j] + "<br>";
        div1.innerHTML += "<font color=red style=font-weight:bold>" + lytext[lytext.length - 1] + "</font><br>";
    }
}

function scrollBar()//设置滚动条的滚动
{
    if (document.getElementById("lyr").scrollTop <= scrollh)
        document.getElementById("lyr").scrollTop += 1;
    if (document.getElementById("lyr").scrollTop >= scrollh + 50)
        document.getElementById("lyr").scrollTop -= 1;
    window.setTimeout("scrollBar()", delay);
}

function getReady(s)//在显示歌词前做好准备工作
{
    var ly = getLy(s);//得到歌词
    //alert(ly);
    // lytext.length=0;
    // lytime.length=0;
    // lytext = new Array();
    // lytime = new Array();
    if (ly=="") {
        $("#lry").html("本歌暂无歌词！");
    }
    var arrly = ly.split("\n");//转化成数组
    tflag = 0;
    $("#lry").html(" ");
    document.getElementById("lyr").scrollTop = 0;
    for (var i = 0; i < arrly.length; i++)
        sToArray(arrly[i]);
    sortAr();
    scrollBar();
}

function sToArray(str)//解析如“[02:02][00:24]没想到是你”的字符串前放入数组
{
    if(str=="[00:00]该音乐暂无歌词"){
        lytext = ["该音乐暂无歌词"];
        lytime = [0];
        return
    }
    var left = 0;//"["的个数
    var leftAr = new Array();
    for (var k = 0; k < str.length; k++) {
        if (str.charAt(k) == "[") {
            leftAr[left] = k;
            left++;
        }
    }
    if (left != 0) {
        for (var i = 0; i < leftAr.length; i++) {
            lytext[tflag] = str.substring(str.lastIndexOf("]") + 1);//放歌词
            lytime[tflag] = conSeconds(str.substring(leftAr[i] + 1, leftAr[i] + 6));//放时间
            tflag++;
        }
    }
}

function sortAr()//按时间重新排序时间和歌词的数组
{
    var temp = null;
    var temp1 = null;
    for (var k = 0; k < lytime.length; k++) {
        for (var j = 0; j < lytime.length - k; j++) {
            if (lytime[j] > lytime[j + 1]) {
                temp = lytime[j];
                temp1 = lytext[j];
                lytime[j] = lytime[j + 1];
                lytext[j] = lytext[j + 1];
                lytime[j + 1] = temp;
                lytext[j + 1] = temp1;
            }
        }
    }
}

function conSeconds(t)//把形如：01：25的时间转化成秒；
{
    var m = t.substring(0, t.indexOf(":"));
    var s = t.substring(t.indexOf(":") + 1);
    m = parseInt(m.replace(/0/, ""));
    var totalt = parseInt(m) * 60 + parseInt(s);
    return totalt;
}


function mPlay()//开始播放
{
    var ms = audio.currentTime;
    show(ms);
    window.setTimeout("mPlay()", 100)
}
