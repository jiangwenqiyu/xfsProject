;
var member_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".param_wrap .do_select").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                alert("稍等户，正处理呢～");
                return;
            }
            var address = $("#address").val()
            var pjname = $("#pjname").val()


            //       btn_target.addClass("disabled");

            $.ajax({
                url: common_ops.buildUrl("/case/case_list"),
                type: "POST",
                data: {
               //     address: address,
                    pjname: pjname,

                },
                dataType: 'json',
                success: function (res) {

                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code = 200) {
                        callback = function () {
                            window.location = common_ops.buildUrl("/case/case_list");
                        };

                    }
                    common_ops.alert(res.msg, callback)
                },

                error: function (res) {

                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code = 200) {
                        callback = function () {
                            window.location = common_ops.buildUrl("/case/case_list");
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