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
            var func_id = $("#funcInfo option:selected").attr('value');
            var header = $(".addmodel_wrap input[name = header]").val();


            if (func_id == null || func_id == "None") {
                common_ops.alert("系统功能没有选择")
                return;
            }
            if (apiname == "undefined" || apiname.length < 1) {
                common_ops.alert("接口名称是必填项")
                return;
            }
            if (explain == "undefined" || explain.length < 1) {
                common_ops.alert("中文解释是必填项")
                return;
            }

            if (route == "undefined" || route.length < 1) {
                common_ops.alert("路径是必填项")
                return;
            }
            if (method == "undefined" || method.length < 1) {
                common_ops.alert("请求方法")
                return;
            }
            if (param == "undefined" || param.length < 1) {
                common_ops.alert("param是必填项")
                return;
            }
            if (data == "undefined" || data.length < 1) {
                common_ops.alert("请求参数是必填项")
                return;
            }
            if (dataType == "undefined" || dataType.length < 1) {
                common_ops.alert("参数类型是必填项")
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
                    dataType: dataType,
                    func_id: func_id,
                    header: header

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




$("#upexcel").click(function () {
    var formData = new FormData($('#uploadForm')[0]);
    $.ajax({
        type: 'post',
        url: "/case/batchExportModel", //上传文件的请求路径必须是绝对路劲
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
    }).success(function (resp) {
        alert(resp.msg);
        filename=data;
    }).error(function () {
        alert("上传失败");
    });
});
