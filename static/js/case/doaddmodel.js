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
            var explain = $(".addmodel_wrap input[name = explain]").val();
            var route = $(".addmodel_wrap input[name = route]").val();
            var method = $(".addmodel_wrap input[name = method]").val();
            var param = $(".addmodel_wrap input[name = param]").val();
            var data = $(".addmodel_wrap input[name = data]").val();
            var dataType = $(".addmodel_wrap input[name = dataType]").val();


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
                    explain: explain,
                    route: route,
                    method: method,
                    param: param,
                    data: data,
                    dataType: dataType


                },
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