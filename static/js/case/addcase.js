;
var member_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        // .expparam_wrap.addcase_wrap
        $(".param_wrap .do_add").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                alert("稍等户，正处理呢～");
                return;
            }
            var user_id = document.getElementsByClassName("user_id");
            var paramname = document.getElementsByClassName("paramname");
            var exp_paramname = document.getElementsByClassName("exp_paramname");
            var pjname = $(".pjname:checked").val()
            var parammap = {}
            var exp_parammap = {}
            var paramnamsearray = new Array();
            var exp_paramnamsearray = new Array();
            var explain = $("#explain").val()
            var exp_data =$('.result').text()


            for (var p = 0; p < paramname.length; p++) {
                paramnamsearray[p] = paramname[p].textContent
            }
            for (var i = 0; i < paramnamsearray.length; i++) {
                parammap[paramnamsearray[i]] = $(".param_wrap input[name =" + paramnamsearray[i] + "]").val();
            }

            for (var p = 0; p < exp_paramname.length; p++) {
                exp_paramnamsearray[p] = exp_paramname[p].textContent
            }
            for (var i = 0; i < exp_paramnamsearray.length; i++) {
                exp_parammap[exp_paramnamsearray[i]] = $(".param_wrap input[name =" + exp_paramnamsearray[i] + "]").val();
            }
            var apiname = $(".apiname").text();

            user_id = user_id[0].textContent
            var case_data = JSON.stringify(parammap)
            var exp_data = JSON.stringify(exp_parammap)


            //   btn_target.addClass("disabled");


            $.ajax({
                url: common_ops.buildUrl("/case/do_add"),
                type: "POST",
                data: {
                    apiname: apiname,
                    param: case_data,
                    explain: explain,
                    expparam: exp_data,
                    pjname: pjname
                },
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;

                    if (res.code = 200) {
                        callback = function () {
                            //  window.location = common_ops.buildUrl("/case/taddcase.html");
                            //  window.location =helper.ops_renderJSON("提交成功")
                        };

                    }
                    common_ops.alert(res.msg, callback)
                },
                error: function (res) {

                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code = 200) {
                        callback = function () {
                            window.location = common_ops.buildUrl("/case/taddcase");
                        };

                    }
                    common_ops.alert(res.msg, callback)
                }
            })

        });
        $(".param_wrap .create_jsondata").click(function () {

            var paramname = document.getElementsByClassName("paramname");
            var paramnamsearray = new Array();
            var parammap = {}
            for (var p = 0; p < paramname.length; p++) {
                paramnamsearray[p] = paramname[p].textContent
            }
            for (var i = 0; i < paramnamsearray.length; i++) {
                parammap[paramnamsearray[i]] = $(".param_wrap input[name =" + paramnamsearray[i] + "]").val();
            }
            var case_data = JSON.stringify(parammap)
            var apiname = $(".apiname").text();
            //   alert(typeof (case_data))

            //    var url = "http://192.168.0.121:8050/cmps/srm/Supplier/querySupplierInfo"
            //   var jsondata = common_ops.send_requests(url, "POST", case_data)
            //   alert(jsondata)
            // 异步对象
            $.ajax({
                url: common_ops.buildUrl("/case/create_json"),
                type: "POST",
                //  async: true,
                data: {
                    apiname: apiname,
                    case_data: case_data,
                },
                //  dataType: 'json',
                success: function (data) {

                    function prettyJson(data) {  // 常规方法
                        json = JSON.parse(data);
                        $("#showjson").JSONView(json);
                    }

                    function prettyJsonSpecial(data) {   // 需要特殊处理的
                        json = JSON.parse(data);
                        content = json.data;
                        content = JSON.parse(content);
                        exp_json = {'data': content};
                        $("#showjson").JSONView(exp_json);
                    }


                    var d = $('.result').html(data.replace(/\\/g, ""));
                    if ( 'querySupplierInfo' == 'querySupplierInfo') {   //  哪些需要特殊处理的，走这个方法
                        prettyJsonSpecial(data);

                    } else {
                        prettyJson(data);
                    }




                }


            })

        })
    }
}

$(document).ready(function () {


    member_login_ops.init();
})