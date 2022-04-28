

function format() {
    param = $("#param").html()
    data = $("#data").html()
    $("#param").JSONView(JSON.parse(param));
    $("#data").JSONView(JSON.parse(data));

}



$('.do_add').click(function () {
    // 保存测试用例
    route = $(".apiname").attr("caseurl");
    param = $("#param").text();
    data = $("#data").text();
    exp = $("#assert").text();
    explain = $("#explain").val();
    apiname = $(".apiname").attr("apiname");
    coordinationId = $(".apiname").attr("coordinationId");

    $.ajax({
        url: '/case/do_add',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({"route":route,"param":param,"data":data,"exp":exp,"explain":explain,"apiname":apiname,"coordinationId":coordinationId}),
        success: function (resp) {
            alert(resp.msg);
        }

    });





});





$(document).ready(function () {

    format();
    $(function () {
        $("#assert").blur(function () {
            data = $("#assert").html()
            $("#assert").JSONView(JSON.parse(data));
        });
    });
})






