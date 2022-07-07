

function format() {
    param = $("#param").html()
    data = $("#data").html()
    $("#param").JSONView(JSON.parse(param));
    $("#data").JSONView(JSON.parse(data));

}



$('.do_add').click(function () {

    var temp = $("#data").clone();
    var t = temp.find('.collapser').remove();


    // 保存测试用例
    route = $(".apiname").attr("caseurl");
    param = $("#param").text();
    // data = $("#data").text();
    data = temp.text();
    exp = $("#assert").text();
    explain = $("#explain").val();
    apiname = $(".apiname").attr("apiname");
    coordinationId = $(".apiname").attr("coordinationId");

    // 必填校验
    if (data == '' || exp == '' || explain == '') {
        alert('有必填项为空');
        return;
    }

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
            data = $("#assert").text()
            data = JSON.stringify(data);
            $("#assert").JSONView(JSON.parse(data));
        });

        $("#data").blur(function () {
            data = $("#data").text()
            data = JSON.stringify(data);
            $("#data").JSONView(JSON.parse(data));
        });
    });
})






