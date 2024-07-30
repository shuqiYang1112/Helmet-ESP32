$(function () {
    setInterval(function () {
        $(".class_name").load(location.href + " .class_name");
    }, 3000);//设置自动刷新时间：3秒
})
