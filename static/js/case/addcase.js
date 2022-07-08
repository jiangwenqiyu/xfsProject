

function format() {
    param = $("#param").html()
    data = $("#data").html()
    $("#param").JSONView(JSON.parse(param));
    $("#data").JSONView(JSON.parse(data));

}



$('.do_add').click(function () {
    // 克隆pre对象，去掉-
    var param = $("#param").clone();
    param.find('.collapser').remove();

    var data = $("#data").clone();
    data.find('.collapser').remove();

    var assert = $("#param").clone();
    assert.find('.collapser').remove();




    // 保存测试用例
    route = $(".apiname").attr("caseurl");
    param = param.text();
    data = data.text();
    assert = assert.text();

    explain = $("#explain").val();
    apiname = $(".apiname").attr("apiname");
    coordinationId = $(".apiname").attr("coordinationId");

    // 必填校验
    if (data == '' || assert == '' || explain == '') {
        alert('有必填项为空');
        return;
    }

    $.ajax({
        url: '/case/do_add',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({"route":route,"param":param,"data":data,"exp":assert,"explain":explain,"apiname":apiname,"coordinationId":coordinationId}),
        success: function (resp) {
            alert(resp.msg);
        }

    });





});





$(document).ready(function () {

    format();
    $(function () {

        $("#param").blur(function () {
            param = $("#param")
            param.find('.collapser').remove()
            param = JSON.stringify(param.text());
            $("#param").JSONView(JSON.parse(param));
        });


        $("#data").blur(function () {
            data = $("#data")
            data.find('.collapser').remove()
            data = JSON.stringify(data.text());
            $("#data").JSONView(JSON.parse(data));
        });

        $("#assert").blur(function () {
            assert = $("#assert")
            assert.find('.collapser').remove()
            assert = JSON.stringify(assert.text());
            $("#assert").JSONView(JSON.parse(assert));
        });


    });
})






