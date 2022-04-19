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
            var case_id = $("p.case_id").text()
            var user_id = document.getElementsByClassName("user_id");
            var paramname = document.getElementsByClassName("paramname");
            var exp_paramname = document.getElementsByClassName("exp_paramname");
            var pjname = $(".pjname:checked").val()
            var parammap = {}
            var exp_parammap = {}
            var paramnamsearray = new Array();
            var exp_paramnamsearray = new Array();
            var explain = $("#explain").val()


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

           // alert(exp_paramnamsearray[0].textContent)
         //   btn_target.addClass("disabled");


            $.ajax({
                url: common_ops.buildUrl("/case/do_edit"),
                type:"POST",
                data: {
                    case_id :case_id,
                    apiname : apiname,
                    param : case_data,
                    explain : explain,
                    expparam : exp_data,
                    pjname : pjname
                },
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code = 200) {
                        callback = function () {
                            window.location = common_ops.buildUrl("/case/mylist");
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
                            window.location = common_ops.buildUrl("/case/do_edit");
                        };

                    }
                    common_ops.alert(res.msg, callback)
                }
            })


        });


    }
}
$(document).ready(function () {
    member_login_ops.init();
})