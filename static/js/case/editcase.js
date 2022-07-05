$('.do_add').click(function () {
    var temp = $("#data").clone();
    temp.find('.collapser').remove()


    param = $("#param").text()
    data = temp.text()
    assert = $("#assert").text()
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









$(document).ready(function () {
    function format() {
        param = $("#param").html()
        data = $("#data").html()
        assert = $("#assert").html()
        $("#param").JSONView(JSON.parse(param));
        $("#data").JSONView(JSON.parse(data));
        $("#assert").JSONView(JSON.parse(assert));

    }
    format();



})