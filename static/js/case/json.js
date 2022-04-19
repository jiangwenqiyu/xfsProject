;
var member_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        // .expparam_wrap.addcase_wrap
        $(".param_wrap .create_jsondata").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                alert("稍等户，正处理呢～");
                return;
            }
            var url = "http://192.168.0.121:8050/cmps/srm/Supplier/querySupplierInfo"


            //   btn_target.addClass("disabled");
            var paramname = document.getElementsByClassName("paramname");
            var paramnamsearray = new Array();
            for (var p = 0; p < paramname.length; p++) {
                paramnamsearray[p] = paramname[p].textContent
            }
            for (var i = 0; i < paramnamsearray.length; i++) {
                parammap[paramnamsearray[i]] = $(".param_wrap input[name =" + paramnamsearray[i] + "]").val();
            }
            alert(parammap)
            var jsondata = common_ops.send_requests(url, "POST", parammap)
            if (typeof jsondata != 'string') {
                jsondata = JSON.stringify(json, undefined, 2);
            }
            jsondata = jsondata.replace(/&/g, '&').replace(/</g, '<').replace(/>/g, '>');
            return jsondata.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g,
                function (match) {
                    var cls = 'number';
                    if (/^"/.test(match)) {
                        if (/:$/.test(match)) {
                            cls = 'key';
                        } else {
                            cls = 'string';
                        }
                    } else if (/true|false/.test(match)) {
                        cls = 'boolean';
                    } else if (/null/.test(match)) {
                        cls = 'null';
                    }
                    return '<span class="' + cls + '">' + match + '</span>';
                }
            );
            $('#result').html(syntaxHighlight(res));

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
                            // window.location = common_ops.buildUrl("/case/taddcase.html");
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


    }
}
$(document).ready(function () {
    member_login_ops.init();
})