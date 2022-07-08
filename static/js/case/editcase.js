$('.do_add').click(function () {
    // 克隆pre对象，去掉-
    var param = $("#param").clone();
    param.find('.collapser').remove();

    var data = $("#data").clone();
    data.find('.collapser').remove();

    var assert = $("#param").clone();
    assert.find('.collapser').remove();


    param = param.text()
    data = data.text()
    assert = assert.text()
    explain = $("#explain").val();
    caseid = $(".case_id").text();

    var d = {};
    d['param'] = param
    d['data'] = data
    d['assert'] = assert
    d['explain'] = explain
    d['caseid'] = caseid

    $.ajax({
        url: '/case/do_edit',
        type: 'post',
        dataType:'json',
        contentType: 'application/json',
        data: JSON.stringify(d),
        success: function (resp) {
            alert(resp.msg);
        }
    })


});


function format() {
    param = $("#param").html()
    data = $("#data").html()
    assert = $("#assert").html()
    $("#param").JSONView(JSON.parse(param));
    $("#data").JSONView(JSON.parse(data));
    $("#assert").JSONView(JSON.parse(assert));

}






$(document).ready(function () {
    // 初始格式化
    format();
    // 鼠标移开执行
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