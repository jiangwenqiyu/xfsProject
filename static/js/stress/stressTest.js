var currentLine = 2;
function addRow() {
    $('tbody').append('<tr><td>' + currentLine + '</td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td></tr>')
    currentLine += 1;
}


function generateScript() {
    var data = [];

    $('#urls').children().each(function (i) {
        if ($.trim($(this).children('td:eq(1)').children('input:eq(0)').val()) == '') {
            return 0;
        }else {
            var temp = [];

            $(this).children().each(function (x) {
                console.log(this)
                if (x != 0) {
                    if ($.trim($(this).children('input:eq(0)').val()) == '') {
                        alert('有内容没填');
                        throw '必填项不能为空';
                    } else {
                        if (x == 6 || x == 4 || x == 5) {
                            temp.push(
                                JSON.parse(
                                    $(this).children('input:eq(0)').val()
                                )
                            );
                        } else {
                            temp.push($(this).children('input:eq(0)').val());
                        }

                    }
                }
            });
            data.push(temp)
        }



    });

    if (JSON.stringify(data) == '[]') {
        alert('没有有效数据');
        return
    }


    $.ajax({
        url: '/stress/generateScript',
        type: 'post',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify({'data':data}),
        success: function (res) {
            if (res.status == '0') {

                $.ajax({
                    url: '/stress/exeScript',
                    type: 'post',
                    contentType: 'application/json',

                    success: function (res) {
                        if (res.status == '0') {
                            alert('脚本生成成功');
                            $('#switch').show();
                        } else {
                            alert(res.msg);
                        }

                    }
                })


            } else {
                alert(res.msg);
            }
        }

    });
}


function zhanyong() {
    $.ajax({
        url: '/stress/zhanyong',
        type: 'get',
        success: function (res) {
            alert(res.msg);
            if (res.status == '0') {
                $('#btn-gen').show();
            }

        }
    });



}


function zhanyong_release() {
    $.ajax({
        url: '/stress/zhanyong_release',
        type: 'get',
        success: function (res) {
            alert(res.msg);
            if (res.status == '0') {
                $('#btn-gen').hide();
                $('#switch').hide();
            }

        }
    });


}









