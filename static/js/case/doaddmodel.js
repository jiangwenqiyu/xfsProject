;
var member_reg_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".addmodel_wrap .do-addmodel").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                layer.alert("稍等，正处理呢～");
                return;
            }
            var apiname = $(".addmodel_wrap input[name = apiname]").val();
            var route = $(".addmodel_wrap input[name = route]").val();
            var parameter = $(".addmodel_wrap input[name = parameter]").val();
            var exp_parameter = $(".addmodel_wrap input[name = exp_parameter]").val();
            var method = $(".addmodel_wrap input[name = method]").val();
            var explain = $(".addmodel_wrap input[name = explain]").val();
            if (apiname == "undefined" || apiname.length < 1) {
                common_ops.alert("接口名称是必填项")
                return;
            }
            ;
            if (route == "undefined" || route.length < 1) {
                common_ops.alert("路径是必填项")
                return;
            }
            if (method == "undefined" || method.length < 1) {
                common_ops.alert("请求方法")
                return;
            }
            if (explain == "undefined" || explain.length < 1) {
                common_ops.alert("中文解释是必填项")
                return;
            }


            $.ajax({
                url: common_ops.buildUrl("/case/do_addmodel"),
                type: "POST",
                data: {
                    apiname: apiname,
                    route: route,
                    parameter: parameter,
                    exp_parameter: exp_parameter,
                    method: method,
                    explain: explain,


                },
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code = 200) {
                        callback = function () {
                            //           window.location = common_ops.buildUrl("/case/addmodel");
                        };

                    }
                    common_ops.alert(res.msg, callback)
                }
            })


        });
    }
}
$(document).ready(function () {
    member_reg_ops.init();
})