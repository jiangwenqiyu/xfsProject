;
var member_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        // .expparam_wrap.addcase_wrap
        $(".test_wrap .param_wrap .do-test").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                alert("稍等户，正处理呢～");
                return;
            }
            var case_id = $(this).attr("name");

            alert(case_id)

            $.ajax({
                url: common_ops.buildUrl("/case/do_add"),
                type: "POST",
                data: {
                    case_id: case_id,
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
        $(".test_wrap .do-alltest").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                alert("稍等户，正处理呢～");
                return;
            }
            //    var case_id = $(this).attr("name");
            var case_id = document.getElementsByClassName("allcase");
            //    var case_id = $(".param_wrap:p").val()
            //     var case_id = $("#case_id").val()
            var case_allarray = new Array()

            for (var i = 0; i < case_id.length; i++) {
                case_allarray[i] = case_id[i].textContent

            }


            var case_all = case_allarray.toString()


            //   btn_target.addClass("disabled");

            $.ajax({
                url: common_ops.buildUrl("/case/do_add"),
                type: "POST",
                data: {
                    case_all: case_all,
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

        $(".test_wrap .do-select").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                alert("稍等户，正处理呢～");
                return;
            }

            var selectnum = document.getElementsByName("choose")
            var case_select =[]
            for (var i=0;i<selectnum.length;i++){
                if(selectnum[i].checked){
                    case_select[i] = selectnum[i].value
                }
            }

            alert(case_select)



                        //   btn_target.addClass("disabled");

                        $.ajax({
                            url: common_ops.buildUrl("/case/do_add"),
                            type: "POST",
                            data: {
                                case_select: case_select,
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


    }
}
$(document).ready(function () {
    member_login_ops.init();
})